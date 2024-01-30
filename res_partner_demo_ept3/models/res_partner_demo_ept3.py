from odoo import fields, models


class ResPartnerDemoEpt3(models.Model):
    _name = 'res.partner.demo.ept3'
    _description = 'Res Partner Demo Ept3'

    name = fields.Char(string='Name', help='Name of the contact')
    email = fields.Char(string='Email', help='Email of the contact')
    street1 = fields.Char(string='Street1', help='Street1 of the contact')
    street2 = fields.Char(string='Street2', help='Street2 of the contact')
    city = fields.Char(string='City', help='City of the contact')
    state = fields.Char(string='State', help='State of the contact')
    zip_code = fields.Char(string='Zip_Code', help='Zip_Code of the contact')
    country = fields.Char(string='Country', help='Country of the contact')
    birthdate = fields.Date(string='Birth Date', help='Birth date of the contact')
    age = fields.Integer(string='Age', help='Age of the contact')
    weight = fields.Float(string='Weight', help='Weight of the contact')
    description = fields.Text(string='Description', help='Description of the contact')
    gender = fields.Selection(string='Gender',
                              selection=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')],
                              help='Specify the gender of the contact')
    details = fields.Html(string='Details', help='Details about the contact')
    is_spectacles = fields.Boolean(string='Is_Spectacles', help='Don contact wears glasses')
    photo = fields.Image(string='Image', help='image of the contact')
