# 🏠 Real Estate Modülü Geliştirme Rehberi

## 🎯 Hedef
Odoo'da profesyonel bir **Emlak Yönetim Modülü** geliştirmek

---

## 📋 Real Estate Modülünde Olması Gerekenler

### Temel Özellikler
- 🏘️ **Mülk Yönetimi** (Properties)
  - Satılık/Kiralık mülkler
  - Mülk detayları (m², oda sayısı, fiyat, vb.)
  - Fotoğraflar ve dökümanlar
  
- 👥 **Müşteri Yönetimi**
  - Alıcılar ve satıcılar
  - İletişim bilgileri
  - Müşteri talepleri

- 💼 **Teklif ve Satış Süreci**
  - Müşteri teklifleri
  - Fiyat pazarlığı
  - Sözleşme yönetimi

- 📊 **Raporlama**
  - Satış raporları
  - Mülk durumu
  - Gelir analizi

### İleri Seviye Özellikler
- 📅 **Randevu Sistemi** - Mülk gezileri
- 📧 **Email Entegrasyonu** - Otomatik bildirimler
- 🗺️ **Harita Entegrasyonu** - Mülk konumları
- 💰 **Komisyon Hesaplama** - Satış komisyonları

---

## 🚀 Hızlı Öğrenme Yolu (Real Estate Odaklı)

### Faz 1: Temel Kavramlar (1-2 Gün)

#### ✅ Öğrenmeniz Gerekenler

**1. Odoo Model Yapısı**
```python
from odoo import models, fields, api

class RealEstateProperty(models.Model):
    _name = 'real.estate.property'
    _description = 'Real Estate Property'
    
    # Temel alanlar
    name = fields.Char(string='Property Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price')
    area = fields.Float(string='Area (m²)')
    bedrooms = fields.Integer(string='Bedrooms')
    bathrooms = fields.Integer(string='Bathrooms')
    
    # İlişkisel alanlar
    property_type_id = fields.Many2one('real.estate.property.type', string='Property Type')
    seller_id = fields.Many2one('res.partner', string='Seller')
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    
    # Durum alanı
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], default='new', string='Status')
```

**2. View Tipleri**
- **Tree View**: Liste görünümü (mülk listesi)
- **Form View**: Detay görünümü (mülk detayları)
- **Kanban View**: Kart görünümü (görsel mülk kartları)
- **Search View**: Filtreleme ve arama

**3. Actions ve Menus**
- Modülünüzü menüye nasıl eklersiniz
- Butonlar ve aksiyonlar

---

### Faz 2: Real Estate Modülü Geliştirme (3-5 Gün)

#### Modül Yapısı

```
real_estate/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── property.py              # Mülk modeli
│   ├── property_type.py         # Mülk tipi (Daire, Villa, vb.)
│   ├── property_offer.py        # Müşteri teklifleri
│   └── property_tag.py          # Etiketler (Havuzlu, Deniz manzaralı)
├── views/
│   ├── property_views.xml       # Mülk görünümleri
│   ├── property_type_views.xml
│   ├── property_offer_views.xml
│   └── menus.xml                # Menü yapısı
├── security/
│   └── ir.model.access.csv      # Erişim hakları
├── data/
│   └── property_type_data.xml   # Varsayılan mülk tipleri
└── static/
    └── description/
        └── icon.png             # Modül ikonu
```

---

## 📝 Adım Adım Geliştirme

### Adım 1: Modül Skeleton Oluşturma

**__manifest__.py**
```python
{
    'name': 'Real Estate',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Emlak Yönetim Sistemi',
    'description': """
        Real Estate Management Module
        ==============================
        - Mülk yönetimi
        - Müşteri teklifleri
        - Satış süreci takibi
    """,
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'depends': ['base', 'mail', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'data/property_type_data.xml',
        'views/property_views.xml',
        'views/property_type_views.xml',
        'views/property_offer_views.xml',
        'views/menus.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
```

