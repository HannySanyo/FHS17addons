#################################################################################
# File Name: res_partner.py
# Revision History:  Engineer    Date          Description
#                    G. Sanyo    09/29/2024    Creation
#################################################################################
import base64
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

            datas = base64.b64encode((vals.get('contractor_doc').read())
            filename = vals.get('contractor_doc_name')
                                     
            record.x_studio_contractor_doc = datas
            record.x_studio_contractor_doc_filename = filename

            self.env['ir.attachment'].create_attachment_record({
                'name': filename,
                'type': 'binary',
                'datas': datas,
                'res_model': self._name,
                'res_id': record.id,
            })
            
        return record

