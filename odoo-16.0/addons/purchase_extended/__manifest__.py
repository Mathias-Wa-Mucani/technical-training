# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Purchase Extended',
    'version': '1.0',
    'depends': ['base', 'mail', 'purchase', 'sale'],
    'author': "Mulumba Mathias Mucani",
    'category': 'Purchase Extended',
    'description': """
    Purchase Module Extended for further functionalities
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/property.xml',
        'views/purchase.xml',

        # 'views/mymodule_view.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'license': 'LGPL-3',
}