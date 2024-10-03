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
    tax_exemption_doc = fields.Binary(string='Fiscal Position', attachment=True)
    tax_exemption_doc_name = fields.Char(string='Fiscal Position Name')


    @api.model
    def create_attachment_record(self, vals):
        # Create the record
        record = super(ResPartnerInherit, self).create(vals)

        # Create an attachment if the binary field has data
        if vals.get('contractor_doc'):

            record.x_studio_contractor_doc = vals.get('contractor_doc')
            record.x_studio_contractor_doc_filename = vals.get('contractor_doc_name')

            self.env['ir.attachment'].create_attachment_record({
                'name': vals.get('contractor_doc_name'),
                'type': 'binary',
                'datas': vals.get('contractor_doc'),
                'res_model': self._name,
                'res_id': record.id,
            })
            
        return record

