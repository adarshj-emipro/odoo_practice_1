from odoo import models, fields


class ResPartnerDemoEPT2(models.Model):
    _name = 'res.partner.demo.ept2'
    _description = 'Res Partner Demo Ept2'

    name = fields.Char(string='name', help='Name of the contact')
    email = fields.Char(string='email', help='Email of the contact')
    street1 = fields.Char(string='street1', help='street1 address of the contact')
    street2 = fields.Char(string='street2', help='street2 address of the contact')
    city = fields.Char(string='city', help='city of the contact')
    state = fields.Char(string='state', help='state of the contact')
    zip_code = fields.Char(string='zip_code', help='zip code of the contact')
    country = fields.Char(string='country', help='country of the contact')
    birthdate = fields.Date(string='birthdate', help='birth date of the contact')
    age = fields.Integer(string='age', help='age of the contact')
    weight = fields.Float(string='weight', help='weight of the contact')
    description = fields.Text(string='description', help='description about the contact')
    gender = fields.Selection(string='gender',
                              selection=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')],
                              help='gender of the contact')
    details = fields.Html(string='details', help='details of the contact')
    is_spectacles = fields.Boolean(strin='is_spectacles', help='Do contact wears spectacles')
    photo = fields.Image(string='photo', help='Image of the contact')
