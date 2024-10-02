#################################################################################
# File Name: res_user.py
# Revision History:  Engineer    Date          Description
#                    G. Sanyo    09/29/2024    Creation
#################################################################################
from odoo import api, fields, models

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
		
		if token:
			partner = self.env['res.partner']._signup_retrieve_partner(token, check_validity=True, raise_exception=True)
			partner_user = partner.user_ids and partner.user_ids[0] or False
			if partner_user:
				values['phone'] = values.get('phone')
				# values[''] = values.get('attachment')
				partner_user.x_studio_contractor_doc = values.get('attachment')
				partner_user.x_studio_contractor_doc_filename = values.get('attachment_name')
		else:	
			values['phone'] = values.get('phone')
			values['attachment'] = values.get('attachment')
			values['attachment_name'] = values.get('attachment_name')
		return super(ResUsers, self).signup(values, token)
		