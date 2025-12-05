# 🏗️ Odoo Estate Modülü - Mimari Diyagram

Bu dokümanda Estate modülünün tüm bileşenleri ve aralarındaki bağlantılar görsel olarak açıklanmıştır.

---

## 📁 1. Dosya Yapısı ve Bağlantılar

```mermaid
graph TD
    A[estate/] --> B[__init__.py]
    A --> C[__manifest__.py]
    A --> D[models/]
    A --> E[views/]
    A --> F[security/]
    
    B --> B1["from . import models"]
    
    C --> C1[data: security/ir.model.access.csv]
    C --> C2[data: views/estate_property_views.xml]
    C --> C3[data: views/property_type_views.xml]
    
    D --> D1[__init__.py]
    D --> D2[estate_property.py]
    D --> D3[property_type.py]
    
    D1 --> D1A["from . import estate_property"]
    D1 --> D1B["from . import property_type"]
    
    E --> E1[estate_property_views.xml]
    E --> E2[property_type_views.xml]
    
    F --> F1[ir.model.access.csv]
    
    style A fill:#e1f5ff
    style C fill:#fff3cd
    style D fill:#d4edda
    style E fill:#f8d7da
    style F fill:#d1ecf1
```

---

## 🎯 2. Python Class'lar ve İlişkileri

```mermaid
classDiagram
    class EstateProperty {
        +String _name = "estate.property"
        +String _description
        +Char name
        +Text description
        +Char postcode
        +Date date_availability
        +Float expected_price
        +Float selling_price
        +Integer bedrooms
        +Integer living_area
        +Integer facades
        +Selection toilets
        +Boolean garage
        +Boolean garden
        +Integer garden_area
        +Selection garden_orientation
        +Many2one property_type_id
    }
    
    class PropertyType {
        +String _name = "estate.property.type"
        +String _description
        +Char name
    }
    
    EstateProperty --> PropertyType : Many2one\nproperty_type_id
    
    note for EstateProperty "Dosya: models/estate_property.py\nTablo: estate_property"
    note for PropertyType "Dosya: models/property_type.py\nTablo: estate_property_type"
```

---

## 🗄️ 3. Veritabanı Tabloları ve İlişkiler

```mermaid
erDiagram
    ESTATE_PROPERTY ||--o{ ESTATE_PROPERTY_TYPE : "property_type_id (FK)"
    
    ESTATE_PROPERTY {
        int id PK
        varchar name
        text description
        varchar postcode
        date date_availability
        float expected_price
        float selling_price
        int bedrooms
        int living_area
        int facades
        varchar toilets
        boolean garage
        boolean garden
        int garden_area
        varchar garden_orientation
        int property_type_id FK
    }
    
    ESTATE_PROPERTY_TYPE {
        int id PK
        varchar name
    }
```

**Açıklama:**
- `ESTATE_PROPERTY.property_type_id` → `ESTATE_PROPERTY_TYPE.id` (Foreign Key)
- Bir Property Type'a birçok Property bağlı olabilir (One-to-Many)
- Her Property'nin bir Property Type'ı vardır (Many-to-One)

---

## 📋 4. XML View Records ve Bağlantıları

### estate_property_views.xml

```mermaid
graph LR
    A[estate_property_views.xml] --> B[Search View]
    A --> C[List View]
    A --> D[Form View]
    A --> E[Action]
    A --> F[Menu]
    
    B --> B1["id: view_estate_property_search"]
    B --> B2["model: estate.property"]
    B --> B3["Arama alanları + Filtreler"]
    
    C --> C1["id: view_estate_property_tree"]
    C --> C2["model: estate.property"]
    C --> C3["Tablo sütunları"]
    
    D --> D1["id: view_estate_property_form"]
    D --> D2["model: estate.property"]
    D --> D3["Form layout + Fields"]
    
    E --> E1["id: action_estate_property"]
    E --> E2["res_model: estate.property"]
    E --> E3["view_mode: list,form"]
    
    F --> F1["id: menu_estate_root"]
    F --> F2["id: menu_estate_property"]
    F2 --> F2A["parent: menu_estate_root"]
    F2 --> F2B["action: action_estate_property"]
    
    style A fill:#f8d7da
    style E fill:#fff3cd
    style F fill:#d4edda
```

### property_type_views.xml

```mermaid
graph LR
    A[property_type_views.xml] --> B[Action]
    A --> C[Menu]
    
    B --> B1["id: action_estate_property_type"]
    B --> B2["res_model: estate.property.type"]
    B --> B3["view_mode: list,form"]
    
    C --> C1["id: menu_estate_property_type"]
    C --> C2["parent: menu_estate_root"]
    C --> C3["action: action_estate_property_type"]
    
    style A fill:#f8d7da
    style B fill:#fff3cd
    style C fill:#d4edda
```

