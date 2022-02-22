// Copyright (c) 2022, IoT Communications (Pty) Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Export Category', {
	// refresh: function(frm) {

	    refresh: function(frm) {
        frm.add_custom_button('Apply for Permit', () => {
            frappe.new_doc('Export Permit Application', {
                export_permit_type: frm.doc.name,
				application_fee: frm.doc.application_fee,
				licence_fee: frm.doc.licence_fee
            })
        })
        
		}

	// }
});
