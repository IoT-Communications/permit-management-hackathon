// Copyright (c) 2022, IoT Communications (Pty) Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Import Permit Category', {
	// refresh: function(frm) {

	    refresh: function(frm) {
        frm.add_custom_button('Apply for Permit', () => {
            frappe.new_doc('Import Permit Application', {
                import_permit_type: frm.doc.name,
				application_fee: frm.doc.app_fee
            })
        })
        
		}

	// }
});
