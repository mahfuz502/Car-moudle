# -*- coding: utf-8 -*-
{
    'name': 'Car',
    'summary': """Something about the App.""",
    'description': """
App Name
========
Something about the App.
    """,
    'version': '13.0.1.0',
    'author': 'Mahfuz Rahman',
    'website': 'http://www.company.com',
    'category': 'Tools',
    'sequence': 1,
    'depends': [
        'mail',
        'contacts',
        'base',
        'web',
    ],
    'data': [
        # Data
        'data/car_template_mail.xml',

        # Security
        "security/ir.model.access.csv",

        # Report

        
        # Wizard
        "wizard/car_wizard.xml",

        
        # View
        # "views/rules.xml",
        "views/security.xml",
        "views/res_partner_inherit_form_view.xml",
        "views/sequence.xml",
        "views/parking.xml",
        "views/car.xml",
        "views/menus.xml",
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 0,
    'currency': 'EUR',
    'license': 'OPL-1',
    'contributors': [
        'Jeshad Khan <https://github.com/jeshadkhan>',
    ],
}
