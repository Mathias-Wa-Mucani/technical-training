# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Estate',
    'version': '1.0',
    'depends': ['base', 'mail'],
    'author': "Mulumba Mathias Mucani",
    'category': 'Esates',
    'description': """
    Real Estates Management App
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/property.xml',

        # 'views/mymodule_view.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'license': 'LGPL-3',
}