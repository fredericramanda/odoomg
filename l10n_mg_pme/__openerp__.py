# -*- coding: utf-8 -*-
##############################################################################
#
#    Module written to odoo for Malagasy Accounting Simplified
#
##############################################################################
{   'name': 'Madagascar - Plan Comptable Général',
    'version': '1.0',
    'category': 'Localization',
    'author': 'Frédéric Harison RAMANDANIARIVO',
    'depends': ['account','l10n_mg',],
    'data': [
        'data/l10n_mg_chart_data.xml',
        'data/account_chart_template_data.xml',
        'data/account_chart_template_data.yml',
    ],
    'demo_xml': [],
    'auto_install': False,
    'installable': True,
    'website': 'https://github.com/redykely/odoo_mg',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
