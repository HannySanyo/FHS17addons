from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    wk_dob = fields.Date(string='Date of Birth')
    custom_field_1 = fields.Binary(string="Custom File Upload 1")  # Binary field for file attachments
    custom_field_2 = fields.Binary(string="Custom File Upload 2")  # Binary field for file attachments
