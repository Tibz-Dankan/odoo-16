# rfq_operations/__manifest__.py

{
    'name': 'RFQ Operations',
    'version': '1.0',
    'category': 'Purchases',
    'summary': 'Adds the ability to assign RFQ to several vendors',
    'author': 'Your Name',
    'depends': ['purchase'],
    'data': [
        'views/menu.xml',
        'views/rfq_operations.xml',
    ],
    'installable': True,
    'application': False,
}
