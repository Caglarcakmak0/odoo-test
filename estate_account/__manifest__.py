{
    'name': 'Real Estate Account',
    'version': '1.0',
    'depends': ['estate', 'account'],
    'author': 'Your Name',
    'category': 'Sales',
    'description': """
    Real Estate Account Integration
    ================================
    Link module between Real Estate and Accounting.
    Creates invoices when properties are sold.
    """,
    'data': [
        # 'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
