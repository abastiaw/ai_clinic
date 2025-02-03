from odoo import api,fields,models

class aiPatients(models.Model):
    _name = 'ai_clinic.ai_patients'
    _description = 'Patient Clinic'
    _rec_name = 'name'

    name = fields.Char(string='Nama Lengkap', required=True)
    image = fields.Image('Foto')
    dob = fields.Date(string='Tanggal Lahir')
    gender = fields.Selection([('male', 'Laki-laki'), ('female', 'Perempuan')], string='Jenis Kelamin')
    address = fields.Text(string='Alamat')
    phone = fields.Char(string='Nomor Telepon')
    email = fields.Char(string='Email')
    emergency_contact = fields.Char(string='Kontak Darurat')
    blood_type = fields.Selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], string='Golongan Darah')
    marital_status = fields.Selection([('single', 'Single'), ('married', 'Menikah'), ('duda', 'Duda'), ('janda', 'Janda')], string='Status Pernikahan')
    nationality = fields.Char(string='Kewarganegaraan')
    occupation = fields.Char(string='Pekerjaan')
    insurance_provider = fields.Char(string='Penyedia Asuransi')
    insurance_number = fields.Char(string='Nomor Asuransi')
    created_date = fields.Datetime(string='Tanggal Pendaftaran', default=lambda self: fields.Datetime.now())
    doctors_ids = fields.Many2many('ai_clinic.ai_doctors', string='Dokter')
    medical_records_ids = fields.One2many('ai_clinic.ai_patients_medical_records', 'patient_id', string='Rekam Medis')
    
    