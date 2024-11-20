from odoo import api,models,fields
from datetime import date

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True,)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', tracking=True)
    contact = fields.Char(string='Contact', tracking=True)
    ref = fields.Char(string='Reference', default='patients', tracking=True)
    active = fields.Boolean('Active', default=True)
    date_of_birth = fields.Date(string='Date of Birth', tracking=True)
    appointment_id = fields.Many2one('hospital.appointment', string='Appointments')


    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0


