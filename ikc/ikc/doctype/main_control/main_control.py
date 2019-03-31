# -*- coding: utf-8 -*-
# Copyright (c) 2019, IK control and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import flt
from frappe.model.document import Document
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time

from ikc.data import set_address_value, publish_data

admin_dict = frappe.db.get_singles_dict("Admin Control")
client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=115200, bytesize=8, parity='N', stopbits=1)

try:
	client.connect()
except:
	args = {
		'message': "Cannot connect to PLC. Please check you connection. Trying to reconnect after 1 minute",
		'title': "PLC Connection Error"
	}

	frappe.log_error(**args)
	# Add js to app for frappe.realtime.on
	publish_data(args, 1)

# START_PB	PLC1[000021]
# STOP_PB	PLC1[000022]
# RESET_PB	PLC1[000215]

START_PB = 021
STOP_PB	 = 022
RESET_PB = 215

# DOOR_1_OPEN_PB	PLC1[000287]
# DOOR_1_CLOSE_PB	PLC1[000279]
# DOOR_2_OPEN_PB	PLC1[000302]
# DOOR_2_CLOSE_PB	PLC1[000291]

DOOR_1_OPEN_PB = 287
DOOR_1_CLOSE_PB = 279
DOOR_2_OPEN_PB = 302
DOOR_2_CLOSE_PB = 291

def get_delay(field):
	return flt(admin_dict.get(field, 10)) / 1000.0

class MainControl(Document):
	def start(self):
		delay = get_delay('start_delay')

		# Change start address register bit from 0 to 1
		set_address_value(START_PB, 1, client)
		time.sleep(delay)
		
		set_address_value(START_PB, 0, client)
		# Change start address register bit from 1 to 0

	def stop(self):
		delay = get_delay('stop_delay')
		# delay = flt(admin_dict.get('stop_delay', 10)) / 1000.0

		# Change stop address register bit from 0 to 1
		set_address_value(STOP_PB, 1, client)
		time.sleep(delay)
		
		set_address_value(STOP_PB, 0, client)
		# Change stop address register bit from 1 to 0

	def reset(self):
		delay = get_delay('reset_delay')
		# delay = flt(admin_dict.get('reset_delay', 10)) / 1000.0

		# Change reset address register bit from 0 to 1
		set_address_value(RESET_PB, 1, client)
		time.sleep(delay)
		
		set_address_value(RESET_PB, 0, client)
		# Change reset address register bit from 1 to 0

	def open_door_1(self):
		set_address_value(DOOR_1_OPEN_PB, 1, client)
		time.sleep(0.01)
		
		set_address_value(DOOR_1_OPEN_PB, 0, client)

	def open_door_2(self):
		set_address_value(DOOR_2_OPEN_PB, 1, client)
		time.sleep(0.01)
		
		set_address_value(DOOR_2_OPEN_PB, 0, client)

	def close_door_1(self):
		set_address_value(DOOR_1_CLOSE_PB, 1, client)
		time.sleep(0.01)
		
		set_address_value(DOOR_1_CLOSE_PB, 0, client)

	def close_door_2(self):
		set_address_value(DOOR_2_CLOSE_PB, 1, client)
		time.sleep(0.01)
		
		set_address_value(DOOR_2_CLOSE_PB, 0, client)