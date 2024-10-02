#################################################################################
# File Name: res_partner.py
# Revision History:  Engineer    Date          Description
#                    G. Sanyo    09/29/2024    Creation
#################################################################################
from odoo import models, fields, api

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    contractor_doc = fields.Binary(string='Contractor Doc', attachment=True)
    contractor_doc_name = fields.Char(string='Contractor Doc Name')
    tax_exemption_doc = fields.Binary(string='Tax Exemption', attachment=True)
    tax_exemption_doc_name = fields.Char(string='Tax Exemption Name')
