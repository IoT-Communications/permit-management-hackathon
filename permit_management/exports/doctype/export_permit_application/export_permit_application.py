# Copyright (c) 2022, IoT Communications (Pty) Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.integrations.utils import get_payment_gateway_controller
from frappe.utils import flt, get_url, nowdate

class ExportPermitApplication(Document):

	def on_update(self):

		if self.workflow_state == "Compliant and Ready for Payment":

			controller = get_payment_gateway_controller(self.payment_gateway)

			controller.validate_transaction_currency(self.currency)

			# Application Payment Url
			app_redirect_to = controller.get_payment_url(**{
				"amount": flt(self.application_fee),
				"title": "IoT Communications Payment Gateway".encode("utf-8"),
				"description": ("Payment Request for Application " + self.name).encode("utf-8"),
				"reference_doctype": self.doctype,
				"reference_docname": self.name,
				"payer_email": self.contact_email,
				"payer_name": self.company_name,
				"order_id": self.name,
				"currency": self.currency
			})

			licence_redirect_to = controller.get_payment_url(**{
				"amount": flt(self.licence_fee),
				"title": "IoT Communications Payment Gateway".encode("utf-8"),
				"description": ("Payment Request for Application " + self.name).encode("utf-8"),
				"reference_doctype": self.doctype,
				"reference_docname": self.name,
				"payer_email": self.contact_email,
				"payer_name": self.company_name,
				"order_id": self.name,
				"currency": self.currency
			})

			self.app_payment_url = app_redirect_to
			self.db_set('app_payment_url', self.app_payment_url)

			self.licence_payment_url = licence_redirect_to
			self.db_set('licence_payment_url', self.licence_payment_url)



	def on_payment_authorized(self, status=None):

		if not status:
			return


		if status in ["Authorized", "Completed"]:
			frappe.flags.ignore_account_permission = True

			redirect_to = None
			doc = frappe.get_doc(self.doctype, self.name)

			if doc.workflow_state == "Pending Application Fee Payment":
				doc.workflow_state = "Application Fee Paid"
				doc.save(ignore_permissions=True)

				#redirect to application
				redirect_to = get_url("/app/export-permit-application/" + self.name)
				return redirect_to


			elif doc.workflow_state == "Pending Licence Fee Payment":
				doc.workflow_state = "Licence Fee Paid"
				doc.save(ignore_permissions=True)

				#redirect to application
				redirect_to = get_url("/app/export-permit-application/" + self.name)
				return redirect_to

