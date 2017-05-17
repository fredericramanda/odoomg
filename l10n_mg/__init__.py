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
    cr.execute("UPDATE res_company SET currency_id = (select id from res_currency where name = 'MGA')");

