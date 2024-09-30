#################################################################################
# File Name: res_partner.py
# Revision History:  Engineer    Date          Description
#                    G. Sanyo    09/29/2024    Creation
#################################################################################
from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    attachment = fields.Binary(string="Attachment", attachment=True)
    attachment_name = fields.Char(string='Attachment Name')


	# @api.constrains('phone')
	# def age_cal(self):
	# 	for rec in self:	
	# 		if self.wk_dob > date.today():
	# 			raise ValidationError("DOB should not exceed the Current Date")
					