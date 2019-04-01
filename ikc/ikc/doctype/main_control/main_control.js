// Copyright (c) 2019, IK control and contributors
// For license information, please see license.txt

frappe.ui.form.on('Main Control', {
	onload: function(frm){
		frappe.realtime.on("periodic_data_results", function(data){
			for(var key in data){
				// console.log(key, data[key]);
				frm.set_value(key, data[key]);
				frm.refresh_fields();
			}
		})
	},
	refresh: function(frm) {
		cur_frm.disable_save();
	},
	start: function(frm){
		frm.events.update_address_value(frm, 'start');
			frappe.show_alert("Started");
	},
	stop: function(frm){
		frm.events.update_address_value(frm, 'stop');
		frappe.show_alert("Stopped");
	},
	reset: function(frm){
		frm.events.update_address_value(frm, 'reset');
		frappe.show_alert("Resetted");
	},
	open_door_1: function(frm){
		frm.events.update_address_value(frm, 'open_door_1');
		frappe.show_alert("Door One Opened.");
	},
	open_door_2: function(frm){
		frm.events.update_address_value(frm, 'open_door_2');
		frappe.show_alert("Door Two Opened.");
	},
	close_door_1: function(frm){
		frm.events.update_address_value(frm, 'close_door_1');
		frappe.show_alert("Door One Closed.");
	},
	close_door_2: function(frm){
		frm.events.update_address_value(frm, 'close_door_2');
		frappe.show_alert("Door Two Closed.");
	},
	update_address_value: function(frm, event){
		frm.call({
			method: event,
			doc: frm.doc,
			callback: function(r){
				if(!r.exc){
					return
				}
			}
		});
	}
});
