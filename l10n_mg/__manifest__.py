# -*- coding: utf-8 -*-
##############################################################################
#
#    Module written to odoo for tax definitions
#
##############################################################################
{
    'name': 'Madagascar - PCG et définition des TVA',
    'version': '1.0',
    'category': 'Accounting/Localizations/Account Charts',
    'description': 'Plan comptable général complet et définition et paramétrage des taxes',
    'icon': '/account/static/description/l10n.png',
    'countries': ['mg'],
    'depends': [
        'base',
        'base_iban',
        'base_vat',
        'account',
        ],
    'data': [
        'views/l10n_mg_view.xml',
    ],
    'demo_xml': [],
    'auto_install': False,
    'installable': True,
    'website': 'https://github.com/fredericramanda/odoomg',
    'license': 'LGPL-3',
}

