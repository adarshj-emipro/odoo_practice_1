from odoo import models, fields


class CrmLeadDemoEpt(models.Model):
    _name = 'crm.lead.demo.ept'
    _description = 'Crm Lead Demo Ept'

    name = fields.Char(string='Lead Name', required=True, help='name of the Customer')
    customer_email = fields.Char(string='Email', required=True, help='email of the customer')
    customer_phone = fields.Char(string='Phone', required=True, help='Customer phone number')
    expected_revenue = fields.Float(string='Expected Revenue', digits=(6, 2), help='Expected revenue from the customer')
    salesperson = fields.Char(string='Salesperson', required=True, help='name of the salesperson')
    sales_team = fields.Char(string='Sales Team', help='Assigned Sales Team')
    campaign = fields.Char(string='Campaign', help='Campaign name')
    channel = fields.Selection(string='Channel', required=True,
                               selection=[('Facebook', 'Facebook'), ('WhatsApp', 'WhatsApp'), ('Email', 'Email'),
                                          ('Newspaper', 'Newspaper'), ('Television', 'Television'),
                                          ('Phone Call', 'Phone Call'), ('SMS', 'SMS'), ('Google Ads', 'Google Ads'), ],
                               help='channel on which campaign was seen by customer')
    state = fields.Selection(string='State', selection=[('New', 'New'), ('Qualified', 'Qualified'),
                                                        ('Proposition', 'Proposition'), ('Won', 'Won'),
                                                        ('Lost', 'Lost'), ], default='New',
                             help='State of the generated Lead')
    next_followup_date = fields.Date(string='Next Followup Date', required=True, help='next followup date')
    won_date = fields.Date(string='Won Date', help='the date when the lead is ready to buy your service')
    lost_reason = fields.Text(string='Lost Reason', help='Reason for lead lost')
