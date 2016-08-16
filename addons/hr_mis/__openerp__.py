# -*- coding: utf-8 -*-
{
    'name': "hr_mis",

    'summary': """HRMIS module for TA-8709 REG""",

    'description': """HRMIS module for TA-8709 REG: Strengthening Institutional Knowledge and Capacity of Customs Administrations
        for Trade Facilitation within the Association of Southeast Asian Nations -
        International ICT Specialist for Myanmar Human Resource Management Information System (HRMIS) (46192-001)""",

    'author': "kostik@kostik.net",
    'website': "http://hrmis.kostik.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
