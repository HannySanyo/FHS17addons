#################################################################################
# File Name: res_partner.py
# Revision History:  Engineer    Date          Description
#                    G. Sanyo    09/29/2024    Creation
#################################################################################
from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Field for contractor attachment
    attachment_contractor = fields.Binary(
        string="Contractor License Document",
        attachment=True,
        help="If you are a contractor, please provide contractor license documentation."
    )
    attachment_contractor_name = fields.Char(
        string='Contractor Attachment Name',
        help="Name of the contractor attachment file."
    )

    # Field for tax exemption attachment
    attachment_taxexempt = fields.Binary(
        string="Tax Exempt Document",
        attachment=True,
        help="If you are tax exempt, please provide proof of exemption documentation."
    )
    attachment_taxexempt_name = fields.Char(
        string='Tax Exempt Attachment Name',
        help="Name of the tax exempt attachment file."
    )


	# @api.constrains('phone')
	# def age_cal(self):
	# 	for rec in self:	
	# 		if self.wk_dob > date.today():
	# 			raise ValidationError("DOB should not exceed the Current Date")
					