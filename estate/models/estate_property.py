from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"
    
    # SQL Constraints
    _sql_constraints = [
        ('check_expected_price_positive', 
         'CHECK(expected_price > 0)', 
         'Expected price must be strictly positive!'),
        ('check_selling_price_positive', 
         'CHECK(selling_price >= 0)', 
         'Selling price must be positive!'),
    ]
    
    _order = "id desc"

    # Temel Bilgiler
    name = fields.Char(string='Başlık', required=True)
    description = fields.Text(string='Açıklama')
    postcode = fields.Char(string='Posta Kodu')
    date_availability = fields.Date(string='Müsaitlik Tarihi', copy=False, default=fields.Date.today)
    
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')

    # Fiyatlandırma
    expected_price = fields.Float(string='Beklenen Fiyat', required=True)
    selling_price = fields.Float(string='Satış Fiyatı', readonly=True, copy=False)
    
    # Mülk Detayları
    bedrooms = fields.Integer(string='Yatak Odası Sayısı', default=2)
    living_area = fields.Integer(string='Yaşam Alanı (metrekare)')
    facades = fields.Integer(string='Cephe Sayısı')
    toilets = fields.Selection(
        string='Banyo Sayısı',
        selection=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
        ],
        default='1',
        required=True
    )
    
    garage = fields.Boolean(string='Garaj')
    garden = fields.Boolean(string='Bahçe')
    garden_area = fields.Integer(string='Bahçe Alanı (metrekare)')
    garden_orientation = fields.Selection(
        string='Bahçe Yönü',
        selection=[('north', 'Kuzey'), ('south', 'Güney'), ('east', 'Doğu'), ('west', 'Batı')]
    )
    
    property_type_id = fields.Many2one('estate.property.type', string='Mülk Tipi')
    
    # Satış Bilgileri
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    salesperson_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    total_area = fields.Float(string="Toplam Alan (metrekare)", compute='_compute_total_area')
    
    # State
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled'),
    ], string='Status', default='new', required=True, copy=False)

    # Computed Fields
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for x in self:
            x.total_area = x.living_area + x.garden_area
    
    # Action Methods
    def action_sold(self):
        for record in self:
            if record.state == 'canceled':
                raise UserError("Canceled properties cannot be sold!")
            record.state = 'sold'
        return True
    
    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("Sold properties cannot be canceled!")
            record.state = 'canceled'
        return True
    
    # Python Constraints
    @api.constrains('selling_price', 'expected_price')
    def _check_selling_price(self):
        for record in self:
            if record.selling_price > 0 and record.selling_price < record.expected_price * 0.9:
                raise ValidationError("Selling price cannot be lower than 90% of expected price!")
    
    @api.ondelete(at_uninstall=False)
    def _check_offer_state_before_delete(self):
        for record in self:
            if record.state not in ('new', 'canceled'):
                raise UserError("Only new and cancelled properties can be deleted!")
