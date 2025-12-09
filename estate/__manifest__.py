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
        'views/property_type_views.xml',
        'views/property_tag_views.xml',
        'views/res_users_views.xml',
        ],
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
