{
    'name': 'Abbasy iTech Clinic',
    'author': 'Abastiaw',
    'website': '',
    'summary': 'Odoo 16 Development',
    'depends': ['base','mail'],
    'category': 'Productivity',
    'version': '0.1',
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/ai_doctors/ai_doctors.xml',
        'views/ai_patients/ai_patients.xml',
    ],
    'installable': True,
    'auto_install': False,    	
    'application': True,
}