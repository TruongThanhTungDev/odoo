{
    'name': "School management",
    'author': "TungTT",
    'category': 'Management',
    'description': "Quản lý trường học",
    'summary' : 'Quản lý trường học',
    'website' : 'www.google.com',
    'sequence': 10,
    # data files always loaded at installation
    'data': [
        'views/school_information.xml',
        'views/menu.xml',
        'views/student_information.xml',
        # 'views/patient.xml',
        'security/ir.model.access.csv',
    ],
    # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
    "installable": True,
    "application": True
    
}