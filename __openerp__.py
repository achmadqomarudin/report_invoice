{
    'name': 'Report Invoice Odoo 9',
    'version': '1.0',
    'author': 'Achmad Qomarudin',
    'website': 'http://www.amatirzoneblog.wordpress.com',
    'category': 'Custom Module',
    'sequence': 1,
    'summary': ' ',
    'description': '''
            Report Invoice Odoo 9
    ''',
    'demo': [],
    'data': [
            'view_report_invoice.xml',
    ],
    'test': [],
    'depends': ['base', 'sale', 'account', 'mrp'],

    'auto_install': False,
    'installable': True,
    'application': False,
}
