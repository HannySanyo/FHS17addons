
from odoo import api, fields, models, _
import re
from datetime import datetime,date
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
	_inherit = 'res.partner'

	wk_dob = fields.Date( string='Date of Birth')
	custom_field_1 = fields.Char(string="Custom Field 1")
	custom_field_2 = fields.Char(string="Custom Field 2")

	@api.constrains('wk_dob')
	def age_cal(self):
		for rec in self:	
			if self.wk_dob > date.today():
				raise ValidationError("DOB should not exceed the Current Date")
					