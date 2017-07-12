# -*- coding: utf-8 -*-
{
    'name': "l10n_mg_partner",

    'summary': """
        Extend partner informations""",

    'description': """
        Add VAT and another fiscal information on partner
    """,

    'author': "Frédéric Harison RAMANDANIARIVO",
    'website': "https://github.com/redykely/odoo_mg",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_views.xml',
    ],
    'demo': [],
    'auto_install': False,
    'installable': True,
}
