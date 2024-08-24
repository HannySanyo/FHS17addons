from odoo import models, fields

class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    create_date = fields.Datetime(string='Creation Date', readonly=False)