---

### Adım 2: Property Model (Ana Model)

**models/property.py**
```python
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class RealEstateProperty(models.Model):
    _name = 'real.estate.property'
    _description = 'Real Estate Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Email ve aktivite desteği
    _order = 'id desc'

    # Temel Bilgiler
    name = fields.Char(string='Title', required=True, tracking=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(
        string='Available From',
        default=fields.Date.today,
        copy=False
    )
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', copy=False, readonly=True)
    
    # Mülk Özellikleri
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string='Garden Orientation')
    
    # İlişkisel Alanlar
    property_type_id = fields.Many2one(
        'real.estate.property.type',
        string='Property Type',
        required=True
    )
    salesperson_id = fields.Many2one(
        'res.users',
        string='Salesperson',
        default=lambda self: self.env.user
    )
    buyer_id = fields.Many2one(
        'res.partner',
        string='Buyer',
        copy=False,
        tracking=True
    )
    tag_ids = fields.Many2many(
        'real.estate.property.tag',
        string='Tags'
    )
    offer_ids = fields.One2many(
        'real.estate.property.offer',
        'property_id',
        string='Offers'
    )
    
    # Computed Fields
    total_area = fields.Integer(
        string='Total Area (sqm)',
        compute='_compute_total_area'
    )
    best_offer = fields.Float(
        string='Best Offer',
        compute='_compute_best_offer'
    )
    
    # Durum
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], default='new', required=True, string='Status', tracking=True)
    
    # Aktif/Pasif
    active = fields.Boolean(string='Active', default=True)
    
    # Compute Methods
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    
    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for record in self:
            if record.offer_ids:
                record.best_offer = max(record.offer_ids.mapped('price'))
            else:
                record.best_offer = 0.0
    
    # Onchange Methods
    @api.onchange('garden')
    def _onchange_garden(self):
        if not self.garden:
            self.garden_area = 0
            self.garden_orientation = False
    
    # Constraints
    @api.constrains('expected_price')
    def _check_expected_price(self):
        for record in self:
            if record.expected_price <= 0:
                raise ValidationError("Expected price must be positive!")
    
    @api.constrains('selling_price', 'expected_price')
    def _check_selling_price(self):
        for record in self:
            if record.selling_price > 0:
                if record.selling_price < record.expected_price * 0.9:
                    raise ValidationError(
                        "Selling price cannot be lower than 90% of expected price!"
                    )
    
    # SQL Constraints
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)', 
         'Expected price must be strictly positive'),
        ('check_selling_price', 'CHECK(selling_price >= 0)', 
         'Selling price must be positive'),
    ]
    
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
    
    # Override unlink (delete)
    def unlink(self):
        for record in self:
            if record.state not in ['new', 'canceled']:
                raise UserError("You can only delete new or canceled properties!")
        return super().unlink()
```

---

### Adım 3: Property Type Model

**models/property_type.py**
```python
from odoo import models, fields

class RealEstatePropertyType(models.Model):
    _name = 'real.estate.property.type'
    _description = 'Real Estate Property Type'
    _order = 'sequence, name'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    property_ids = fields.One2many(
        'real.estate.property',
        'property_type_id',
        string='Properties'
    )
    
    # SQL Constraints
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Property type name must be unique!'),
    ]
```

---

### Adım 4: Property Offer Model

