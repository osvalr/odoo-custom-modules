# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage Trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "osvalr",

    'website': "vauxoo.com",

    'category': 'OpenAcademy',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        "view/openacademy_course_view.xml",
        "view/openacademy_session_view.xml",
        "view/partner.xml",
        "view/openacademy_session_workflow.xml",
        "security/security.xml",
        "security/ir.model.access.csv",
        "view/openacademy_wizard_view.xml",
        "report/openacademy_session_report.xml",
        "view/openacademy_session_board.xml",
    ],

    'demo': [
        "demo/openacademy_course_demo.xml",
        "demo/partner_demo.xml"
    ],
    'test':[
        'tests/openacademy_course.yml',
        'tests/openacademy_session.yml',
    ],
    'installable': True,
    'auto_install': False,
}
