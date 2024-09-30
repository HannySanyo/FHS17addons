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

    attachment_contractor = fields.Binary(string="If you are a contractor, please provide contractor license documentation:", attachment=True)
    attachment_contractor_name = fields.Char(string='Contractor Attachment Name')
	attachment_taxexempt = fields.Binary(string="If you are tax exempt, please provide proof of exemption documentation:", attachment=True)
    attachment_taxrexempt_name = fields.Char(string='Tax Exempt Attachment Name')

	# @api.constrains('phone')
	# def age_cal(self):
	# 	for rec in self:	
	# 		if self.wk_dob > date.today():
	# 			raise ValidationError("DOB should not exceed the Current Date")
					