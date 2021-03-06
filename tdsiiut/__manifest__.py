# -*- coding: utf-8 -*-
{
    'name': "tdsimodel",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "teamDSI",
    'website': "http://www.team-dsi.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/iut_it_schedule_views.xml',
        'views/iut_it_respartner_views.xml',
        'views/iut_it_course_views.xml',
        'views/iut_it_student_views.xml',
        'views/iut_it_class_views.xml',
        'views/iut_it_menu_views.xml',
        'security/ir.model.access.csv',    
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}