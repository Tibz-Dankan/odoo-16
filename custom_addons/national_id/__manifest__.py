{
    'name': 'National ID Application',
    'author': 'Tibesigwa Dankan',
    'version': '1.2',
    'category': 'Services/national_id',
    'sequence': 10,
    'summary': 'National ID Registration',
    'website': 'https://www.odoo.com/app/national_id_application',
    'license': 'LGPL-3',
      'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/application.xml'
      ]
    ,
    'assets': {
        'web.assets_backend': [
            'national_id/static/src/css/progress_bar.css',
            'national_id/static/src/js/progress_bar.js',
        ],
    },
}