**models/property_offer.py**
```python
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class RealEstatePropertyOffer(models.Model):
    _name = 'real.estate.property.offer'
    _description = 'Real Estate Property Offer'
    _order = 'price desc'

    price = fields.Float(string='Price', required=True)
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
    ], string='Status', copy=False)
    partner_id = fields.Many2one(
        'res.partner',
        string='Partner',
        required=True
    )
    property_id = fields.Many2one(
        'real.estate.property',
        string='Property',
        required=True
    )
    validity = fields.Integer(string='Validity (days)', default=7)
    date_deadline = fields.Date(
        string='Deadline',
        compute='_compute_date_deadline',
        inverse='_inverse_date_deadline'
    )
    
    # Computed Fields
    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date.date() + timedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today() + timedelta(days=record.validity)
    
    def _inverse_date_deadline(self):
        for record in self:
            if record.create_date and record.date_deadline:
                record.validity = (record.date_deadline - record.create_date.date()).days
    
    # Action Methods
    def action_accept(self):
        for record in self:
            # Diğer teklifleri reddet
            record.property_id.offer_ids.filtered(
                lambda o: o.id != record.id
            ).write({'status': 'refused'})
            
            # Bu teklifi kabul et
            record.status = 'accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
            record.property_id.state = 'offer_accepted'
        return True
    
    def action_refuse(self):
        for record in self:
            record.status = 'refused'
        return True
    
    # Model Methods
    @api.model
    def create(self, vals):
        # Teklif oluşturulduğunda mülk durumunu güncelle
        property_id = self.env['real.estate.property'].browse(vals['property_id'])
        if property_id.state == 'new':
            property_id.state = 'offer_received'
        
        # Düşük teklif kontrolü
        if property_id.offer_ids:
            max_offer = max(property_id.offer_ids.mapped('price'))
            if vals['price'] < max_offer:
                raise ValidationError("Offer must be higher than existing offers!")
        
        return super().create(vals)
    
    # SQL Constraints
    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)', 'Offer price must be positive!'),
    ]
```

---

### Adım 5: Property Tag Model

**models/property_tag.py**
```python
from odoo import models, fields

class RealEstatePropertyTag(models.Model):
    _name = 'real.estate.property.tag'
    _description = 'Real Estate Property Tag'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    color = fields.Integer(string='Color Index')
    
    # SQL Constraints
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Tag name must be unique!'),
    ]
```

---

### Adım 6: Views (Görünümler)

