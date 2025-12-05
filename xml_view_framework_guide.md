# 🎨 Odoo XML View Framework - Kapsamlı Rehber

## 📋 İçindekiler
1. [View Tipleri](#view-tipleri)
2. [View Yapısı](#view-yapısı)
3. [Field Widgets](#field-widgets)
4. [Attributes ve Modifiers](#attributes-ve-modifiers)
5. [Actions](#actions)
6. [Menus](#menus)
7. [İleri Seviye Özellikler](#i̇leri-seviye-özellikler)

---

## 1. View Tipleri

Odoo'da 7 ana view tipi vardır:

### 📊 List View (Tree View)
**Kullanım:** Kayıtları tablo halinde gösterir

```xml
<list string="Properties">
    <field name="name"/>
    <field name="price"/>
    <field name="state"/>
</list>
```

**Özellikler:**
- `editable="top"` veya `editable="bottom"` - Satır içi düzenleme
- `decoration-*` - Koşullu renklendirme
- `create="false"` - Create butonunu gizle
- `delete="false"` - Delete butonunu gizle

**Örnek:**
```xml
<list string="Properties" 
      editable="bottom"
      decoration-success="state=='sold'"
      decoration-danger="state=='canceled'">
    <field name="name"/>
    <field name="price"/>
    <field name="state" invisible="1"/>
</list>
```

---

### 📝 Form View
**Kullanım:** Tek bir kaydın detaylarını gösterir

```xml
<form string="Property">
    <sheet>
        <h1>
            <field name="name"/>
        </h1>
        <group>
            <field name="price"/>
            <field name="state"/>
        </group>
    </sheet>
</form>
```

**Yapı Elemanları:**
- `<sheet>` - Ana içerik alanı
- `<header>` - Üst kısım (butonlar, statusbar)
- `<group>` - Field'ları gruplar (2 sütun)
- `<notebook>` - Sekmeler
- `<page>` - Sekme sayfası

**Örnek:**
```xml
<form>
    <header>
        <button name="action_confirm" string="Confirm" type="object"/>
        <field name="state" widget="statusbar"/>
    </header>
    <sheet>
        <div class="oe_title">
            <h1><field name="name"/></h1>
        </div>
        <group>
            <group string="Temel Bilgiler">
                <field name="date"/>
                <field name="partner_id"/>
            </group>
            <group string="Fiyatlandırma">
                <field name="price"/>
                <field name="currency_id"/>
            </group>
        </group>
        <notebook>
            <page string="Açıklama">
                <field name="description"/>
            </page>
            <page string="Notlar">
                <field name="notes"/>
            </page>
        </notebook>
    </sheet>
    <div class="oe_chatter">
        <field name="message_follower_ids"/>
        <field name="message_ids"/>
    </div>
</form>
```

---

### 🎴 Kanban View
**Kullanım:** Kartlar halinde görünüm (Trello benzeri)

```xml
<kanban>
    <templates>
        <t t-name="kanban-box">
            <div class="oe_kanban_card">
                <div class="oe_kanban_content">
                    <field name="name"/>
                    <field name="price"/>
                </div>
            </div>
        </t>
    </templates>
</kanban>
```

**QWeb Template:** Kanban view'da QWeb template kullanılır

---

### 🔍 Search View
**Kullanım:** Filtreleme ve gruplama

```xml
<search>
    <field name="name"/>
    <field name="partner_id"/>
    <filter string="Available" name="available" 
            domain="[('state', '=', 'available')]"/>
    <group expand="0" string="Group By">
        <filter string="Status" name="status" 
                context="{'group_by': 'state'}"/>
    </group>
</search>
```

---

### 📈 Graph View
**Kullanım:** Grafik gösterimi

```xml
<graph string="Sales Analysis" type="bar">
    <field name="date"/>
    <field name="price" type="measure"/>
</graph>
```

**Tipler:** `bar`, `line`, `pie`

---

### 📊 Pivot View
**Kullanım:** Pivot tablo

```xml
<pivot string="Sales Pivot">
    <field name="date" type="row"/>
    <field name="partner_id" type="col"/>
    <field name="price" type="measure"/>
</pivot>
```

---

### 📅 Calendar View
**Kullanım:** Takvim görünümü

```xml
<calendar string="Meetings" 
          date_start="start_date" 
          date_stop="end_date"
          color="partner_id">
    <field name="name"/>
</calendar>
```

---

## 2. View Yapısı

### Record Tanımı

```xml
<record id="view_unique_id" model="ir.ui.view">
    <field name="name">model.name.view_type</field>
    <field name="model">model.name</field>
    <field name="arch" type="xml">
        <!-- View içeriği -->
    </field>
</record>
```

**Parametreler:**
- `id` - Benzersiz tanımlayıcı
- `name` - View adı (genellikle `model.name.view_type`)
- `model` - Hangi model için
- `arch` - View mimarisi (XML)

---

## 3. Field Widgets

Widget'lar field'ların nasıl görüneceğini belirler.

### Temel Widgets

```xml
<!-- Char field -->
<field name="name"/>

<!-- Email -->
<field name="email" widget="email"/>

<!-- Phone -->
<field name="phone" widget="phone"/>

<!-- URL -->
<field name="website" widget="url"/>

<!-- Image -->
<field name="image" widget="image"/>

<!-- HTML Editor -->
<field name="description" widget="html"/>

<!-- Badge -->
<field name="state" widget="badge"/>

<!-- Statusbar -->
<field name="state" widget="statusbar" 
       statusbar_visible="draft,confirmed,done"/>

<!-- Progress Bar -->
<field name="progress" widget="progressbar"/>

<!-- Many2one -->
<field name="partner_id" widget="many2one"/>

<!-- Many2many Tags -->
<field name="tag_ids" widget="many2many_tags"/>

<!-- One2many List -->
<field name="line_ids" widget="one2many_list"/>

<!-- Boolean -->
<field name="active" widget="boolean_toggle"/>

<!-- Date -->
<field name="date" widget="date"/>

<!-- Datetime -->
<field name="datetime" widget="datetime"/>

<!-- Monetary -->
<field name="price" widget="monetary"/>

<!-- Integer -->
<field name="quantity" widget="integer"/>

<!-- Float -->
<field name="amount" widget="float"/>

<!-- Selection -->
<field name="state" widget="selection"/>

<!-- Radio -->
<field name="type" widget="radio"/>

<!-- Priority (Yıldızlar) -->
<field name="priority" widget="priority"/>

<!-- Handle (Sıralama için) -->
<field name="sequence" widget="handle"/>
```

---

## 4. Attributes ve Modifiers

### Field Attributes

```xml
<!-- Zorunlu -->
<field name="name" required="1"/>

<!-- Sadece okunur -->
<field name="total" readonly="1"/>

<!-- Görünmez -->
<field name="internal_ref" invisible="1"/>

<!-- Placeholder -->
<field name="name" placeholder="Enter property name..."/>

<!-- Domain (Filtreleme) -->
<field name="partner_id" 
       domain="[('customer', '=', True)]"/>

<!-- Context (Varsayılan değerler) -->
<field name="partner_id" 
       context="{'default_customer': True}"/>

<!-- Options -->
<field name="tag_ids" 
       options="{'color_field': 'color', 'no_create': True}"/>

<!-- Class (CSS) -->
<field name="name" class="oe_inline"/>

<!-- Style -->
<field name="name" style="width: 50%"/>
```

### Dinamik Attributes (attrs)

```xml
<!-- state == 'draft' ise readonly -->
<field name="name" 
       attrs="{'readonly': [('state', '!=', 'draft')]}"/>

<!-- garden == True ise required -->
<field name="garden_area" 
       attrs="{'required': [('garden', '=', True)],
               'invisible': [('garden', '=', False)]}"/>

<!-- Çoklu koşul -->
<field name="selling_price" 
       attrs="{'readonly': [('state', 'in', ['sold', 'canceled'])],
               'required': [('state', '=', 'sold')]}"/>
```

**Operatörler:**
- `=` - Eşit
- `!=` - Eşit değil
- `>`, `<`, `>=`, `<=` - Karşılaştırma
- `in` - Liste içinde
- `not in` - Liste dışında

---

### Decoration (Renklendirme)

List view'da satırları renklendirir:

```xml
<list decoration-success="state=='sold'"
      decoration-danger="state=='canceled'"
      decoration-info="state=='draft'"
      decoration-warning="state=='pending'"
      decoration-muted="active==False"
      decoration-bf="priority==3">
    <field name="name"/>
    <field name="state" invisible="1"/>
    <field name="active" invisible="1"/>
    <field name="priority" invisible="1"/>
</list>
```

**Decoration Tipleri:**
- `decoration-success` - Yeşil
- `decoration-danger` - Kırmızı
- `decoration-warning` - Turuncu
- `decoration-info` - Mavi
- `decoration-muted` - Gri
- `decoration-bf` - Kalın (bold)
- `decoration-it` - İtalik

---

## 5. Actions

### Window Action

```xml
<record id="action_estate_property" model="ir.actions.act_window">
    <field name="name">Properties</field>
    <field name="res_model">estate.property</field>
    <field name="view_mode">list,form,kanban</field>
    <field name="domain">[('active', '=', True)]</field>
    <field name="context">{'default_state': 'new'}</field>
    <field name="help" type="html">
        <p class="o_view_nocontent_smiling_face">
            Create your first property
        </p>
    </field>
</record>
```

**Parametreler:**
- `name` - Action adı
- `res_model` - Model
- `view_mode` - View sırası
- `domain` - Filtre
- `context` - Varsayılan değerler
- `limit` - Sayfa başına kayıt sayısı
- `target` - `new` (popup), `current` (aynı sayfa)

---

### Server Action

Python kodu çalıştırır:

```xml
<record id="action_set_sold" model="ir.actions.server">
    <field name="name">Set as Sold</field>
    <field name="model_id" ref="model_estate_property"/>
    <field name="state">code</field>
    <field name="code">
        records.write({'state': 'sold'})
    </field>
</record>
```

---

## 6. Menus

### Menu Hiyerarşisi

```xml
<!-- Ana Menü -->
<menuitem id="menu_estate_root" 
          name="Real Estate"/>

<!-- Alt Menü -->
<menuitem id="menu_estate_property" 
          name="Properties" 
          parent="menu_estate_root" 
          action="action_estate_property"
          sequence="10"/>

<!-- İkinci Seviye Alt Menü -->
<menuitem id="menu_estate_property_available" 
          name="Available Properties" 
          parent="menu_estate_property" 
          action="action_estate_property_available"
          sequence="1"/>
```

**Parametreler:**
- `id` - Benzersiz ID
- `name` - Menü adı
- `parent` - Üst menü ID'si
- `action` - Açılacak action
- `sequence` - Sıralama (küçük önce gelir)
- `groups` - Erişim grupları

---

## 7. İleri Seviye Özellikler

### Butonlar

```xml
<form>
    <header>
        <!-- Object Button (Python method çağırır) -->
        <button name="action_confirm" 
                string="Confirm" 
                type="object"
                class="btn-primary"
                invisible="state != 'draft'"/>
        
        <!-- Action Button (Action açar) -->
        <button name="%(action_report)d" 
                string="Print" 
                type="action"/>
        
        <!-- Statusbar -->
        <field name="state" widget="statusbar" 
               statusbar_visible="draft,confirmed,done"/>
    </header>
</form>
```

---

### Chatter (Mesajlaşma)

```xml
<form>
    <sheet>
        <!-- ... -->
    </sheet>
    <div class="oe_chatter">
        <field name="message_follower_ids"/>
        <field name="activity_ids"/>
        <field name="message_ids"/>
    </div>
</form>
```

**Gerekli:** Model'de `_inherit = ['mail.thread', 'mail.activity.mixin']`

---

### Smart Buttons

```xml
<form>
    <sheet>
        <div class="oe_button_box" name="button_box">
            <button name="action_view_offers" 
                    type="object" 
                    class="oe_stat_button" 
                    icon="fa-handshake-o">
                <field name="offer_count" widget="statinfo" 
                       string="Offers"/>
            </button>
        </div>
        <!-- ... -->
    </sheet>
</form>
```

---

### Inline Editing

```xml
<!-- List view'da satır içi düzenleme -->
<list editable="bottom">
    <field name="name"/>
    <field name="quantity"/>
    <field name="price"/>
</list>

<!-- Form view'da inline -->
<field name="line_ids">
    <list editable="bottom">
        <field name="product_id"/>
        <field name="quantity"/>
        <field name="price"/>
    </list>
</field>
```

---

### Conditional Visibility

```xml
<!-- Python expression -->
<group invisible="state == 'draft'">
    <field name="confirmed_date"/>
</group>

<!-- Context-based -->
<field name="internal_notes" 
       groups="base.group_no_one"/>
```

---

## 🎯 Pratik Örnekler

### Örnek 1: Gelişmiş Form View

```xml
<form>
    <header>
        <button name="action_confirm" string="Confirm" 
                type="object" class="btn-primary"
                invisible="state != 'draft'"/>
        <button name="action_cancel" string="Cancel" 
                type="object" class="btn-secondary"
                invisible="state in ['done', 'canceled']"/>
        <field name="state" widget="statusbar" 
               statusbar_visible="draft,confirmed,done"/>
    </header>
    <sheet>
        <div class="oe_button_box">
            <button name="action_view_invoices" type="object" 
                    class="oe_stat_button" icon="fa-pencil-square-o">
                <field name="invoice_count" widget="statinfo" 
                       string="Invoices"/>
            </button>
        </div>
        <div class="oe_title">
            <h1>
                <field name="name" placeholder="Property Name"/>
            </h1>
            <field name="tag_ids" widget="many2many_tags" 
                   options="{'color_field': 'color'}"/>
        </div>
        <group>
            <group string="Basic Info">
                <field name="property_type_id"/>
                <field name="postcode"/>
                <field name="date_availability"/>
            </group>
            <group string="Pricing">
                <field name="expected_price"/>
                <field name="best_offer" readonly="1"/>
                <field name="selling_price" readonly="1"/>
            </group>
        </group>
        <notebook>
            <page string="Description">
                <field name="description" widget="html"/>
            </page>
            <page string="Offers">
                <field name="offer_ids">
                    <list editable="bottom" 
                          decoration-success="status=='accepted'"
                          decoration-danger="status=='refused'">
                        <field name="price"/>
                        <field name="partner_id"/>
                        <field name="validity"/>
                        <button name="action_accept" type="object" 
                                icon="fa-check"/>
                        <button name="action_refuse" type="object" 
                                icon="fa-times"/>
                        <field name="status" invisible="1"/>
                    </list>
                </field>
            </page>
        </notebook>
    </sheet>
    <div class="oe_chatter">
        <field name="message_follower_ids"/>
        <field name="activity_ids"/>
        <field name="message_ids"/>
    </div>
</form>
```

---

## 📚 Kaynaklar

- **Resmi Döküman:** https://www.odoo.com/documentation/19.0/developer/reference/user_interface/view_records.html
- **View Architecture:** https://www.odoo.com/documentation/19.0/developer/reference/user_interface/view_architectures.html
- **QWeb:** https://www.odoo.com/documentation/19.0/developer/reference/frontend/qweb.html

---

**Başarılar! 🎨**
