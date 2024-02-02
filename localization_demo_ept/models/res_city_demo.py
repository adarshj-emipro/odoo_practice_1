from odoo import fields, models


class ResCityDemoEpt(models.Model):
    _name = 'res.city.demo.ept'
    _description = 'Res City Demo Ept'

    name = fields.Char(string='City', help='Name of the city')
    state_name = fields.Char(string='State', copy=False, help='Name of the state')
    active = fields.Boolean(string='Active', default=True, help='Is record active')
