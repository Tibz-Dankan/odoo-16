# rfq_operations/models/rfq_operations.py

from odoo import fields, models

class RFQOperations(models.Model):
    _inherit = 'purchase.order'
#
    vendor_ids = fields.One2many('rfq.assigned', 'rfq_assigned_id', string='Vendors')



class RFQAssigned(models.Model):
    _name ="rfq.assigned"
    _description = "RFQ Assign To Vendors"

    rfq_assigned_id = fields.Many2one('purchase.order', string='RFQ Assigned')
    vendor_name = fields.Char(string='Vendor')

