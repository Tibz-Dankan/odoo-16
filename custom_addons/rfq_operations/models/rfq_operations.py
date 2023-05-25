# rfq_operations/models/rfq_operations.py

from odoo import fields, models

class RFQOperations(models.Model):
    _inherit = 'purchase.order'

    vendor_ids = fields.One2many('res.partner', 'rfq_id', string='Vendors')



class ResPartner(models.Model):
    _inherit = 'res.partner'

    rfq_id = fields.Many2one('rfq.operations', string='RFQ Operations')
