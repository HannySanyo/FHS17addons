#################################################################################
# File Name: res_partner.py
# Revision History:  Engineer    Date          Description
#                    G. Sanyo    09/29/2024    Creation
#################################################################################
from odoo import models, fields, api

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    # attachment = fields.Binary(string="Attachment", attachment=True)
    # attachment_name = fields.Char(string='Attachment Name')

    # @api.model
    # def update_custom_field(self, vals):
    #     partners = self.search([('active', '=', True)])
    #     for partner in partners:
    #         partner.x_studio_contractor_doc = vals.get('attachment') 
    #         partner.x_studio_contractor_doc_filename = vals.get('attachment_name')

    # @api.model
    # def create_attachment_record(self, vals):
    #     # Create the record
    #     record = super(ResPartnerInherit, self).create(vals)

        # # Create an attachment if the binary field has data
        # if vals.get('attachment'):

        #     #record.x_studio_contractor_doc = vals.get('attachment')
        #     #record.x_studio_contractor_doc_filename = vals.get('attachment_name')

        #     self.env['ir.attachment'].create_attachment_record({
        #         'name': vals.get('attachment_name'),
        #         'type': 'binary',
        #         'datas': vals.get('attachment'),
        #         'res_model': self._name,
        #         'res_id': record.id,
        #     })

        # return record