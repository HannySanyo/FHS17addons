# -*- coding: utf-8 -*-
{
    'name': "sale_order",

    'summary': """
        Edit create date in sales orders""",

    'description': """
        This module allows editing the create date in sales orders by making the 'create_date' field editable.
    """,

    'author': "Hanny",
    'website': "www.federalheatingsupply.com",

    'category': 'Tools',
    'version': '0.1',

    'depends': ['base', 'sale'],

    'data': [
        'views/sale_order.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
