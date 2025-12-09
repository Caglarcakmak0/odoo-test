from odoo import models, Command

class EstateProperty(models.Model):
    _inherit = "estate.property"
    
    def action_sold(self):
        # Call parent method first
        res = super().action_sold()
        
        # Create invoice for each sold property
        for record in self:
            # Create invoice (account.move)
            self.env['account.move'].create({
                'partner_id': record.buyer_id.id,
                'move_type': 'out_invoice',
                'invoice_line_ids': [
                    Command.create({
                        'name': f'Property: {record.name}',
                        'quantity': 1,
                        'price_unit': record.selling_price * 0.06,  # 6% commission
                    }),
                    Command.create({
                        'name': 'Administrative fees',
                        'quantity': 1,
                        'price_unit': 100.00,
                    }),
                ],
            })
        
        return res
