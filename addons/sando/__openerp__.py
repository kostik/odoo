# -*- coding: utf-8 -*-
{
    'name': "Suspects and Offenders module",

    'summary': """
        Myanmar Customs Department RM & Intelligence unit""",

    'description': """
        STRENGTHENING INSTITUTIONAL KNOWLEDGE AND CAPACITY OF CUSTOMS ADMINISTRATIONS FOR TRADE FACILITATION WITHIN ASEAN: MYANMAR

        Assistance to the Myanmar Customs Department with the Development of a Myanmar Customs Department Information System (MCDIS)
    """,

    'author': "Kostik Naumov",
    'website': "http://www.kostik.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'MCD',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/sequences.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}