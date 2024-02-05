# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP



class IdApplication(models.Model):
    _name = "id.application"
    # _rec_name='first_name'
    # _inherit = "purchase.order"
    _description = "National ID Application"
    # _order = "sequence"
    
    first_name = fields.Char('First Name', required=True)
    last_name = fields.Char('Last Name', required=True)
    date_of_birth = fields.Date('Date of Birth', required=True)
    telephone = fields.Integer('Telephone Number', required=True)
    district = fields.Char('District', required=True)
    county = fields.Char('County', required=True)
    subcounty = fields.Char('Sub County', required=True)
    parish = fields.Char('Parish', required=True)
    village = fields.Char('Village ', required=True)
    profile_picture = fields.Binary('Profile picture' )
    lc_reference_letter = fields.Binary('LC reference letter' )
    is_active = fields.Boolean('Is Active', default=True)


    # description = fields.Text('Description')
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
    # garden_orientation = fields.Selection(
    #     selection=[('north', 'North'), ('east', 'East'), ('south', 'South'), ('west', 'West')  ], help = "Please select a choice here")
    # sequence = fields.Integer('Sequence', default=10)

    _sql_constraints = [
        # ('check_number_of_months', 'CHECK(number_of_months >= 0)', 'The number of month can\'t be negative.'),
    ]
    
    # @api
    def name_get(self):
        return [(record.id, f"{record.first_name} {record.last_name} - {record.village}") for record in self]