---

## 🎭 5. Model-View-Controller (MVC) Akışı

```mermaid
sequenceDiagram
    participant U as Kullanıcı
    participant M as Menu
    participant A as Action
    participant V as View
    participant C as Controller
    participant D as Database
    
    U->>M: Real Estate → Properties tıklar
    M->>A: action_estate_property çalıştır
    A->>C: estate.property modelini aç
    C->>D: SELECT * FROM estate_property
    D->>C: Kayıtları döndür
    C->>V: List View'ı render et
    V->>U: Tablo görünümü göster
    
    U->>V: Bir kayda tıklar
    V->>A: Form View'ı aç
    A->>C: Kayıt ID'si ile veri iste
    C->>D: SELECT * WHERE id=X
    D->>C: Kayıt detayı döndür
    C->>V: Form View'ı render et
    V->>U: Detay sayfası göster
```

---

## 🔗 6. Many2one İlişkisi Detaylı

```mermaid
graph TD
    subgraph "Property Form View"
        A[property_type_id field]
    end
    
    subgraph "Python Model"
        B["fields.Many2one('estate.property.type')"]
    end
    
    subgraph "Database"
        C[property_type_id column]
        D[Foreign Key → estate_property_type.id]
    end
    
    subgraph "Property Type Records"
        E[ID: 1, Name: Villa]
        F[ID: 2, Name: Daire]
        G[ID: 3, Name: Arsa]
    end
    
    A --> B
    B --> C
    C --> D
    D --> E
    D --> F
    D --> G
    
    style A fill:#e1f5ff
    style B fill:#d4edda
    style C fill:#fff3cd
    style E fill:#f8d7da
    style F fill:#f8d7da
    style G fill:#f8d7da
```

**Kullanıcı Perspektifi:**
```
Form'da görünen:
┌─────────────────┐
│ Mülk Tipi       │
│ [Villa ▼]       │ ← Dropdown
│   - Villa       │
│   - Daire       │
│   - Arsa        │
└─────────────────┘

Veritabanında saklanan:
property_type_id = 1 (Villa'nın ID'si)
```

---

## 🌳 7. Menu Hiyerarşisi

```mermaid
graph TD
    A[Odoo Ana Menü] --> B[Real Estate]
    B --> C[Properties]
    B --> D[Property Types]
    
    C --> C1["Action: action_estate_property"]
    C1 --> C2["Model: estate.property"]
    C2 --> C3["Views: List, Form, Search"]
    
    D --> D1["Action: action_estate_property_type"]
    D1 --> D2["Model: estate.property.type"]
    D2 --> D3["Views: List, Form (otomatik)"]
    
    style A fill:#e1f5ff
    style B fill:#d4edda
    style C fill:#fff3cd
    style D fill:#fff3cd
```

**Ekranda Görünüm:**
```
┌────────────────────────────────────┐
│ [Logo] Real Estate ▼  Discuss ...  │ ← Üst Navbar
├────────────────────────────────────┤
│        ↓ Dropdown                  │
│     ┌──────────────┐               │
│     │ Properties   │ ← Tıklayınca list view
│     │ Property Types│ ← Tıklayınca list view
│     └──────────────┘               │
└────────────────────────────────────┘
```

---

## 🔄 8. Veri Akışı: Kayıt Oluşturma

```mermaid
sequenceDiagram
    participant U as Kullanıcı
    participant F as Form View
    participant M as Model (Python)
    participant D as Database
    
    U->>F: "New" butonuna tıklar
    F->>U: Boş form gösterir
    
    U->>F: Alanları doldurur
    Note over U,F: name: "Lüks Villa"<br/>property_type_id: Villa (ID=1)<br/>expected_price: 15000000
    
    U->>F: "Save" butonuna tıklar
    F->>M: create() method çağrılır
    M->>M: Field validasyonları
    M->>D: INSERT INTO estate_property
    Note over M,D: name='Lüks Villa'<br/>property_type_id=1<br/>expected_price=15000000
    
    D->>M: Yeni kayıt ID'si (örn: 5)
    M->>F: Kayıt başarılı
    F->>U: Form view (edit mode)
```

---

## 📊 9. Security (Erişim Hakları) Akışı

