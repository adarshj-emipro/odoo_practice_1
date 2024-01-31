{
    'name':'Localization Demo EPT',
    'version':'1.0',
    'sequence':-2,
    'author':'Adarsh Jaiswal',
    'summary':'Practice Module',
    'description':'This is a practice module!!',
    'depends':['sales_team'],
    'data':[
        'security/ir.model.access.csv',
        'views/res_country_demo_ept_views.xml',
        'views/res_state_demo_ept_views.xml',
        'views/res_city_demo_ept_view.xml',
        'data/res_country_demo_ept_demo.xml',
        'data/res_state_demo_ept_demo.xml',
        'data/res_city_demo_ept_demo.xml',
    ],
    'application':True
}