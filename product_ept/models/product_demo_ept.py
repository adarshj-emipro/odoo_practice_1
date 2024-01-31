from odoo import fields, models


class ProductDemoEpt(models.Model):
    _name = 'product.demo.ept'
    _description = 'Product Demo Ept'

    name = fields.Char(string='Product Name', help='Name of the product')
    default_code = fields.Char(string='SKU', help='Stock Keeping Unit')
    barcode = fields.Char(string='Barcode', help='Barcode value')
    can_sold = fields.Boolean(string='Sellable', help='Can be sold or not')
    product_type = fields.Selection(string='Type', selection=[('Storable', 'Storable'), ('Consumable', 'Consumable'),
                                                              ('Service', 'Service')], help='type of product')
    sale_price = fields.Float(string='Sale Price', digits=(6, 2), help='sale price of the product')
    cost_price = fields.Float(string='Cost Price', digits=(6, 2), help='Cost price of the product')
    active = fields.Boolean(string='Active', default=True, help='Active Record??')
    warehouse = fields.Char(string='Warehouse', help='Warehouse Name')
    product_image = fields.Image(string='Product Image', help='products image')
    website_description = fields.Html(string='Website Description', help='About the website')
    internal_note = fields.Text(string='Internal Note', help='Internal Notes')
