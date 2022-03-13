# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

{
    'name': 'Employee Ratings',
    'version': '1.0',
    'summary': 'Provide features of Employee Ratings.',
    'description': """
    Provide features of Employee Ratings.
    """,
    'category': 'Human Resources/Employees',
    'author': 'Dimpal Patel',
    'website': 'pateldimpal277@gmail.com',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/email_template.xml',
        'data/cron_data.xml',
        'views/employee_views.xml',
        'views/hr_rating_views.xml',
        'views/res_users_views.xml',
        'views/assets.xml',
    ],
    'demo': [],
    'qweb': [
        "static/src/xml/suggestion.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
