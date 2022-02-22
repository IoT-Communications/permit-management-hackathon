// Copyright (c) 2022, IoT Communications (Pty) Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Import Permit Application', {
	 refresh: function(frm) {

		if(frm.doc.workflow_state == 'Pending Payment'){
    		    
    		    window.location.replace(frm.doc.payment_url);
    		}

	 }
});
