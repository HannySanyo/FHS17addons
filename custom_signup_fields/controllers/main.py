from odoo import http
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request
import base64

class CustomSignup(AuthSignupHome):
    def do_signup(self, qcontext):
        super(CustomSignup, self).do_signup(qcontext)
        user = request.env['res.users'].sudo().search([('login', '=', qcontext.get('login'))], limit=1)

        if user:
            custom_file_1 = qcontext.get('custom_field_1')
            custom_file_2 = qcontext.get('custom_field_2')

            if custom_file_1:
                custom_file_1 = base64.b64encode(custom_file_1.read())
            else:
                custom_file_1 = None

            if custom_file_2:
                custom_file_2 = base64.b64encode(custom_file_2.read())
            else:
                custom_file_2 = None

            user.partner_id.sudo().write({
                'custom_field_1': custom_file_1,
                'custom_field_2': custom_file_2,
            })