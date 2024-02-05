# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'National ID Application',
    'version': '1.0',
    'depends': ['base', 'mail', 'purchase'],
    'author': "Mulumba Mathias Mucani",
    'category': 'National ID',
    'description': """
    National ID Application
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/application.xml',
        'views/approval.xml',

        # 'views/mymodule_view.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'license': 'LGPL-3',
}