# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    nif = fields.Char(string='NIF', size=20)
    num_stat = fields.Char(string='N STAT', size=20)
