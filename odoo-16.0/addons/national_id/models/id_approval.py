# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP



class IdApproval(models.Model):
    _name = "id.approval"
    _rec_name = 'application_id'
    _inherit = ['mail.thread']
    _description = "National ID Approval"
    # _order = "sequence"
    
    application_id = fields.Many2one('id.application', string="National ID Application")
    stage1_approved_by = fields.Many2one('res.users', string="Stage1 Approver")
    stage1_approved_at = fields.Date('Stage1 Approval Date', required=True)
    stage2_approved_by = fields.Many2one('res.users', string="Stage2 Approver")
    stage2_approved_at = fields.Date('Stage2 Approval Date')
    


    _sql_constraints = [
        # ('check_number_of_months', 'CHECK(number_of_months >= 0)', 'The number of month can\'t be negative.'),
    ]
    
    