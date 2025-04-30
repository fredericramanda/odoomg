# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    nif = fields.Char(related='partner_id.nif', string='NIF', size=20, readonly=False)
    num_stat = fields.Char(related='partner_id.num_stat', string='STAT', size=20, readonly=False)
