{
    'name': 'Employee EPT',
    'version': '1.0',
    'sequence': -4,
    'summary': 'Practice Module',
    'author': 'Adarsh Jaiswal',
    'description': 'This module is for practice purpose only!!',
    'depends': ['sales_team'],
    'data': [
        'security/employee_demo_ept_security.xml',
        'security/ir.model.access.csv',
        'views/employee_demo_ept_views.xml',
    ],
    'application': True
}
