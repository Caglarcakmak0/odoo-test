# Odoo Real Estate Management

A comprehensive Real Estate Management module for Odoo, providing property management, offers tracking, and accounting integration.

## 📋 Modules

### Estate (`estate`)
Core real estate management module with the following features:
- **Property Management**: Create and manage real estate properties
- **Property Types**: Categorize properties (House, Apartment, Land, etc.)
- **Property Tags**: Tag properties with custom attributes
- **Offers Management**: Track and manage property offers
- **User Integration**: Link properties to sales users

### Estate Account (`estate_account`)
Accounting integration for the Real Estate module:
- Automatic invoice generation when property is sold
- Integration with Odoo Accounting module
- Financial tracking for real estate transactions

## 🚀 Quick Start

### Prerequisites
- Odoo 17.0 or higher
- PostgreSQL 12+
- Python 3.8+

### Installation

#### Option 1: Odoo.sh (Cloud)
1. Fork this repository to your GitHub account
2. Create a new project on [Odoo.sh](https://www.odoo.sh)
3. Connect your GitHub repository
4. Deploy automatically

#### Option 2: Docker (Local Development)
```bash
# Clone the repository
git clone https://github.com/Caglarcakmak0/odoo-test.git
cd odoo-test

# Start Odoo with Docker
docker-compose up -d

# Access Odoo
# Open http://localhost:8069 in your browser
```

#### Option 3: Manual Installation
```bash
# Clone the repository
git clone https://github.com/Caglarcakmak0/odoo-test.git

# Add to Odoo addons path
# Edit your odoo.conf:
# addons_path = /path/to/odoo-test,...

# Restart Odoo
odoo -c odoo.conf
```

### Module Installation
1. Login to your Odoo instance
2. Go to **Apps** menu
3. Click **Update Apps List**
4. Search for "Real Estate"
5. Click **Install**

## 📚 Features

### Property Management
- Create and edit properties with detailed information
- Set property type, tags, and pricing
- Track property status (New, Offer Received, Offer Accepted, Sold, Canceled)
- Manage expected price and selling price
- Add property descriptions and specifications

### Offers System
- Receive and manage property offers
- Accept or refuse offers
- Track offer validity period
- Link offers to partners (buyers)
- Automatic status updates

### Accounting Integration
- Automatic invoice creation on property sale
- Integration with Odoo's accounting module
- Financial reporting for real estate transactions

## 🛠️ Development

### Module Structure
```
estate/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── estate_property.py
│   ├── estate_property_offer.py
│   ├── property_type.py
│   ├── property_tag.py
│   └── res_users.py
├── views/
│   ├── estate_property_views.xml
│   ├── property_type_views.xml
│   ├── property_tag_views.xml
│   └── res_users_views.xml
└── security/
    └── ir.model.access.csv

estate_account/
├── __init__.py
├── __manifest__.py
└── models/
    ├── __init__.py
    └── estate_property.py
```

### Running Tests
```bash
# Run module tests
odoo -c odoo.conf -u estate --test-enable --stop-after-init
```

### Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📖 Documentation

### Models

#### `estate.property`
Main property model with fields:
- `name`: Property name
- `description`: Property description
- `postcode`: Property postcode
- `date_availability`: Available from date
- `expected_price`: Expected selling price
- `selling_price`: Actual selling price
- `bedrooms`: Number of bedrooms
- `living_area`: Living area in sqm
- `facades`: Number of facades
- `garage`: Has garage (boolean)
- `garden`: Has garden (boolean)
- `garden_area`: Garden area in sqm
- `garden_orientation`: Garden orientation (North, South, East, West)
- `state`: Property state (New, Offer Received, Offer Accepted, Sold, Canceled)

#### `estate.property.offer`
Property offer model with fields:
- `price`: Offer price
- `status`: Offer status (Accepted, Refused)
- `partner_id`: Buyer (partner)
- `property_id`: Related property
- `validity`: Offer validity in days
- `date_deadline`: Offer deadline

#### `estate.property.type`
Property type categorization:
- `name`: Type name (House, Apartment, etc.)
- `property_ids`: Related properties

#### `estate.property.tag`
Property tags for custom attributes:
- `name`: Tag name
- `color`: Tag color

## 🔧 Configuration

### Security
Access rights are defined in `security/ir.model.access.csv`:
- All authenticated users can read, write, create, and delete properties
- Same permissions for property types, tags, and offers

### Dependencies
- `base`: Odoo base module
- `account`: Odoo accounting module (for estate_account)

## 📝 License

This project is licensed under the LGPL-3 License.

## 🤝 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Contact: [Your Contact Information]

## 🎯 Roadmap

- [ ] Add property images gallery
- [ ] Implement property search filters
- [ ] Add property comparison feature
- [ ] Create property reports
- [ ] Add email notifications for offers
- [ ] Implement property booking system

## 📊 Screenshots

*Coming soon*

## 🌟 Acknowledgments

Built with [Odoo](https://www.odoo.com) - Open Source ERP and CRM

---

**Version**: 1.0  
**Odoo Version**: 17.0  
**Author**: Your Name  
**Repository**: https://github.com/Caglarcakmak0/odoo-test
