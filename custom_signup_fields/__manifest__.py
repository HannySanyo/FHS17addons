{
  "name"                 :  "Website Signup Extension",
  "summary"              :  "Add custom fields to the website sign-up form",
  "category"             :  "Website",
  "version"              :  "1.1",
  "depends"              :  ['auth_signup'],
  "data"                 :  [
                             'views/res_partner_view.xml',
                             'views/account_details_template.xml',
                            ],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "pre_init_hook"        :  "pre_init_check",
}
