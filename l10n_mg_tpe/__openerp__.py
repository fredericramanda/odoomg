# -*- coding: utf-8 -*-
##############################################################################
#
#    Module written to odoo for Malagasy Accounting Simplified
#
##############################################################################
{
    'name': 'Madagascar - Simplified accounting for very small businesses',
    'version': '1.0',
    'category': 'Localization',
    'description': 'Accounting Chart for MG TPE',
    'depends': ['account',],
    'data': [
        'data/l10n_mg_tpe_chart_data.xml',
        'data/account_chart_template_data.xml',
        'data/account_chart_template_data.yml',
    ],
    'demo_xml': [],
    'auto_install': False,
    'installable': True,
    'website': 'https://github.com/redykely/odoomg',
}

