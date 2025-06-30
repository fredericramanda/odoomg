from odoo import models, Command
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'

    @template('mg')
    def _get_mg_template_data(self):
        return {
            'code_digits': 6,
            'property_account_receivable_id': 'mg_pcg_recv',
            'property_account_payable_id': 'mg_pcg_pay',
            'property_account_expense_categ_id': 'pcg_607',
            'property_account_income_categ_id': 'pcg_707',
        }

    @template('mg', 'res.company')
    def _get_mg_res_company(self):
        return {
            self.env.company.id: {
                'account_fiscal_country_id': 'base.mg',
                'bank_account_code_prefix': '512',
                'cash_account_code_prefix': '53',
                'transfer_account_code_prefix': '58',
                'account_default_pos_receivable_account_id': 'mg_pcg_recv_pos',
                'income_currency_exchange_account_id': 'pcg_766',
                'expense_currency_exchange_account_id': 'pcg_666',
                'account_journal_early_pay_discount_loss_account_id': 'pcg_665',
                'account_journal_early_pay_discount_gain_account_id': 'pcg_766',
                'account_sale_tax_id': 'tva_normale',
                'account_purchase_tax_id': 'tva_acq_normale',
            },
        }

    @template('mg', 'account.journal')
    def _get_mg_account_journal(self):
        return {
            'sale': {'refund_sequence': True},
            'purchase': {'refund_sequence': True},
        }

    @template('mg', 'account.reconcile.model')
    def _get_mg_reconcile_model(self):
        return {
            'bank_charges_reconcile_model': {
                'name': 'Bank fees',
                'line_ids': [
                    Command.create({
                        'account_id': 'pcg_6278',
                        'amount_type': 'percentage',
                        'amount_string': '100',
                    }),
                ],
            },
        }
