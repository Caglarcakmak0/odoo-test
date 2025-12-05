# 🏠 Odoo Real Estate Tutorial - Kapsamlı Özet

Bu dokümanda, Odoo 19 Enterprise ile Real Estate modülü geliştirme sürecinde öğrendiğimiz her şey yer almaktadır.

---

## 📋 İçindekiler

1. [Kurulum ve Hazırlık](#kurulum-ve-hazırlık)
2. [Modül Yapısı](#modül-yapısı)
3. [Model Geliştirme](#model-geliştirme)
4. [View Geliştirme](#view-geliştirme)
5. [Security](#security)
6. [Actions ve Menus](#actions-ve-menus)
7. [Önemli Kavramlar](#önemli-kavramlar)

---

## 1. Kurulum ve Hazırlık

### ✅ Kurulum Kontrol Listesi

```
✅ Odoo 19.0 Enterprise - C:\Program Files\Odoo 19.0e.20251202
✅ PostgreSQL (Odoo ile birlikte geldi) - PostgreSQL_For_Odoo servisi
✅ Python 3.13.7
✅ Git 2.51.0
✅ Tutorials klasörü - C:\Users\cakma\Documents\Odoo-Files\tutorials
```

### 🔧 Odoo Servisi Yönetimi

```powershell
# Servis durumunu kontrol et
Get-Service -Name "odoo-server-19.0"

# Servisi başlat (Yönetici gerekli)
Start-Service -Name "odoo-server-19.0"

# Servisi durdur
Stop-Service -Name "odoo-server-19.0"

# Servisi yeniden başlat
Restart-Service -Name "odoo-server-19.0"
```

### 🌐 Web Arayüzü

```
URL: http://localhost:8069
```

---

## 2. Modül Yapısı

### 📁 Estate Modülü Klasör Yapısı

```
estate/
├── __init__.py                      # Ana package başlatıcı
├── __manifest__.py                  # Modül tanımı
├── models/
│   ├── __init__.py                  # Models package başlatıcı
│   └── estate_property.py           # Property modeli
├── views/
│   └── estate_property_views.xml    # View tanımları
└── security/
    └── ir.model.access.csv          # Erişim hakları
```

### 📄 __manifest__.py

```python
{
    'name': 'Real Estate',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Your Name',
    'category': 'Sales',
    'description': """
    Real Estate Management Module
    ==============================
    Manage real estate properties, offers, and sales.
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
```

**Önemli Parametreler:**
- `depends`: Bağımlı modüller (en az `base` gerekli)
- `data`: XML dosyaları (sıralama önemli: önce security, sonra views)
- `application`: True ise Apps filtresinde görünür

---

## 3. Model Geliştirme

### 🏗️ Model Tanımı (estate_property.py)

```python
from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"
    
    # Temel Bilgiler
    name = fields.Char(string='Başlık', required=True)
    description = fields.Text(string='Açıklama')
    postcode = fields.Char(string='Posta Kodu')
    date_availability = fields.Date(
        string='Müsaitlik Tarihi', 
        copy=False,                    # Kopyalanmaz
        default=fields.Date.today      # Varsayılan: bugün
    )
    
    # Fiyatlandırma
    expected_price = fields.Float(string='Beklenen Fiyat', required=True)
    selling_price = fields.Float(
        string='Satış Fiyatı', 
        readonly=True,                 # Sadece okunur
        copy=False                     # Kopyalanmaz
    )
    
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
    
    # İmkanlar
    garage = fields.Boolean(string='Garaj')
    garden = fields.Boolean(string='Bahçe')
    garden_area = fields.Integer(string='Bahçe Alanı (metrekare)')
    garden_orientation = fields.Selection(
        string='Bahçe Yönü',
        selection=[
            ('north', 'Kuzey'), 
            ('south', 'Güney'), 
            ('east', 'Doğu'), 
            ('west', 'Batı')
        ]
    )
```

### 📊 Field Tipleri

| Field Tipi | Kullanım | Örnek |
|------------|----------|-------|
| `Char` | Kısa metin | `name = fields.Char()` |
| `Text` | Uzun metin | `description = fields.Text()` |
| `Integer` | Tam sayı | `bedrooms = fields.Integer()` |
| `Float` | Ondalıklı sayı | `price = fields.Float()` |
| `Boolean` | Evet/Hayır | `garage = fields.Boolean()` |
| `Date` | Tarih | `date = fields.Date()` |
| `Selection` | Seçenekli | `state = fields.Selection([...])` |

### 🎯 Field Parametreleri

```python
# Zorunlu alan
name = fields.Char(required=True)

# Sadece okunur
selling_price = fields.Float(readonly=True)

# Kopyalanmaz
date_availability = fields.Date(copy=False)

# Varsayılan değer
bedrooms = fields.Integer(default=2)

# String (label)
name = fields.Char(string='Başlık')
```

### 🔍 Selection Field Yapısı

```python
garden_orientation = fields.Selection(
    selection=[
        ('north', 'Kuzey'),  # ('veritabanı_değeri', 'Görünen_etiket')
        ('south', 'Güney'),
    ]
)
```

**Önemli:**
- İlk değer (north): Veritabanında saklanır
- İkinci değer (Kuzey): Kullanıcıya gösterilir

---

## 4. View Geliştirme

### 🎨 View Tipleri ve Kullanımları

```
┌─────────────────────────────────────────┐
│  Odoo View Hiyerarşisi                  │
├─────────────────────────────────────────┤
│  1. Search View   → Filtreleme          │
│  2. List View     → Tablo görünümü      │
│  3. Form View     → Detay görünümü      │
│  4. Kanban View   → Kart görünümü       │
└─────────────────────────────────────────┘
```

---

### 🔍 Search View

```xml
<search string="Properties">
    <!-- Arama Alanları -->
    <field name="name"/>
    <field name="postcode"/>
    
    <!-- Domain Filter (Filtreleme) -->
    <filter string="With Garden" 
            name="filter_garden" 
            domain="[('garden', '=', True)]"/>
    
    <separator/>
    
    <!-- Context Filter (Gruplama) -->
    <group expand="0" string="Group By">
        <filter string="Postcode" 
                name="group_postcode" 
                context="{'group_by': 'postcode'}"/>
    </group>
</search>
```

**Ekranda Görünüm:**

```
┌─────────────────────────────────────────┐
│ 🔍 [Search box]  [Filters ▼] [Group ▼] │
├─────────────────────────────────────────┤
│ Filters:                                │
│ ☐ With Garden                           │
│ ─────────────                           │
│ Group By:                               │
│ ☐ Postcode                              │
└─────────────────────────────────────────┘
```

**Domain Syntax:**

```python
# Basit koşul
[('field', 'operator', value)]

# Örnekler
[('garden', '=', True)]                    # Bahçesi olanlar
[('bedrooms', '>=', 3)]                    # 3+ yatak odalı
[('expected_price', '>', 1000000)]         # 1M üzeri

# AND koşulu (varsayılan)
[('garden', '=', True), ('garage', '=', True)]

# OR koşulu
['|', ('garden', '=', True), ('garage', '=', True)]
```

**Operatörler:**
- `=`, `!=` - Eşitlik
- `>`, `<`, `>=`, `<=` - Karşılaştırma
- `in`, `not in` - Liste kontrolü
- `like`, `ilike` - Metin içerir (ilike = case-insensitive)

---

### 📋 List View

```xml
<list string="Properties">
    <field name="name"/>
    <field name="postcode"/>
    <field name="bedrooms"/>
    <field name="living_area"/>
    <field name="expected_price"/>
    <field name="selling_price"/>
    <field name="date_availability"/>
</list>
```

**Ekranda Görünüm:**

```
┌─────────────────────────────────────────────────────────────┐
│ Properties                                    [+ New]        │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│ Title    │ Postcode │ Bedrooms │ Area     │ Expected Price  │
├──────────┼──────────┼──────────┼──────────┼─────────────────┤
│ Villa    │ 34353    │ 4        │ 250      │ 15,000,000      │
│ Daire    │ 34340    │ 2        │ 120      │ 5,000,000       │
└──────────┴──────────┴──────────┴──────────┴─────────────────┘
```

**List View Özellikleri:**

```xml
<!-- Satır içi düzenleme -->
<list editable="bottom">

<!-- Koşullu renklendirme -->
<list decoration-success="state=='sold'"
      decoration-danger="state=='canceled'">

<!-- Create/Delete butonlarını gizle -->
<list create="false" delete="false">
```

**Decoration Tipleri:**
- `decoration-success` → Yeşil
- `decoration-danger` → Kırmızı
- `decoration-warning` → Turuncu
- `decoration-info` → Mavi
- `decoration-muted` → Gri
- `decoration-bf` → Kalın (bold)

---

### 📝 Form View

```xml
<form string="Property">
    <sheet>
        <h1>
            <field name="name"/>
        </h1>
        <group>
            <group>
                <field name="postcode"/>
                <field name="date_availability"/>
            </group>
            <group>
                <field name="expected_price"/>
                <field name="selling_price"/>
            </group>
        </group>
        <notebook>
            <page string="Açıklama">
                <field name="description"/>
            </page>
            <page string="Mülk Detayları">
                <group>
                    <field name="bedrooms"/>
                    <field name="living_area"/>
                    <field name="facades"/>
                    <field name="toilets"/>
                    <field name="garage"/>
                    <field name="garden"/>
                    <field name="garden_area"/>
                    <field name="garden_orientation"/>
                </group>
            </page>
        </notebook>
    </sheet>
</form>
```

**Ekranda Görünüm:**

```
┌─────────────────────────────────────────────────────────┐
│  Lüks Villa - Beşiktaş                                  │ ← h1
├─────────────────────────────────────────────────────────┤
│  Posta Kodu        │  Beklenen Fiyat                    │ ← 2 sütun
│  [34353]           │  [15,000,000]                      │
│                    │                                    │
│  Müsaitlik Tarihi  │  Satış Fiyatı                      │
│  [2025-01-01]      │  [0] (readonly)                    │
├─────────────────────────────────────────────────────────┤
│  [Açıklama] [Mülk Detayları]                           │ ← Sekmeler
├─────────────────────────────────────────────────────────┤
│  Açıklama içeriği...                                    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Form View Yapı Elemanları:**

```xml
<form>
    <header>
        <!-- Butonlar ve statusbar -->
    </header>
    <sheet>
        <div class="oe_button_box">
            <!-- Smart buttons -->
        </div>
        <div class="oe_title">
            <!-- Başlık -->
        </div>
        <group>
            <!-- 2 sütun layout -->
            <group>
                <!-- Sol sütun -->
            </group>
            <group>
                <!-- Sağ sütun -->
            </group>
        </group>
        <notebook>
            <!-- Sekmeler -->
            <page string="Sekme 1">
                <!-- İçerik -->
            </page>
        </notebook>
    </sheet>
    <div class="oe_chatter">
        <!-- Mesajlaşma -->
    </div>
</form>
```

---

### 🎯 View Record Yapısı

```xml
<record id="view_estate_property_form" model="ir.ui.view">
    <field name="name">estate.property.form</field>
    <field name="model">estate.property</field>
    <field name="arch" type="xml">
        <form>
            <!-- View içeriği -->
        </form>
    </field>
</record>
```

**Parametreler:**
- `id`: Benzersiz tanımlayıcı (örn: `view_estate_property_form`)
- `model="ir.ui.view"`: Bu bir view kaydıdır
- `name`: View adı (genellikle `model.view_type`)
- `model`: Hangi model için (örn: `estate.property`)
- `arch`: View mimarisi (XML içeriği)

**Önemli:** `model="ir.ui.view"` → Odoo'nun built-in modeli, tüm view'ları saklar

---

## 5. Security

### 🔐 ir.model.access.csv

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_estate_property,access_estate_property,model_estate_property,base.group_user,1,1,1,1
```

**Sütun Açıklamaları:**

| Sütun | Değer | Açıklama |
|-------|-------|----------|
| `id` | `access_estate_property` | Benzersiz tanımlayıcı |
| `name` | `access_estate_property` | İsim |
| `model_id:id` | `model_estate_property` | Model adı (`estate.property` → `model_estate_property`) |
| `group_id:id` | `base.group_user` | Kullanıcı grubu (tüm kullanıcılar) |
| `perm_read` | `1` | Okuma izni (1=Evet, 0=Hayır) |
| `perm_write` | `1` | Yazma izni |
| `perm_create` | `1` | Oluşturma izni |
| `perm_unlink` | `1` | Silme izni |

---

## 6. Actions ve Menus

### 🎬 Window Action

```xml
<record id="action_estate_property" model="ir.actions.act_window">
    <field name="name">Properties</field>
    <field name="res_model">estate.property</field>
    <field name="view_mode">list,form</field>
    <field name="domain">[('active', '=', True)]</field>
    <field name="context">{'default_state': 'new'}</field>
</record>
```

**Parametreler:**
- `name`: Action adı
- `res_model`: Hangi model
- `view_mode`: View sırası (önce list, sonra form)
- `domain`: Filtre (opsiyonel)
- `context`: Varsayılan değerler (opsiyonel)

---

### 📍 Menu Yapısı

```xml
<!-- Ana Menü (Üst navbar) -->
<menuitem id="menu_estate_root" name="Real Estate"/>

<!-- Alt Menü (Dropdown) -->
<menuitem id="menu_estate_property" 
          name="Properties" 
          parent="menu_estate_root" 
          action="action_estate_property"/>
```

**Ekranda Görünüm:**

```
┌──────────────────────────────────────────┐
│ [Odoo Logo]  Real Estate  Discuss  ...   │ ← Üst Navbar
└──────────────────────────────────────────┘
              ↓ (tıklayınca)
         ┌─────────────┐
         │ Properties  │ ← Dropdown
         └─────────────┘
```

**Menu Parametreleri:**

| Parametre | Açıklama | Örnek |
|-----------|----------|-------|
| `id` | Benzersiz ID | `menu_estate_root` |
| `name` | Menü adı | `"Real Estate"` |
| `parent` | Üst menü | `menu_estate_root` |
| `action` | Açılacak action | `action_estate_property` |
| `sequence` | Sıralama | `10` |

---

## 7. Önemli Kavramlar

### 🔄 Modül Güncelleme Süreci

```
1. Kod değişikliği yap
   ↓
2. Restart (Python kodu için)
   ↓
3. Upgrade (XML/CSV için)
   ↓
4. Test et
```

**Restart Komutu:**
```powershell
Restart-Service -Name "odoo-server-19.0"
```

**Upgrade:**
- Apps → Real Estate → ⋮ → Upgrade

---

### 📦 Odoo'da Her Şey Record

```python
# Mülk kaydı
<record model="estate.property">
    <field name="name">Villa</field>
</record>

# View kaydı
<record model="ir.ui.view">
    <field name="name">estate.property.form</field>
</record>

# Action kaydı
<record model="ir.actions.act_window">
    <field name="name">Properties</field>
</record>
```

**Hepsi veritabanında kayıt olarak saklanır!**

---

### 🎨 Rendering: Form vs Search

| View Tipi | Rendering | Amaç |
|-----------|-----------|------|
| **Form View** | ✅ VAR | Layout kontrolü (2 sütun, h1, notebook) |
| **List View** | ✅ VAR | Sütun sırası, decoration |
| **Search View** | ❌ YOK | Sadece fonksiyon (filter, group) |

**Search view'da layout kontrolü yoktur, Odoo otomatik render eder!**

---

### 🔢 Odoo 19 Değişiklikleri

**Önemli:** Odoo 19'da `<tree>` → `<list>` oldu!

```xml
<!-- Eski (Odoo 16) -->
<tree string="Properties">
    <field name="name"/>
</tree>

<!-- Yeni (Odoo 19) -->
<list string="Properties">
    <field name="name"/>
</list>
```

**Action'da da:**
```xml
<!-- Eski -->
<field name="view_mode">tree,form</field>

<!-- Yeni -->
<field name="view_mode">list,form</field>
```

---

## 📚 Tutorial İlerlemesi

### ✅ Tamamlanan Bölümler

- [x] **Chapter 1:** Architecture Overview
- [x] **Chapter 2:** A New Application
- [x] **Chapter 3:** Models and Basic Fields
- [x] **Chapter 4:** Security
- [x] **Chapter 5:** Finally, Some UI
- [x] **Chapter 6:** Basic Views (List, Form, Search)

### ⏭️ Sıradaki Bölümler

- [ ] **Chapter 7:** Relations Between Models
- [ ] **Chapter 8:** Computed Fields and Onchanges
- [ ] **Chapter 9:** Ready For Some Action?
- [ ] **Chapter 10:** Constraints
- [ ] **Chapter 11:** Add The Sprinkles
- [ ] **Chapter 12:** Interact With Other Modules
- [ ] **Chapter 13:** Reporting

---

## 🔗 Faydalı Linkler

- **Resmi Tutorial:** https://www.odoo.com/documentation/19.0/developer/tutorials/server_framework_101.html
- **View Architecture:** https://www.odoo.com/documentation/19.0/developer/reference/user_interface/view_architectures.html
- **ORM API:** https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html
- **Actions:** https://www.odoo.com/documentation/19.0/developer/reference/backend/actions.html

---

## 🎯 Hızlı Referans

### Model Field Tanımı
```python
field_name = fields.FieldType(
    string='Label',
    required=True,
    readonly=False,
    copy=True,
    default=value
)
```

### View Record Tanımı
```xml
<record id="view_id" model="ir.ui.view">
    <field name="name">model.view_type</field>
    <field name="model">model.name</field>
    <field name="arch" type="xml">
        <view_type>...</view_type>
    </field>
</record>
```

### Domain Syntax
```python
[('field', 'operator', value)]
['|', ('a', '=', 1), ('b', '=', 2)]  # OR
[('a', '=', 1), ('b', '=', 2)]       # AND
```

---

**Son Güncelleme:** 2025-12-03  
**Odoo Versiyonu:** 19.0 Enterprise  
**Tutorial Durumu:** Chapter 6 Tamamlandı
