{
    'name': 'Hospital Management System',
    'category': 'Healthcare',
    'version': '1.0',
    'sequence': '-100',
    'summary': 'Manage all hospital operations such as appointments, patient records, and medical history.',
    'description': """
        A comprehensive system for managing hospitals, including features like:
        - Patient Management
        - Appointment Scheduling
        - Medical History Tracking
        - Doctor and Nurse Scheduling
        - Pharmacy Management
        - Billing and Payments
    """,
    'author': 'Rakib Hasan',
    'depends': ['base', 'mail'],
    'data': [
        'views/hospital_menu_view.xml',
        'views/appointment_view.xml',
        'views/patient_views.xml',
        'views/female_patient_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
