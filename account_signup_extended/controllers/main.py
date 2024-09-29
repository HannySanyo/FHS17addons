#################################################################################
#
#################################################################################
import logging
from odoo import _
from odoo.http import request
from odoo.exceptions import UserError
#from odoo.addons.web.controllers.home import SIGN_UP_REQUEST_PARAMS, Home
from odoo.addons.auth_signup.controllers.main import AuthSignupHome

_logger = logging.getLogger(__name__)

class AuthSignupHomeInherited(AuthSignupHome):

    def get_auth_signup_qcontext(self):
        print(request.params)
        qcontext = super(AuthSignupHomeInherited, self).get_auth_signup_qcontext()
        qcontext.update({k: v for (k, v) in request.params.items() if k in ['phone']})
        return qcontext

    def _prepare_signup_values(self, qcontext):
        values = super(AuthSignupHomeInherited, self)._prepare_signup_values(qcontext)
        values.update({ key: qcontext.get(key) for key in ('phone')})
        return values
