from odoo import fields, models


class ResPartnerDemoEpt1(models.Model):
    _name = 'res.partner.demo.ept1'
    _description = 'Res Partner Demo EPT1'

    name = fields.Char(string='name', help='name of the contact')
    email = fields.Char(string='email', help='email of the contact')
    street1 = fields.Char(string='street1', help='street 1 address')
    street2 = fields.Char(string='street2', help='street2 address')
    city = fields.Char(string='city', help='city address')
    state = fields.Char(string='state', help='state address')
    zip_code = fields.Char(string='zip_code', help='zip code of the address')
    country = fields.Char(string='country', help='country address')
    birthdate = fields.Date(string='birthdate', help='birth date of the contact')
    age = fields.Integer(string='age', help='age of the contact')
    weight = fields.Float(string='weight', help='weight of the contact')
    description = fields.Text(string='description', help='description of the contact')
    gender = fields.Selection(string='gender',
                              selection=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')],
                              help='specify the gender of the contact')
    details = fields.Html(string='details', help='details about the contact')
    is_spectacles = fields.Boolean(string='is_spectacles', help='do contact wear glasses')
    photo = fields.Image(string='photo', help='Image of the contact')
