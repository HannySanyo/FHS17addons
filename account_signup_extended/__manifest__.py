# -*- coding: utf-8 -*-
#################################################################################
# Author      : Grace Sanyo
# Description : Extension of the auth_signup page for additional fields
# Rev History : Date          Author       Summary
#               09/26/2024    G. Sanyo     Extend auth_signup w/ phone # and attachment fields
#              
#################################################################################
{
  "name"                 :  "Account Sign-Up Extended",
  "summary"              :  """Add a mandatory field for users to share their phone number and allow for contract or tax exempt attachments during the sign up.""",
  "category"             :  "Custom fields",
  "version"              :  "1.0.0",
  "author"               :  "Grace Sanyo",
  "description"          :  """Add phone number and attachment fields to account sign up""",
  "depends"              :  ['auth_signup'],
  "data"                 :  [
                             'views/auth_signup_template.xml',
                            ],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "pre_init_hook"        :  "pre_init_check",
  
  # May want to add a valid phone number format check here using javascript, but for rn, not needed.
  # 'assets':{
  # 'web.assets_frontend':[
    
  #   'account_signup_extended/static/src/js/validate.js',
    
  #   ],
  # },
}
