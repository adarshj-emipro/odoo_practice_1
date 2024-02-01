{
    'name':'CRM Lead Demo EPT',
    'version':'1.0',
    'author':'Adarsh Jaiswal',
    'sequence':-5,
    'summary':'CRM Practice Module',
    'description':'This module is for practice purpose only!!',
    'depends':['sales_team'],
    'data':[
        'security/crm_lead_demo_ept_rule.xml',
        'security/crm_lead_demo_ept_groups.xml',
        'security/ir.model.access.csv',
        'views/crm_lead_demo_ept_views.xml',
    ],
    'application':True
}