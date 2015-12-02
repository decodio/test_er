# -*- encoding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    This module copyright (C) 2015 Slobodni-programi d.o.o.#    #
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

from openerp import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.one
    @api.depends('reseller_order_ids.partner_id')
    def _resseller_order_count(self):
        try:
            self.reseller_order_count = len(self.reseller_order_ids)
        except:
            self.reseller_order_count = 0

    reseller_order_ids = fields.One2many(
        'reseller.order', 'partner_id', string='Reseller Orders')
    reseller_order_count = fields.Integer(
        compute='_resseller_order_count', string="Reseller Orders", readonly=True)
