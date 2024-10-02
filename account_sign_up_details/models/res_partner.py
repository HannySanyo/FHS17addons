#################################################################################
# File Name: res_partner.py
# Revision History:  Engineer    Date          Description
#                    G. Sanyo    09/29/2024    Creation
#################################################################################
from odoo import models, fields, api

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    attachment = fields.Binary(string='Attachment', attachment=True)
    attachment_name = fields.Char(string='Attachment Name')

    @api.model
    def create_attachment_record(self, vals):
        # Create the record
        record = super(ResPartnerInherit, self).create(vals)

        # Create an attachment if the binary field has data
        if vals.get('attachment'):
            self.env['ir.attachment'].create_attachment_record({
                'name': vals.get('attachment_name'),
                'type': 'binary',
                'datas': vals.get('attachment'),
                'res_model': self._name,
                'res_id': record.id,
            })
        return record