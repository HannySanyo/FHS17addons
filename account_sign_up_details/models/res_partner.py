#################################################################################
# File Name: res_partner.py
# Revision History:  Engineer    Date          Description
#                    G. Sanyo    09/29/2024    Creation
#################################################################################
from odoo import models, fields, api

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    contractor_doc = fields.Binary(string='Contractor Document', attachment=True)
    contractor_doc_name = fields.Char(string='Contractor Document Name')
    tax_exemption_doc = fields.Binary(string='Tax Exemption Document', attachment=True)
    tax_exemption_doc_name = fields.Char(string='Tax Exemption Document Name')
