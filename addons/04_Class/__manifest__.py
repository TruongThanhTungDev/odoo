{
    'name': "Class management",
    'author': "TungTT",
    'category': 'Management',
    'description': "Quản lý lớp học",
    'summary' : 'Quản lý lớp học',
    'website' : 'www.google.com',
    'sequence': 10,
    # data files always loaded at installation
    'data': [
        'views/class_information.xml',
        'security/ir.model.access.csv',
    ],
    # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
    "installable": True,
    "application": True
    
}