from odoo import fields, models


class EmployeeDemoEpt(models.Model):
    _name = 'employee.demo.ept'
    _description = 'Employee Demo Ept'

    name = fields.Char(string='Name of the Employee', help='Employee name')
    d_name = fields.Char(string='Department Name', help='Department name of the employee')
    position = fields.Char(string='Designation', help='Job position')
    salary = fields.Float(string='Salary', digits=(6, 2), help='Salary of the employee')
    hire_date = fields.Date(string='Hired Date', help='Employee hire date')
    gender = fields.Selection(string='Gender',
                              selection=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')],
                              help='gender of the employee')
    type = fields.Selection(string='Job Type', selection=[('Permanent', 'Permanent'), ('Ad Hoc', 'Ad Hoc')])