**views/property_views.xml**
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <!-- Tree View -->
    <record id="view_real_estate_property_tree" model="ir.ui.view">
        <field name="name">real.estate.property.tree</field>
        <field name="model">real.estate.property</field>
        <field name="arch" type="xml">
            <tree string="Properties" decoration-success="state=='offer_received'" 
                  decoration-bf="state=='offer_accepted'" decoration-muted="state=='sold'">
                <field name="name"/>
                <field name="property_type_id"/>
                <field name="postcode"/>
                <field name="bedrooms"/>
                <field name="living_area"/>
                <field name="expected_price"/>
                <field name="selling_price"/>
                <field name="state"/>
            </tree>
        </field>
    </record>

    <!-- Form View -->
    <record id="view_real_estate_property_form" model="ir.ui.view">
        <field name="name">real.estate.property.form</field>
        <field name="model">real.estate.property</field>
        <field name="arch" type="xml">
            <form string="Property">
                <header>
                    <button name="action_sold" type="object" string="Sold" 
                            invisible="state in ['sold', 'canceled']"/>
                    <button name="action_cancel" type="object" string="Cancel" 
                            invisible="state in ['sold', 'canceled']"/>
                    <field name="state" widget="statusbar" 
                           statusbar_visible="new,offer_received,offer_accepted,sold"/>
                </header>
                <sheet>
                    <div class="oe_title">
                        <h1>
                            <field name="name" placeholder="Property Title"/>
                        </h1>
                        <field name="tag_ids" widget="many2many_tags" options="{'color_field': 'color'}"/>
                    </div>
                    <group>
                        <group>
                            <field name="property_type_id" options="{'no_create': True}"/>
                            <field name="postcode"/>
                            <field name="date_availability"/>
                        </group>
                        <group>
                            <field name="expected_price"/>
                            <field name="best_offer"/>
                            <field name="selling_price"/>
                        </group>
                    </group>
                    <notebook>
                        <page string="Description">
                            <group>
                                <field name="description"/>
                                <field name="bedrooms"/>
                                <field name="living_area"/>
                                <field name="facades"/>
                                <field name="garage"/>
                                <field name="garden"/>
                                <field name="garden_area" invisible="not garden"/>
                                <field name="garden_orientation" invisible="not garden"/>
                                <field name="total_area"/>
                            </group>
                        </page>
                        <page string="Offers">
                            <field name="offer_ids">
                                <tree editable="bottom" decoration-success="status=='accepted'" 
                                      decoration-danger="status=='refused'">
                                    <field name="price"/>
                                    <field name="partner_id"/>
                                    <field name="validity"/>
                                    <field name="date_deadline"/>
                                    <button name="action_accept" type="object" icon="fa-check" 
                                            invisible="status"/>
                                    <button name="action_refuse" type="object" icon="fa-times" 
                                            invisible="status"/>
                                    <field name="status" invisible="1"/>
                                </tree>
                            </field>
                        </page>
                        <page string="Other Info">
                            <group>
                                <field name="salesperson_id"/>
                                <field name="buyer_id"/>
                            </group>
                        </page>
                    </notebook>
                </sheet>
                <div class="oe_chatter">
                    <field name="message_follower_ids"/>
                    <field name="activity_ids"/>
                    <field name="message_ids"/>
                </div>
            </form>
        </field>
    </record>

    <!-- Kanban View -->
    <record id="view_real_estate_property_kanban" model="ir.ui.view">
        <field name="name">real.estate.property.kanban</field>
        <field name="model">real.estate.property</field>
        <field name="arch" type="xml">
            <kanban default_group_by="property_type_id">
                <field name="state"/>
                <templates>
                    <t t-name="kanban-box">
                        <div class="oe_kanban_global_click">
                            <div class="oe_kanban_details">
                                <strong class="o_kanban_record_title">
                                    <field name="name"/>
                                </strong>
                                <div class="o_kanban_tags_section">
                                    <field name="tag_ids" widget="many2many_tags" options="{'color_field': 'color'}"/>
                                </div>
                                <div class="o_kanban_record_bottom">
                                    <div class="oe_kanban_bottom_left">
                                        <field name="expected_price"/>
                                    </div>
                                    <div class="oe_kanban_bottom_right">
                                        <field name="state" widget="label_selection" 
                                               options="{'classes': {'sold': 'success', 'canceled': 'danger'}}"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </t>
                </templates>
            </kanban>
        </field>
    </record>

    <!-- Search View -->
    <record id="view_real_estate_property_search" model="ir.ui.view">
        <field name="name">real.estate.property.search</field>
        <field name="model">real.estate.property</field>
        <field name="arch" type="xml">
            <search string="Properties">
                <field name="name"/>
                <field name="postcode"/>
                <field name="property_type_id"/>
                <separator/>
                <filter string="Available" name="available" 
                        domain="[('state', 'in', ['new', 'offer_received'])]"/>
                <filter string="Sold" name="sold" domain="[('state', '=', 'sold')]"/>
                <group expand="1" string="Group By">
                    <filter string="Property Type" name="property_type" 
                            context="{'group_by': 'property_type_id'}"/>
                    <filter string="Status" name="status" context="{'group_by': 'state'}"/>
                </group>
            </search>
        </field>
    </record>

    <!-- Action -->
    <record id="action_real_estate_property" model="ir.actions.act_window">
        <field name="name">Properties</field>
        <field name="res_model">real.estate.property</field>
        <field name="view_mode">kanban,tree,form</field>
        <field name="context">{'search_default_available': 1}</field>
        <field name="help" type="html">
            <p class="o_view_nocontent_smiling_face">
                Create a new property
            </p>
        </field>
    </record>
