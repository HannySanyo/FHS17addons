#################################################################################
# File Name: res_partner.py
# Revision History:  Engineer    Date          Description
#                    G. Sanyo    09/29/2024    Creation
#################################################################################
from odoo import api, fields, models, _
import re
from datetime import datetime,date
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
	_inherit = 'res.partner'

	wk_dob = fields.Date( string='Phone Number')

	# @api.constrains('phone')
	# def age_cal(self):
	# 	for rec in self:	
	# 		if self.wk_dob > date.today():
	# 			raise ValidationError("DOB should not exceed the Current Date")
					