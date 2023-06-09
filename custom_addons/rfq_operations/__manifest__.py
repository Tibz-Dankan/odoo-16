# rfq_operations/__manifest__.py

{
    'name': 'RFQ Operations',
    'version': '1.0',
    'category': 'Purchases',
    'summary': 'Adds the ability to assign RFQ to several vendors',
    'author': 'Tibesigwa Dankan',
    'depends': ['purchase'],
    'website': 'https://www.odoo.com/app/rfq_operations',
    'license': 'LGPL-3',
    'data': [
         'security/ir.model.access.csv',
        'views/menu.xml',
        'views/rfq_assign.xml',
    ],
    'installable': True,
    'application': False,
}
