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
    fiscal_pos_doc = fields.Binary(string='Fiscal Position', attachment=True)
    fiscal_pos_doc_name = fields.Char(string='Fiscal Position Name')
