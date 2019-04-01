# -*- coding: utf-8 -*-
# Copyright (c) 2019, IK control and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt
from frappe.model.document import Document
import time

from ikc.data import set_address_value, publish_data

admin_dict = frappe.db.get_singles_dict("Admin Control")

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

class MainControl(Document):
	def start(self):
		delay = get_delay('start_delay')
		change_address_1_0(START_PB, delay)

	def stop(self):
		delay = get_delay('stop_delay')
		change_address_1_0(STOP_PB, delay)

	def reset(self):
		delay = get_delay('reset_delay')
		change_address_1_0(RESET_PB, delay)

	def open_door_1(self):
		change_address_1_0(DOOR_1_OPEN_PB)

	def open_door_2(self):
		change_address_1_0(DOOR_2_OPEN_PB)

	def close_door_1(self):
		change_address_1_0(DOOR_1_CLOSE_PB)

	def close_door_2(self):
		change_address_1_0(DOOR_2_CLOSE_PB)

def get_delay(field):
	return flt(admin_dict.get(field, 10)) / 1000.0

def change_address_1_0(address, delay=0.01):
	set_address_value(address, 1)
	time.sleep(delay)
	set_address_value(address, 0)
