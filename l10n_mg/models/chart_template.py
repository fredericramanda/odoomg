# -*- coding: utf-8 -*-

from openerp import fields, models


class AccountChartTemplate(models.Model):
    _name = 'account.chart.template'
    _inherit = 'account.chart.template'
    _description = 'Templates for Account Chart'

    code_digits = fields.Integer(default=lambda self: self.env.user.company_id.accounts_code_digits or 6)




