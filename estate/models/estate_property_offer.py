from odoo import models, fields, api
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    
    # SQL Constraints
    _sql_constraints = [
        ('check_offer_price_positive', 
         'CHECK(price > 0)', 
         'Offer price must be strictly positive!'),
    ]
    
    price = fields.Float(string='Price', required=True)
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ], string='Status', copy=False)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('estate.property', string='Property', required=True)
    validity = fields.Integer(string='Validity (days)', default=7)
    date_deadline = fields.Date(string='Deadline')

    def action_accept(self):
        for record in self:
            # Sadece bir offer kabul edilebilir
            if record.property_id.offer_ids.filtered(lambda o: o.status == 'accepted'):
                raise UserError("An offer is already accepted for this property!")
            
            # Offer'ı kabul et
            record.status = 'accepted'
            
            # Property'yi güncelle
            record.property_id.buyer_id = record.partner_id
            record.property_id.selling_price = record.price
            record.property_id.state = 'offer_accepted'
        
        return True

    def action_refuse(self):
        for record in self:
            record.status = 'refused'
        return True

    @api.model
    def create(self, vals):
        # 1. Property'yi al
        property_obj = self.env['estate.property'].browse(vals['property_id'])
    
        # 2. Property state'ini güncelle
        property_obj.state = 'offer_received'
    
        # 3. Mevcut offer'ları kontrol et
        if property_obj.offer_ids:
            max_offer = max(property_obj.offer_ids.mapped('price'))
            if vals['price'] < max_offer:
                raise UserError("Offer price cannot be lower than existing offers!")
    
        # 4. Parent create
        return super().create(vals)