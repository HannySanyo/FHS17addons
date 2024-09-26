from odoo import models, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def signup(self, values, token=None):
        if token:
            partner = self.env['res.partner']._signup_retrieve_partner(token, check_validity=True, raise_exception=True)
            partner_user = partner.user_ids and partner.user_ids[0] or False
            if partner_user:
                values['wk_dob'] = values.get('wk_dob')
                values['custom_field_1'] = values.get('custom_field_1')
                values['custom_field_2'] = values.get('custom_field_2')
        else:
            values['wk_dob'] = values.get('wk_dob')
            values['custom_field_1'] = values.get('custom_field_1')
            values['custom_field_2'] = values.get('custom_field_2')

        return super(ResUsers, self).signup(values, token)