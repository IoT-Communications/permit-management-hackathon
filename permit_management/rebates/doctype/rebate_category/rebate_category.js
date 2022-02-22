// Copyright (c) 2022, IoT Communications (Pty) Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Rebate Category', {
	// refresh: function(frm) {

	    refresh: function(frm) {
        frm.add_custom_button('Apply for Certificate', () => {
            frappe.new_doc('Rebate Certificate Application', {
                rebate_certificate_type: frm.doc.name,
				application_fee: frm.doc.application_fee
            })
        })
        
		}

	// }
});
