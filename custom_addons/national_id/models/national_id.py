# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api

class NationalId(models.Model):
     _name = "national.id"
     _description = "National Id Application records"

     surname = fields.Char(string="Surname", required=True)
     lastname = fields.Char(string="Lastname", required=True)
     gender = fields.Selection([("male", "Male"), ("female", "Female"), ("others", "Others")], string="Gender")
     age = fields.Integer(string="Age", required=True)
     district = fields.Char(string="District", required=True)
     sub_county = fields.Char(string="Sub_county", required=True)
     parish = fields.Char(string="Parish", required=True)
     village = fields.Char(string="Village", required=True)
     stage = fields.Selection([("draft", "Application"), ("review", "Review"), ("approved", "Approved")],
                                 string="Stage", default="draft")
     progress = fields.Float(string="Progress", compute="_compute_progress", store=True)
     chatter_log = fields.Text(string="Chatter Log", readonly=True)

     @api.depends('stage')
     def _compute_progress(self):
        for record in self:
                if record.stage == 'draft':
                    record.progress = 0.0
                elif record.stage == 'review':
                    record.progress = 50.0
                elif record.stage == 'approved':
                    record.progress = 100.0

     def write(self, vals):
        result = super(NationalId, self).write(vals)
        for record in self:
            # Check if any fields other than chatter_log have changed
            if any(field_name in vals for field_name in record._fields) and 'chatter_log' not in vals:
                log_message = f"Changes made by {self.env.user.name}: {fields.Datetime.now()}\n"
                if record.chatter_log:
                    log_message = record.chatter_log + log_message
                record.chatter_log = log_message
        return result

     def action_review(self):
         self.write({'stage': 'review'})

     def action_approve(self):
         self.write({'stage': 'approved'})