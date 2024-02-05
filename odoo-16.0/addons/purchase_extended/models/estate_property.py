# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP



class EstateProperty(models.Model):
    _name = "estate.property"
    # _inherit = "purchase.order"
    _description = "Estate Property"
    _order = "sequence"
    
    # partner_id = fields.Many2one('res.partner', string='Vendor', required=True, change_default=True, tracking=True, domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", help="You can find a vendor by its Name, TIN, Email or Internal Reference.")

    name = fields.Char('Property Name', required=True)
    description = fields.Text('Description')
    parent_id = fields.Many2one('res.partner', string='Parent Company', index=True, ondelete='cascade')
    # child_ids = fields.One2many('res.partner', 'parent_id', string='Subsidiaries')

    company_id = fields.One2many('res.partner', 'parent_id', string='Vendor',  copy=True)#readonly=False, store=True, states={'cancel': [('readonly', True)], 'done': [('readonly', True)]},

    # postcode = fields.Char('Postcode')
    # date_availability = fields.Date('Availability Date')
    # expected_price = fields.Float('Expected Price', required=True)
    # selling_price = fields.Float('Selling Price')
    # bedrooms = fields.Integer('Bedrooms')
    # living_area = fields.Integer('Living Area')
    # facades = fields.Integer('Facades')
    # garage = fields.Boolean('Garage')
    # garden = fields.Boolean('Garden')
    # garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('east', 'East'), ('south', 'South'), ('west', 'West')  ], help = "Please select a choice here")
    is_active = fields.Boolean('Is Active', default=True)
    sequence = fields.Integer('Sequence', default=10)

    _sql_constraints = [
        # ('check_number_of_months', 'CHECK(number_of_months >= 0)', 'The number of month can\'t be negative.'),
    ]