```mermaid
graph TD
    A[Kullanıcı] --> B{Giriş Yapmış mı?}
    B -->|Hayır| C[Login Sayfası]
    B -->|Evet| D{base.group_user üyesi mi?}
    
    D -->|Hayır| E[Erişim Reddedildi]
    D -->|Evet| F[ir.model.access.csv kontrol]
    
    F --> G{estate.property için izin var mı?}
    G -->|Hayır| E
    G -->|Evet| H[Model'e Erişim İzni]
    
    H --> I{Ne yapmak istiyor?}
    I -->|Okuma| J{perm_read=1?}
    I -->|Yazma| K{perm_write=1?}
    I -->|Oluşturma| L{perm_create=1?}
    I -->|Silme| M{perm_unlink=1?}
    
    J -->|Evet| N[İşlem İzin Verildi]
    K -->|Evet| N
    L -->|Evet| N
    M -->|Evet| N
    
    J -->|Hayır| E
    K -->|Hayır| E
    L -->|Hayır| E
    M -->|Hayır| E
    
    style A fill:#e1f5ff
    style E fill:#f8d7da
    style N fill:#d4edda
```

---

## 🎯 10. Tam Sistem Bağlantı Diyagramı

```mermaid
graph TB
    subgraph "Dosya Sistemi"
        A[__manifest__.py]
        B[models/__init__.py]
        C[models/estate_property.py]
        D[models/property_type.py]
        E[views/estate_property_views.xml]
        F[views/property_type_views.xml]
        G[security/ir.model.access.csv]
    end
    
    subgraph "Python Runtime"
        H[EstateProperty Class]
        I[PropertyType Class]
    end
    
    subgraph "Odoo ORM"
        J[Model Registry]
        K[Field Definitions]
    end
    
    subgraph "Database"
        L[estate_property table]
        M[estate_property_type table]
        N[ir_ui_view table]
        O[ir_actions_act_window table]
        P[ir_ui_menu table]
        Q[ir_model_access table]
    end
    
    subgraph "Web Interface"
        R[Menu Bar]
        S[List View]
        T[Form View]
        U[Search View]
    end
    
    A -->|loads| B
    A -->|loads| E
    A -->|loads| F
    A -->|loads| G
    
    B -->|imports| C
    B -->|imports| D
    
    C -->|defines| H
    D -->|defines| I
    
    H -->|registers in| J
    I -->|registers in| J
    
    H -->|creates| L
    I -->|creates| M
    
    E -->|creates records in| N
    E -->|creates records in| O
    E -->|creates records in| P
    
    F -->|creates records in| N
    F -->|creates records in| O
    F -->|creates records in| P
    
    G -->|creates records in| Q
    
    J -->|queries| L
    J -->|queries| M
    
    R -->|reads from| P
    R -->|triggers| O
    
    O -->|renders| S
    O -->|renders| T
    
    N -->|defines| S
    N -->|defines| T
    N -->|defines| U
    
    L -.->|FK| M
    
    style A fill:#fff3cd
    style H fill:#d4edda
    style L fill:#e1f5ff
    style R fill:#f8d7da
```

---

## 📝 11. Özet: Her Şey Nasıl Bağlı?

### Adım Adım Akış:

1. **Modül Yükleme:**
   - `__manifest__.py` → Odoo'ya modülü tanıtır
   - `data` listesi → Hangi dosyaların yükleneceğini belirtir

2. **Python Kodları:**
   - `models/__init__.py` → Python dosyalarını import eder
   - `estate_property.py` → `EstateProperty` class'ını tanımlar
   - `property_type.py` → `PropertyType` class'ını tanımlar

3. **ORM (Object-Relational Mapping):**
   - Class'lar → Veritabanı tablolarına dönüşür
   - Field'lar → Tablo sütunlarına dönüşür
   - Many2one → Foreign key ilişkisi oluşturur

4. **XML View'lar:**
   - View record'ları → `ir_ui_view` tablosuna kaydedilir
   - Action record'ları → `ir_actions_act_window` tablosuna kaydedilir
   - Menu record'ları → `ir_ui_menu` tablosuna kaydedilir

5. **Security:**
   - CSV dosyası → `ir_model_access` tablosuna kaydedilir
   - Kullanıcı erişimlerini kontrol eder

6. **Web Arayüzü:**
   - Kullanıcı menüye tıklar
   - Action çalışır
   - View render edilir
   - Database'den veri çekilir
   - Kullanıcıya gösterilir

---

## 🎓 Anahtar Kavramlar

| Kavram | Açıklama | Örnek |
|--------|----------|-------|
| **Model** | Python class, veritabanı tablosu | `EstateProperty` |
| **Field** | Model özelliği, tablo sütunu | `name`, `price` |
| **Many2one** | Çoktan bire ilişki, foreign key | `property_type_id` |
| **View** | Kullanıcı arayüzü tanımı | List, Form, Search |
| **Record** | XML'de tanımlanan kayıt | `<record id="...">` |
| **Action** | View'ları açan tetikleyici | `action_estate_property` |
| **Menu** | Navigasyon öğesi | Real Estate → Properties |

---

**Artık her şeyin nasıl bağlı olduğunu görüyorsunuz! 🎉**
