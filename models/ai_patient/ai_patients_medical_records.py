from odoo import api,fields,models

class aiPatientsMedicalRecords(models.Model):
    _name = 'ai_clinic.ai_patients_medical_records'
    _description = 'Patiens Medical Records Clinic'
    _rec_name = 'date'

    patient_id = fields.Many2one('ai_clinic.ai_patients', string='Pasien', ondelete='cascade')
    doctor_id = fields.Many2one('ai_clinic.ai_doctors', string='Dokter', ondelete='cascade')
    date = fields.Datetime('Tanggal Pemeriksaan')
    allergies = fields.Char('Allergi')
    diagnosis = fields.Text('Diagnosa')
    treatment = fields.Text('Treatment')
    notes = fields.Text('Catatan')