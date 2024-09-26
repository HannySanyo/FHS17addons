from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    wk_dob = fields.Date(string='Date of Birth')
    custom_field_1 = fields.Binary(string="Custom File Upload 1", attachment=True)
    custom_field_2 = fields.Binary(string="Custom File Upload 2", attachment=True)