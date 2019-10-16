# -*- coding: utf-8 -*-
{
    'name': " Yuemei FIT",

    'summary': """
       Yuemei FIT""",

    'description': """
        FIT
    """,

    'author': "Bunny",
    'website': "https://bunny.com",

    'category': 'CRM',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr', 'sale', 'purchase', 'project', 'fleet'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',


        'views/menu.xml',
        'views/fit_view.xml',
        'views/partner_view.xml',
        'views/res_air_plan_view.xml',
        'views/hotel_view.xml',


    ],
}
