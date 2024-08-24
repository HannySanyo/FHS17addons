# -*- coding: utf-8 -*-
{
    'name': "sale_order",

    'summary': """
        edit create date in sales orders""",

    'description': """
        edit create date in sales orders
    """,

    'author': "Hanny",
    'website': "www.federalheatingsupply.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'views/sale_order.xml',
    ],

    'installable': "True",
    'auto_install': "False",
    'application': "True",
}