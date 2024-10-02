#################################################################################
# File Name: res_partner.py
# Revision History:  Engineer    Date          Description
#                    G. Sanyo    09/29/2024    Creation
#################################################################################
from odoo import models, fields, api
import logging

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    x_studio_contractor_doc = fields.Binary(string='Documentation', attachment=True)
    x_studio_contractor_doc_filename = fields.Char(string='Documentation Name')

    @api.model
    def create_attachment_record(self, vals):
        # Create the record
        record = super(ResPartnerInherit, self).create(vals)

        # Create an attachment if the binary field has data
        if vals.get('x_studio_contractor_doc'):
            self.env['ir.attachment'].create_attachment_record({
                'name': vals.get('x_studio_contractor_doc_filename'),
                'type': 'binary',
                'datas': vals.get('x_studio_contractor_doc'),
                'res_model': self._name,
                'res_id': record.id,
            })
        return record