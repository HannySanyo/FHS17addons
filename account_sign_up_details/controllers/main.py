#################################################################################
# File Name: main.py
# Revision History:  Engineer    Date          Description
#                    G. Sanyo    09/29/2024    Creation
#################################################################################
import base64
from odoo import _
from odoo import http
from odoo.http import request,route
from odoo.exceptions import UserError
from odoo.addons.web.controllers.home import SIGN_UP_REQUEST_PARAMS
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
    
class AuthSignupHomeInherit(AuthSignupHome):
    def do_signup(self, qcontext):
        """ Shared helper that creates a res.partner out of a token """
        values = {key: qcontext.get(key) for key in ('login', 'name', 'password', 'phone', 'x_studio_contractor_doc','x_studio_contractor_doc_filename') }
        if not values:
            raise UserError(_("The form was not properly filled in."))
        if values.get('password') != qcontext.get('confirm_password'):
            raise UserError(_("Passwords do not match; please retype them."))
        if values.get('x_studio_contractor_doc'):
            datas = base64.b64encode(values.get('x_studio_contractor_doc').read())
            values.update({'x_studio_contractor_doc': datas, 'x_studio_contractor_doc_filename': values.get('x_studio_contractor_doc').filename})

        supported_lang_codes = [code for code, _ in request.env['res.lang'].get_installed()]
        lang = request.context.get('lang', '').split('_')[0]
        if lang in supported_lang_codes:
            values['lang'] = lang
        self._signup_with_values(qcontext.get('token'), values)
        request.env.cr.commit()

    def get_auth_signup_qcontext(self):
        SIGN_UP_REQUEST_PARAMS.update({'phone', 'x_studio_contractor_doc', 'x_studio_contractor_doc_filename'})
        return super().get_auth_signup_qcontext()
