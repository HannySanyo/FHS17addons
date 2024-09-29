#################################################################################
#
#################################################################################
from odoo import api, models, _
import logging

_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def signup(self, values, token=None):
        """ Signup a user, to either:
            - create a new user (no token), or
            - create a user for a partner (with token, but no user for partner), or
            - change the password of a user (with token, and existing user).
            :param values: a dictionary with field values that are written on user
            :param token: signup token (optional)
            :return: (dbname, login, password) for the signed up user
        """

        _logger.debug("Signup values: %s", values)  # Log the incoming values

        if token:
            partner = self.env['res.partner']._signup_retrieve_partner(token, check_validity=True, raise_exception=True)
            partner_user = partner.user_ids and partner.user_ids[0] or False
            if partner_user:
                # Directly use the phone number from values
                if 'phone' in values:
                    partner_user.phone = values['phone']
        else:
            if 'phone' in values:
                # Directly use the phone number from values
                values['phone'] = values['phone']  # This line can also be omitted

        return super(ResUsers, self).signup(values, token)
