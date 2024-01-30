from odoo import fields, models


class ResPartnerDemoEpt4(models.Model):
    _name = 'res.partner.demo.ept4'
    _description = 'Res Partner Demo Ept4'

    name = fields.Char(string='Name', help='Name of the contact')
    email = fields.Char(string='Email', help='Email of the contact')
    street1 = fields.Char(string='Street1', help='Street1 of the contact')
    street2 = fields.Char(string='Street2', help='Street2 of the contact')
    city = fields.Char(string='City', help='City of the contact')
    state = fields.Char(string='State', help='State of the contact')
    zip_code = fields.Char(string='Zip Code', help='Zip Code of the contact')
    country = fields.Char(string='Country', help='Country of the contact')
    birthdate = fields.Date(string='Birthdate', help='Birth date of the contact')
    age = fields.Integer(string='Age', help='Age of the contact')
    weight = fields.Float(string='Weight', help='Weight of the contact')
    description = fields.Text(string='Description', help='Description')
    gender = fields.Selection(string='Gender',
                              selection=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')],
                              help='Gender of the contact')
    details = fields.Html(string='Details', help='Details about the contact')
    is_spectacles = fields.Boolean(string='Wear Specs??', help='Wears glasses')
    photo = fields.Image(string='Image', help='Image of the contact')
