# -*- coding: utf-8 -*-

from openerp import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    ref1 = fields.Char(string='Ref/Code 1', index=True)
    ref2 = fields.Char(string='Ref/Code 2', index=True)
    nif = fields.Char(string='NIF', index=True)
    nstat = fields.Char(string='Num STAT', index=True)

    # historisable dans une future version
    cif = fields.Char(string='Num CIF', index=True)
    dcif = fields.Date(string='Date CIF')

    # registre de commerce
    rcs = fields.Char(string='Imm. RCS', index=True)
    drcs = fields.Date(string='Date RCS')

    # scan signature
    signature_img = fields.Binary('Signature scannee')
