# -*- coding: utf-8 -*-
#################################################################################
#
# Copyright (c) 2018-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>:wink:
# See LICENSE file for full copyright and licensing details.
#################################################################################
from odoo import api, fields, models, _
import re
from datetime import datetime,date
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
	_inherit = 'res.partner'

# 	wk_dob = fields.Date( string='Date of Birth')
	phone = fields.phone( string='Date of Birth')

# 	@api.constrains('wk_dob')
# 	def age_cal(self):
# 		for rec in self:	
# 			if self.wk_dob > date.today():
# 				raise ValidationError("DOB should not exceed the Current Date")
					