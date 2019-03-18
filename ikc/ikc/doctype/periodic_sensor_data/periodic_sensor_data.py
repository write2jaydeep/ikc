# -*- coding: utf-8 -*-
# Copyright (c) 2019, IK control and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import get_datetime
from frappe.model.document import Document

class PeriodicSensorData(Document):
	def autoname(self):
		if not self.get('timestamp'):
			self.name = get_datetime().strftime("%Y-%m-%d %H:%M:%S")
		else:
			self.name = self.timestamp
