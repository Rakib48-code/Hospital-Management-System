from odoo import api,models,fields

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    contact = fields.Char(string='Contact')
    ref = fields.Char(string='Reference', default='patients')
    active = fields.Boolean('Active', default=True)
    date_of_birth = fields.Date(string='Date of Birth')
