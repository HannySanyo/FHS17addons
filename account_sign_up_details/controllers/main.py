#################################################################################
# File Name: main.py
# Revision History:  Engineer    Date          Description
#                    G. Sanyo    09/29/2024    Creation
#################################################################################
import base64
import logging
from odoo import _
from odoo.http import request,route
from odoo.exceptions import UserError
from odoo.addons.web.controllers.home import SIGN_UP_REQUEST_PARAMS, Home
from odoo.addons.auth_signup.controllers.main import AuthSignupHome

_logger = logging.getLogger(__name__)


class AuthSignupHome(Home):
    def do_signup(self, qcontext):
        """ Shared helper that creates a res.partner out of a token """
        values = {key: qcontext.get(key) for key in ('login', 'name', 'password', 'phone') }
        if not values:
            raise UserError(_("The form was not properly filled in."))
        if values.get('password') != qcontext.get('confirm_password'):
            raise UserError(_("Passwords do not match; please retype them."))
        supported_lang_codes = [code for code, _ in request.env['res.lang'].get_installed()]
        lang = request.context.get('lang', '').split('_')[0]
        if lang in supported_lang_codes:
            values['lang'] = lang
        self._signup_with_values(qcontext.get('token'), values)
        request.env.cr.commit()
    
class AuthSighup(AuthSignupHome):

    def get_auth_signup_qcontext(self):
        SIGN_UP_REQUEST_PARAMS.update({'phone'})
        return super().get_auth_signup_qcontext()

    def _signup_with_values(self, token, values):
        context = self.get_auth_signup_qcontext()
        attachment_contractor = context.get('attachment_contractor')
        if attachment_contractor:
            datas = base64.b64encode(attachment_contractor.read())
            values.update({'attachment_contractor': datas, 'attachment_contractor_name': attachment_contractor.filename})

        attachment_taxexempt = context.get('attachment_taxexempt')
        if attachment_taxexempt:
            datas = base64.b64encode(attachment_taxexempt.read())
            values.update({'attachment_taxexempt': datas, 'attachment_taxexempt_name': attachment_taxexempt.filename})
        super(AuthSignupStreet, self)._signup_with_values(token, values)