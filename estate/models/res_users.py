from odoo import fields, models

class ResUsers(models.Model):
    _inherit = "res.users"
    
    property_ids = fields.One2many(
        'estate.property', #ilişki yapılmış model
        'salesperson_id', #foreign key
        string='Properties',
        domain=[('state', 'in', ['new', 'offer_received', 'offer_accepted'])]
    )
