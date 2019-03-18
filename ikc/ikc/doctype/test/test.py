# -*- coding: utf-8 -*-
# Copyright (c) 2019, IK control and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import get_datetime
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from frappe.model.document import Document
import time


#---------------------------------------------------------------------------# 
# configure the client logging
#---------------------------------------------------------------------------# 
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)



#rr = client.read_holding_registers(0, 6, unit=1)

class TEST(Document):
	rr = 10
	def data(self):
		client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=19200, bytesize=8, parity='N', stopbits=2)
		# frappe.msgprint("Hello")
		#print(client)
		client.connect()
		self.temperature = rr
		self.save()
		frappe.db.commit()

	def autoname(self):
		self.name = get_datetime().strftime("%Y-%m-%d %H:%M:%S")

@frappe.whitelist()
def get_plc_data():
	"""
		Runs every second to store PLC Data
	"""

	client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=19200, bytesize=8, parity='N', stopbits=2)
	if client.connect():
		for _ in range(60):
			result = client.read_holding_registers(0, 6, unit=1)
			doc = frappe.new_doc("TEST")
			doc.one = result.registers[0]
			doc.two = result.registers[1]
			doc.three = result.registers[2]
			doc.four = result.registers[3]
			doc.five = result.registers[4]
			doc.six = result.registers[5]

			doc.save()
			frappe.db.commit()
			time.sleep(1)
