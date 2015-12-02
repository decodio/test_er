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


class ResellerOrder(models.Model):
    """Reseller Order management"""
    _name = 'reseller.order'

    name = fields.Char('Order number',
                       default='/',
                       readonly=True,
                       required=True
                       )
    partner_id = fields.Many2one(
            comodel_name='res.partner',
            string='Customer',
    )
    product_id = fields.Many2one(
            comodel_name='product.product',
            string='Package',
    )
    order_date = fields.Date(string='Order date')
    canceled_date = fields.Date(string='Canceled date')
    state = fields.Selection(
            selection=[('draft', 'Draft'),
                       ('confirmed', 'Confirmed'),
                       ('active', 'Active'),
                       ('canceled', 'Canceled')],
            default='draft'
    )

    @api.model
    def create(self, vals=None):
        """ Automatic Order number using sequence"""
        if vals.get('name', '/') == '/':
            vals['name'] = self.env['ir.sequence'].next_by_code('reseller.order')
        res = super(ResellerOrder, self).create(vals)
        return res
