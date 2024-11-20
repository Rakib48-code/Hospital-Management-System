from odoo import api,fields,models

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    patient_id = fields.Many2one('hospital.patient', string='Patient')
