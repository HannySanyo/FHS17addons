from odoo import api, fields, models, _

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def signup(self, values, token=None):
        """ signup a user, to either:
            - create a new user (no token), or
            - create a user for a partner (with token, but no user for partner), or
            - change the password of a user (with token, and existing user).
            :param values: a dictionary with field values that are written on user
            :param token: signup token (optional)
            :return: (dbname, login, password) for the signed up user
        """
        # Capture 'wk_dob', 'custom_field_1', and 'custom_field_2' during signup
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
