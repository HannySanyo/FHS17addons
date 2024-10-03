#################################################################################
# File Name: main.py
# Revision History:  Engineer    Date          Description
#                    G. Sanyo    09/29/2024    Creation
#################################################################################
import logging

_logger = logging.getLogger(__name__)

class AuthSignupHomeInherit(AuthSignupHome):
    def do_signup(self, qcontext):
        """ Shared helper that creates a res.partner out of a token """
        values = {key: qcontext.get(key) for key in ('login', 'name', 'password', 'phone', 'contractor_doc', 'contractor_doc_name', 'tax_exemption_doc', 'tax_exemption_doc_name')}
        _logger.info("Signup values: %s", values)  # Log the values for debugging
        
        if not values:
            raise UserError(_("The form was not properly filled in."))
        
        if values.get('password') != qcontext.get('confirm_password'):
            raise UserError(_("Passwords do not match; please retype them."))

        if 'contractor_doc' in values and values['contractor_doc']:
            if hasattr(values['contractor_doc'], 'read'):
                contractor_filedata = base64.b64encode(values['contractor_doc'].read())
                contractor_filename = values.get('contractor_doc_name')
                values.update({'x_studio_contractor_doc': contractor_filedata, 'x_studio_contractor_doc_filename': contractor_filename})
            else:
                _logger.warning("contractor_doc is not a FileStorage object: %s", type(values['contractor_doc']))

        if 'tax_exemption_doc' in values and values['tax_exemption_doc']:
            if hasattr(values['tax_exemption_doc'], 'read'):
                fiscal_pos_filedata = base64.b64encode(values['tax_exemption_doc'].read())
                fiscal_pos_filename = values.get('tax_exemption_doc_name')
                values.update({'x_studio_tax_exemption_doc': fiscal_pos_filedata, 'x_studio_tax_exemption_doc_filename': fiscal_pos_filename})
            else:
                _logger.warning("tax_exemption_doc is not a FileStorage object: %s", type(values['tax_exemption_doc']))

        supported_lang_codes = [code for code, _ in request.env['res.lang'].get_installed()]
        lang = request.context.get('lang', '').split('_')[0]
        if lang in supported_lang_codes:
            values['lang'] = lang
        self._signup_with_values(qcontext.get('token'), values)
        request.env.cr.commit()

    def get_auth_signup_qcontext(self):
        SIGN_UP_REQUEST_PARAMS.update({'phone', 'contractor_doc', 'contractor_doc_name', 'tax_exemption_doc', 'tax_exemption_doc_name'})
        return super().get_auth_signup_qcontext()
