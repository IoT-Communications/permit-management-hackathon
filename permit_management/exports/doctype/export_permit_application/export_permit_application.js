// Copyright (c) 2022, IoT Communications (Pty) Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Export Permit Application', {
	refresh: function(frm) {

		if(frm.doc.workflow_state == 'Pending Application Fee Payment'){
		    
    		window.location.replace(frm.doc.app_payment_url);
    	
    	}
    		
    	else if(frm.doc.workflow_state == 'Pending Licence Fee Payment'){
    	    window.location.replace(frm.doc.licence_payment_url);
    	}

	 }
});
