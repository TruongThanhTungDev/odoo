{
    'name': "Hospital management",
    'author': "TungTT",
    'category': 'Category',
    'description': "Run demo odoo",
    'summary' : 'Run demo odoo',
    'website' : 'www.google.com',
    # data files always loaded at installation
    'data': [
        # 'views/views.xml',
        'views/menu.xml',
        'views/patient.xml',
        'security/ir.model.access.csv',
    ],
    # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
}