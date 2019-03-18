# -*- coding: utf-8 -*-
# Copyright (c) 2019, IK control and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import now, get_datetime

import time
from pymodbus.client.sync import ModbusSerialClient as ModbusClient


# TODO: Uncomment Modbus communication
@frappe.whitelist()
def get_sensor_data():
	"""
		Runs every second to get data from PLC and store into Periodic Sensor Data
	"""
	test_data()


def test_data():
	# client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=19200, bytesize=8, parity='N', stopbits=2)
	if True:
	# if client.connect():
		
		for _ in range(60):
			if get_datetime().minute == 0 and get_datetime().second == 0:
				frappe.db.sql(""" DELETE from `tabTEST` """)
			# result = client.read_holding_registers(0, 6, unit=1)
			# doc = frappe.new_doc("TEST")
			# doc.one = result.registers[0]
			# doc.two = result.registers[1]
			# doc.three = result.registers[2]
			# doc.four = result.registers[3]
			# doc.five = result.registers[4]
			# doc.six = result.registers[5]
			frappe.get_doc({
				'doctype': "TEST",
				'one': 1,
				'two': 2,
				'three': 3,
				'four': 4,
				'five': 5,
				'six': 6,
			}).insert()
			frappe.db.commit()
			time.sleep(1)
