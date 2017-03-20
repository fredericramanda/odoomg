# -*- coding: utf-8 -*-
##############################################################################
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

# import

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

import models
from openerp import SUPERUSER_ID

def _set_currency_to_mga(cr, registry):
    cr.execute("UPDATE res_currency SET active = True WHERE name = 'MGA'")
    currency_mga_ids = registry['res.currency'].search(cr, SUPERUSER_ID, [('name', '=', 'MGA')])
    if currency_mga_ids:
        my_company = registry['res.users'].browse(cr, SUPERUSER_ID, SUPERUSER_ID, {}).company_id
        my_company.write({'currency_id': currency_mga_ids[0]})

