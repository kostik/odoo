# -*- coding: utf-8 -*-
{
    'name': "AEO",

    'summary': """
        MCDIS AEO module
        """,

    'description': """
        STRENGTHENING INSTITUTIONAL KNOWLEDGE AND CAPACITY OF CUSTOMS ADMINISTRATIONS FOR TRADE FACILITATION WITHIN ASEAN: MYANMAR

        Assistance to the Myanmar Customs Department with the Development of a Myanmar Customs Department Information System (MCDIS)
    """,

    'author': "Kostik kostik@kostik.net",
    'website': "http://www.kostik.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'AEO',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/aeo_security.xml',
        'views/views.xml',
        'views/templates.xml',
        'res_partner_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}