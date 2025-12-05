# 🎓 Odoo Öğrenme Rehberi

## 📋 İçindekiler
1. [Odoo Arayüzünü Tanıma](#1-odoo-arayüzünü-tanıma)
2. [Temel Modüller](#2-temel-modüller)
3. [İlk Adımlar - Pratik Uygulamalar](#3-i̇lk-adımlar---pratik-uygulamalar)
4. [Developer Mode ve Özelleştirme](#4-developer-mode-ve-özelleştirme)
5. [Modül Geliştirme](#5-modül-geliştirme)
6. [Kaynaklar ve Dökümanlar](#6-kaynaklar-ve-dökümanlar)

---

## 1. Odoo Arayüzünü Tanıma

### Ana Menü Yapısı

```
┌─────────────────────────────────────────────────────┐
│  [Logo]  [Apps]  [Discuss]  [Calendar]  [Contacts]  │  ← Üst Menü
│                                      [🔍] [👤] [⚙️]  │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Ana İçerik Alanı                                   │
│                                                     │
│  • Listeler (Tree View)                            │
│  • Formlar (Form View)                             │
│  • Kanban Görünümü                                 │
│  • Dashboard'lar                                   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Temel Navigasyon

- **Apps**: Tüm modüllerin listesi
- **Discuss**: Dahili mesajlaşma
- **Calendar**: Takvim ve toplantılar
- **Contacts**: Müşteriler, tedarikçiler, çalışanlar
- **🔍 Arama**: Global arama
- **👤 Kullanıcı Menüsü**: Profil, ayarlar, çıkış
- **⚙️ Settings**: Sistem ayarları

---

## 2. Temel Modüller

### 📞 CRM (Müşteri İlişkileri Yönetimi)

**Ne İşe Yarar?**
- Potansiyel müşterileri (leads) takip etme
- Satış hunisi (sales pipeline) yönetimi
- Müşteri iletişim geçmişi

**İlk Adımlar:**
1. Apps → **CRM** modülünü yükleyin
2. **Pipeline** (Huni) oluşturun:
   - Yeni → Teklif → Müzakere → Kazanıldı
3. İlk lead'inizi ekleyin:
   - CRM → Create (Oluştur)
   - Müşteri bilgilerini girin
   - Aşamasını belirleyin

**Pratik Örnek:**
```
Müşteri: ABC Şirketi
Email: info@abc.com
Telefon: 0212 XXX XXXX
Beklenen Gelir: 50,000 TL
Aşama: Teklif
Sorumlu: Admin
```

---

### 🛒 Sales (Satış Yönetimi)

**Ne İşe Yarar?**
- Teklif oluşturma
- Sipariş yönetimi
- Faturalama

**İlk Adımlar:**
1. Apps → **Sales** modülünü yükleyin
2. Ürün ekleyin:
   - Sales → Products → Create
   - Ürün adı, fiyat, açıklama
3. İlk teklifinizi oluşturun:
   - Sales → Quotations → Create
   - Müşteri seçin
   - Ürün ekleyin
   - Confirm Sale (Satışı Onayla)

**Pratik Örnek:**
```
Teklif No: S00001
Müşteri: ABC Şirketi
Ürünler:
  - Laptop Dell XPS 15 x 5 adet = 75,000 TL
  - Mouse Logitech x 5 adet = 500 TL
Toplam: 75,500 TL
```

---

### 📦 Inventory (Stok Yönetimi)

**Ne İşe Yarar?**
- Stok takibi
- Depo yönetimi
- Ürün hareketleri

**İlk Adımlar:**
1. Apps → **Inventory** modülünü yükleyin
2. Depo (Warehouse) yapılandırın
3. Ürün stoğu ekleyin:
   - Inventory → Products → Ürün seçin
   - Update Quantity (Miktar Güncelle)

**Pratik Örnek:**
```
Ürün: Laptop Dell XPS 15
Stok: 100 adet
Konum: WH/Stock
Min. Stok: 10 adet (Otomatik sipariş için)
```

---

### 💰 Accounting (Muhasebe)

**Ne İşe Yarar?**
- Fatura yönetimi
- Gelir-gider takibi
- Mali raporlar

**İlk Adımlar:**
1. Apps → **Accounting** modülünü yükleyin
2. Şirket bilgilerini tamamlayın
3. Banka hesabı ekleyin
4. İlk faturanızı oluşturun:
   - Accounting → Customers → Invoices → Create

---

### 📊 Project (Proje Yönetimi)

**Ne İşe Yarar?**
- Proje ve görev takibi
- Ekip işbirliği
- Zaman takibi

**İlk Adımlar:**
1. Apps → **Project** modülünü yükleyin
2. Yeni proje oluşturun
3. Görevler (tasks) ekleyin
4. Ekip üyelerine atayın

---

## 3. İlk Adımlar - Pratik Uygulamalar

### Senaryo 1: Basit Bir Satış Süreci

**Adım 1: Ürün Oluşturma**
```
Sales → Products → Create

Ürün Bilgileri:
- Product Name: Laptop Dell XPS 15
- Product Type: Storable Product
- Sales Price: 15,000 TL
- Cost: 12,000 TL
- Internal Reference: DELL-XPS-15
```

**Adım 2: Müşteri Ekleme**
```
Contacts → Create

Müşteri Bilgileri:
- Name: ABC Teknoloji A.Ş.
- Company Type: Company
- Phone: 0212 XXX XXXX
- Email: info@abc.com
- Address: İstanbul, Türkiye
- Tax ID: 1234567890
```

**Adım 3: Teklif Oluşturma**
```
Sales → Quotations → Create

Teklif Detayları:
- Customer: ABC Teknoloji A.Ş.
- Expiration: 7 gün sonra
- Add a product: Laptop Dell XPS 15
- Quantity: 5
- Unit Price: 15,000 TL
- Total: 75,000 TL

→ Send by Email (Email ile gönder)
→ Confirm (Onayla)
```

**Adım 4: Fatura Oluşturma**
```
Onaylanan satıştan:
→ Create Invoice (Fatura Oluştur)
→ Confirm (Onayla)
→ Register Payment (Ödeme Kaydet)
```

---

### Senaryo 2: Stok Yönetimi

**Adım 1: Başlangıç Stoğu Girme**
```
Inventory → Products → Laptop Dell XPS 15

→ Update Quantity
- Location: WH/Stock
- New Quantity: 100
```

**Adım 2: Stok Hareketlerini Görüntüleme**
```
Inventory → Reporting → Stock Moves

Burada tüm giriş-çıkışları görebilirsiniz
```

**Adım 3: Otomatik Sipariş Kuralı**
```
Inventory → Configuration → Reordering Rules

- Product: Laptop Dell XPS 15
- Min Quantity: 10
- Max Quantity: 100
- Quantity Multiple: 10

→ Stok 10'un altına düşünce otomatik sipariş oluşturur
```

---

## 4. Developer Mode ve Özelleştirme

### Developer Mode'u Aktifleştirme

**Yöntem 1: Settings'den**
```
Settings → Activate the developer mode (en altta)
```

**Yöntem 2: URL'den**
```
http://localhost:8069/web?debug=1
```

### Developer Mode'da Neler Yapabilirsiniz?

1. **Teknik Menüler**
   - Settings → Technical
   - Database Structure (Veritabanı yapısı)
   - Views (Görünümler)
   - Actions (Aksiyonlar)
   - Menus (Menüler)

2. **View Düzenleme**
   - Herhangi bir sayfada → Debug icon → Edit View
   - XML kodunu görebilir ve düzenleyebilirsiniz

3. **Field İnceleme**
   - Herhangi bir alana tıklayın → Debug icon
   - Field Properties (Alan özellikleri)
   - Model adı, field adı, type vb.

4. **Python Kod Çalıştırma**
   - Settings → Technical → Python Code
   - Odoo API'sini test edebilirsiniz

---

## 5. Modül Geliştirme

### Odoo Modül Yapısı

```
my_module/
├── __init__.py           # Python package başlatıcı
├── __manifest__.py       # Modül tanımı
├── models/              # Veri modelleri
│   ├── __init__.py
│   └── my_model.py
├── views/               # XML görünümleri
│   └── my_views.xml
├── security/            # Erişim hakları
│   └── ir.model.access.csv
├── data/                # Demo/başlangıç verileri
│   └── demo_data.xml
└── static/              # CSS, JS, resimler
    └── src/
        ├── css/
        ├── js/
        └── img/
```

### Basit Bir Modül Örneği

**__manifest__.py**
```python
{
    'name': 'My First Module',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'İlk Odoo modülüm',
    'description': """
        Bu benim ilk Odoo modülüm.
        Basit bir TODO listesi uygulaması.
    """,
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_views.xml',
    ],
    'installable': True,
    'application': True,
}
```

**models/todo.py**
```python
from odoo import models, fields, api

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'TODO Task'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    is_done = fields.Boolean(string='Done?')
    due_date = fields.Date(string='Due Date')
    
    @api.depends('is_done')
    def _compute_status(self):
        for task in self:
            task.status = 'Done' if task.is_done else 'Pending'
    
    status = fields.Char(compute='_compute_status', store=True)
```

**views/todo_views.xml**
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <!-- Tree View -->
    <record id="view_todo_task_tree" model="ir.ui.view">
        <field name="name">todo.task.tree</field>
        <field name="model">todo.task</field>
        <field name="arch" type="xml">
            <tree>
                <field name="name"/>
                <field name="due_date"/>
                <field name="is_done"/>
                <field name="status"/>
            </tree>
        </field>
    </record>

    <!-- Form View -->
    <record id="view_todo_task_form" model="ir.ui.view">
        <field name="name">todo.task.form</field>
        <field name="model">todo.task</field>
        <field name="arch" type="xml">
            <form>
                <sheet>
                    <group>
                        <field name="name"/>
                        <field name="description"/>
                        <field name="due_date"/>
                        <field name="is_done"/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>

    <!-- Action -->
    <record id="action_todo_task" model="ir.actions.act_window">
        <field name="name">TODO Tasks</field>
        <field name="res_model">todo.task</field>
        <field name="view_mode">tree,form</field>
    </record>

    <!-- Menu -->
    <menuitem id="menu_todo_root" name="TODO"/>
    <menuitem id="menu_todo_task" 
              name="Tasks" 
              parent="menu_todo_root" 
              action="action_todo_task"/>
</odoo>
```

---

## 6. Kaynaklar ve Dökümanlar

### Resmi Dökümanlar

1. **Odoo Documentation**
   - https://www.odoo.com/documentation/19.0/
   - Kullanıcı kılavuzları
   - Geliştirici dökümanları

2. **Odoo Tutorials**
   - https://www.odoo.com/slides
   - Video eğitimler
   - Adım adım rehberler

3. **Odoo API Reference**
   - https://www.odoo.com/documentation/19.0/developer/reference/
   - ORM metodları
   - View tipleri
   - QWeb şablonları

### Topluluk Kaynakları

1. **Odoo Community Forum**
   - https://www.odoo.com/forum
   - Soru-cevap
   - Problem çözümleri

2. **GitHub**
   - https://github.com/odoo/odoo
   - Kaynak kod
   - Örnek modüller

3. **YouTube Kanalları**
   - Odoo Official
   - Odoo Mates
   - Cybrosys Techno Solutions

### Türkçe Kaynaklar

1. **Odoo Türkiye Topluluğu**
   - Facebook grupları
   - LinkedIn grupları

2. **Türkçe Blog'lar**
   - Medium'da Odoo makaleleri
   - Kişisel blog'lar

---

## 🎯 Öğrenme Planı (4 Hafta)

### Hafta 1: Temel Kullanım
- [ ] Odoo arayüzünü keşfet
- [ ] CRM modülünü yükle ve kullan
- [ ] Sales modülünü yükle ve ilk satış yap
- [ ] Inventory ile stok yönetimini öğren

### Hafta 2: İleri Seviye Kullanım
- [ ] Accounting modülünü öğren
- [ ] Project modülü ile proje yönetimi
- [ ] Raporları keşfet
- [ ] Email entegrasyonu

### Hafta 3: Özelleştirme
- [ ] Developer mode'u aktifleştir
- [ ] View'ları incele
- [ ] Studio ile basit özelleştirmeler yap
- [ ] Automated actions oluştur

### Hafta 4: Modül Geliştirme
- [ ] Python ve XML temelleri
- [ ] İlk modülünü oluştur
- [ ] Model, view, action kavramları
- [ ] Modülünü test et ve yükle

---

## 💡 İpuçları

### Genel İpuçları
1. **Demo Data Kullanın**: İlk kurulumda demo data'yı aktif edin, örneklerle öğrenmek daha kolay
2. **Developer Mode**: Öğrenme sürecinde developer mode'u açık tutun
3. **Yedek Alın**: Denemeler yaparken düzenli yedek alın
4. **Dökümanları Okuyun**: Resmi dökümanlar çok kapsamlı ve güncel

### Geliştirme İpuçları
1. **Küçük Başlayın**: İlk modülünüz basit olsun
2. **Mevcut Modülleri İnceleyin**: Odoo'nun kendi modüllerini örnek alın
3. **Log Kullanın**: `_logger.info()` ile debug yapın
4. **Test Edin**: Her değişiklikten sonra test edin

---

## 🚀 Sonraki Adımlar

1. **İlk modülünüzü yükleyin**: Sales veya CRM ile başlayın
2. **Pratik yapın**: Gerçek senaryolar oluşturun
3. **Toplulukla etkileşime geçin**: Forum'larda sorular sorun
4. **Kendi modülünüzü geliştirin**: Öğrendiklerinizi uygulayın

---

**Başarılar! 🎉**

Sorularınız olursa çekinmeden sorun!
