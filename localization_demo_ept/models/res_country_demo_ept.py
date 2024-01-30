from odoo import fields, models


class ResCountryDemoEpt(models.Model):
    _name = 'res.country.demo.ept'
    _description = 'Res Country Demo Ept'

    name = fields.Char(string='Name', help='name of the country')
    code = fields.Char(string='Code', help='Code of the country')
    active = fields.Boolean(string='Active', default=True, help='Is contact Active?')
