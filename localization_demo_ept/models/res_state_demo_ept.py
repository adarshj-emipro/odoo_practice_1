from odoo import fields, models


class ResStateDemoEpt(models.Model):
    _name = 'res.state.demo.ept'
    _description = 'Res State Demo Ept'

    name = fields.Char(string='State Name', help='name of the state')
    code = fields.Char(string='State Code', help='code of the state')
    country_name = fields.Char(string='Country Name', copy=True, help='Name of the country')
    active = fields.Boolean(string='Is Active', default=True, help='is record active')
