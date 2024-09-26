import base64
import logging
from odoo import _
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome

_logger = logging.getLogger(__name__)

class CustomSignup(AuthSignupHome):
    def do_signup(self, qcontext):
        # Call parent method to handle the default signup logic
        super(CustomSignup, self).do_signup(qcontext)

        # Fetch the user based on the login/email used in signup
        user = request.env['res.users'].sudo().search([('login', '=', qcontext.get('login'))], limit=1)

        if user:
            # Retrieve file inputs and encode them in base64 for Binary fields
            custom_file_1 = qcontext.get('custom_field_1')
            custom_file_2 = qcontext.get('custom_field_2')

            # Handle file upload (binary)
            if custom_file_1:
                custom_file_1 = base64.b64encode(custom_file_1.read())
            else:
                custom_file_1 = None  # Handle case where no file is uploaded

            if custom_file_2:
                custom_file_2 = base64.b64encode(custom_file_2.read())
            else:
                custom_file_2 = None  # Handle case where no file is uploaded

            # Update the user's partner with custom fields
            user.partner_id.sudo().write({
                'custom_field_1': custom_file_1,
                'custom_field_2': custom_file_2,
            })

            _logger.info("User %s signed up with custom fields.", user.login)

    def get_auth_signup_qcontext(self):
        # Update SIGN_UP_REQUEST_PARAMS to include custom fields
        SIGN_UP_REQUEST_PARAMS.update({'wk_dob', 'custom_field_1', 'custom_field_2'})
        return super(CustomSignup, self).get_auth_signup_qcontext()
