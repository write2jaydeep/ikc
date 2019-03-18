// Copyright (c) 2019, IK control and contributors
// For license information, please see license.txt

frappe.ui.form.on('Main Control', {
	onload: function(frm){
		frappe.realtime.on("periodic_data_results", function(data){
			for(var key in data){
				console.log(key, data[key]);
				frm.set_value(key, data[key]);
				frm.refresh_fields()
			}
		})
	},
	refresh: function(frm) {
		cur_frm.disable_save();
	}
});