</odoo>
```

---

### Adım 7: Security (Erişim Hakları)

**security/ir.model.access.csv**
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_real_estate_property,access_real_estate_property,model_real_estate_property,base.group_user,1,1,1,1
access_real_estate_property_type,access_real_estate_property_type,model_real_estate_property_type,base.group_user,1,1,1,1
access_real_estate_property_tag,access_real_estate_property_tag,model_real_estate_property_tag,base.group_user,1,1,1,1
access_real_estate_property_offer,access_real_estate_property_offer,model_real_estate_property_offer,base.group_user,1,1,1,1
```

---

## 🎯 Öğrenme Sırası (Öncelikli)

### 1. Mutlaka Öğrenmeniz Gerekenler ✅
- [ ] **Python Temelleri** - Class, inheritance, decorators
- [ ] **Odoo Model API** - fields, api decorators, CRUD
- [ ] **View Yapısı** - Tree, Form, Kanban, Search
- [ ] **XML Syntax** - Odoo view tanımları
- [ ] **Actions ve Menus** - Modülü menüye ekleme

### 2. Önemli Ama Sonra Öğrenebilirsiniz ⚠️
- [ ] **Computed Fields** - Otomatik hesaplanan alanlar
- [ ] **Onchange Methods** - Dinamik form davranışları
- [ ] **Constraints** - Veri doğrulama
- [ ] **Inheritance** - Mevcut modülleri genişletme

### 3. İleri Seviye (İhtiyaç Duyarsan) 🚀
- [ ] **Wizard** - Popup formlar
- [ ] **Report** - PDF raporlar
- [ ] **Email Templates** - Otomatik emailler
- [ ] **Scheduled Actions** - Cron jobs
- [ ] **Website Integration** - Web sitesi entegrasyonu

---

## 📚 Önerilen Öğrenme Kaynakları

### Resmi Odoo Tutorials
1. **Odoo Official Tutorial**
   - https://www.odoo.com/documentation/19.0/developer/tutorials/server_framework_101.html
   - Real Estate örneği ile anlatılıyor! (Tam sizin için)

2. **Odoo ORM API**
   - https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html

### Video Kaynaklar
- **Odoo Mates** YouTube kanalı
- **Cybrosys** YouTube kanalı

---

## ⏱️ Gerçekçi Zaman Planı

| Faz | Süre | Açıklama |
|-----|------|----------|
| Python + Odoo Temelleri | 2-3 gün | Model, field, view kavramları |
| İlk Basit Modül | 1 gün | TODO app gibi basit bir şey |
| Real Estate Modülü | 3-5 gün | Yukarıdaki kodu uygulama |
| Test ve İyileştirme | 2-3 gün | Bug fix, özellik ekleme |
| **TOPLAM** | **8-12 gün** | Günde 4-6 saat çalışma ile |

---

## 💡 Pratik İpuçları

1. **Küçük Başlayın**: İlk önce sadece Property modelini yapın, sonra diğerlerini ekleyin
2. **Resmi Tutorial'ı Takip Edin**: Odoo'nun kendi Real Estate tutorial'ı var, onu takip edin
3. **Kod Kopyalamayın, Yazın**: Kodu elle yazarak daha iyi öğrenirsiniz
4. **Hata Loglarını Okuyun**: Odoo hata mesajları çok açıklayıcıdır
5. **Developer Mode**: Her zaman açık tutun

---

## 🚀 Başlangıç Adımları

1. **Odoo Tutorial'ı Açın**
   - https://www.odoo.com/documentation/19.0/developer/tutorials/server_framework_101.html
   - Bu tutorial tam olarak Real Estate modülü yapımını anlatıyor!

2. **Tutorials Klasörünüzü Kullanın**
   - `C:\Users\cakma\Documents\Odoo-Files\tutorials` klasöründe çalışın
   - Burada `real_estate` adında yeni bir klasör oluşturun

3. **Adım Adım İlerleyin**
   - Her adımı test edin
   - Çalışmayan bir şey varsa bana sorun

---

**Başarılar! 🏠**

Sorularınız olursa çekinmeden sorun!
