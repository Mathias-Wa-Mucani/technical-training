# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP

class PurchaseOrderVendorLine(models.Model):
    _name = 'purchase.order.vendor.line'
    _description = 'Purchase Order Vendor Line'
    
    READONLY_STATES = {
        'purchase': [('readonly', True)],
        'done': [('readonly', True)],
        'cancel': [('readonly', True)],
    }
    purchase_order_id = fields.Many2one('purchase.order', string='Purchase Order')
    partner_id = fields.Many2one('res.partner', string='Vendor')
    # Add other fields as needed

class PurchaseExtended(models.Model):
    _inherit = "purchase.order"
    # order_id = fields.Many2one('purchase.order', string='Order Reference', index=True, required=True, ondelete='cascade')
    READONLY_STATES = {
        'purchase': [('readonly', True)],
        'done': [('readonly', True)],
        'cancel': [('readonly', True)],
    }
     
    partner_id = fields.Many2one(required=False)
    # partner_id = fields.One2many('purchase.order.vendor.line', 'purchase_order_id', string='Vendor Lines')
    partner_ids = fields.Many2many('res.partner', string='Vendor')#, states=READONLY_STATES, required=True, change_default=True, tracking=True, domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", help="You can find a vendor by its Name, TIN, Email or Internal Reference."
    purchase_description = fields.Char("Purchase Description")
    
    @api.depends('partner_ids')
    def _compute_partner_ids(self):
        # Compute the partner_ids based on the selected_partners
        self.partner_ids = self.partner_ids

    @api.onchange('partner_ids')
    def _onchange_selected_partners(self):
        # When the selected_partners change, trigger the computation of partner_ids
        self._compute_partner_ids()

    @api.onchange('partner_ids')
    def _onchange_partner_ids(self):
        # When the partner_ids change, update the selected_partners
        self.partner_ids = [(6, 0, self.partner_ids.ids)]

    def button_confirm(self):
        # Your custom logic before confirming the purchase order
        # ...

       # Call the original button_confirm method
        result = super(PurchaseExtended, self).button_confirm()

        # Send RFQ emails to vendors
        self.send_custom_rfq_emails()

        # Your custom logic after confirming the purchase order
        # ...

        return result

    def send_custom_rfq_emails(self):
        # Use Odoo's email sending functionality to send emails
        # self.ensure_one()
        # ir_model_data = self.env['ir.model.data']
        # try:
        #     if self.env.context.get('send_rfq', False):
        #         template_id = ir_model_data._xmlid_lookup('purchase.email_template_edi_purchase')[2]
        #     else:
        #         template_id = ir_model_data._xmlid_lookup('purchase.email_template_edi_purchase_done')[2]
        # except ValueError:
        #     template_id = False
        # try:
        #     compose_form_id = ir_model_data._xmlid_lookup('mail.email_compose_message_wizard_form')[2]
        # except ValueError:
        #     compose_form_id = False
        # ctx = dict(self.env.context or {})
        # ctx.update({
        #     'default_model': 'purchase.order',
        #     'active_model': 'purchase.order',
        #     'active_id': self.ids[0],
        #     'default_res_id': self.ids[0],
        #     'default_use_template': bool(template_id),
        #     'default_template_id': template_id,
        #     'default_composition_mode': 'comment',
        #     'default_email_layout_xmlid': "mail.mail_notification_layout_with_responsible_signature",
        #     'force_email': True,
        #     'mark_rfq_as_sent': True,
        # })
        # mail_template = self.env['mail.template'].browse(ctx['default_template_id'])
        # if mail_template:
            # # Create a new mail composition
            # mail_composer = self.env['mail.compose.message'].create({
            #     'model': 'purchase.order',
            #     'composition_mode': 'comment',
            #     'template_id': mail_template.id,
            #     'res_id': self.id,
            #     'email_to': ', '.join(email_addresses),
            # })

            # # Send the email
            # mail_composer.send_mail()
            # Use Odoo's mail.compose.message to send emails
            for vendor in self.partner_ids:
                # Customize email content as needed
                subject = "RFQ for your consideration"
                body = f"Dear {vendor.name},\n\nWe are sending you a Request for Quotation (RFQ) for your consideration.\n\nThank you."

                # Use Odoo's mail.compose.message to send the email
                mail_values = {
                    'subject': subject,
                    'body_html': body,
                    'email_to': vendor.email or False,
                    'model': 'purchase.order',
                    'res_id': self.id,
                    'author_id': self.env.user.partner_id.id,
                }

                self.env['mail.compose.message'].create(mail_values).send()

                # Optionally, you can add additional logic after sending all emails
