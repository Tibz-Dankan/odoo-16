# rfq_operations/models/rfq_operations.py

from odoo import fields, models

class RFQOperations(models.Model):
    _inherit = 'res.partner'

    # rfq_assigned = fields.One2many("purchase.order", "vendor_ids", "RFQAssigned")
    # vendor_ids = fields.One2many('res.partner', 'rfq_assigned_id', string='Vendors')



class RFQAssigned(models.Model):
    _inherit = 'purchase.order'

    vendor_ids = fields.Many2many("res.partner", "purchase_order_tag_rel", "purchase_id", "tag_id", "Vendors")