# -*- coding: utf-8 -*-
##############################################################################
#
#    Module written to odoo for tax definitions
#
##############################################################################
{
    'name': 'Madagascar - PCG et définition des TVA',
    'version': '1.0',
    'category': 'Localization',
    'description': 'Plan comptable général complet et définition et paramétrage des taxes',
    'depends': ['account', 'l10n_mg',],
    'data': [
        'data/l10n_mg_chart_data.xml',
		'data/account_chart_template_data.xml',
		'data/account_tax_template_data.xml',
        'data/account_fiscal_position_template_data.xml',
        'data/account_chart_template_data.yml',
    ],
    'demo_xml': [],
    'auto_install': False,
    'installable': True,
    'website': 'https://github.com/redykely/odoomg',
}

