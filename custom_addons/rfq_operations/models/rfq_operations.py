# rfq_operations/models/rfq_operations.py

from odoo import fields, models

class RFQOperations(models.Model):
    _inherit = 'res.partner'

    # rfq_assigned = fields.Many2many("purchase.order", "VendorsAssigned")
    # vendor_ids = fields.One2many('res.partner', 'rfq_assigned_id', string='Vendors')



class RFQAssigned(models.Model):
    _inherit = 'purchase.order'

    vendor_ids = fields.Many2many("res.partner.category", "purchase_order_tag_rel", "purchase_id", "tag_id", "Vendors")
