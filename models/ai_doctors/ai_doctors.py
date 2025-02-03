from odoo import api,fields,models

class aiDoctors(models.Model):
    _name = 'ai_clinic.ai_doctors'
    _description = 'Doctors Clinic'
    _rec_name = 'name'

    name = fields.Char(string='Nama Lengkap', required=True)
    image = fields.Image('Foto')
    dob = fields.Date(string='Tanggal Lahir')
    gender = fields.Selection([('male', 'Laki-laki'), ('female', 'Perempuan')], string='Jenis Kelamin')
    specialization = fields.Char(string='Spesialisasi')
    qualification = fields.Text(string='Kualifikasi Pendidikan')
    license_number = fields.Char(string='Nomor Izin Praktik')
    phone = fields.Char(string='Nomor Telepon')
    email = fields.Char(string='Email')
    address = fields.Text(string='Alamat')
    workplace = fields.Char(string='Tempat Praktik')
    years_of_experience = fields.Integer(string='Tahun Pengalaman')
    doctor_type = fields.Selection([('general', 'Dokter Umum'), ('specialist', 'Dokter Spesialis')], string='Jenis Dokter')
    working_hours = fields.Char(string='Jam Kerja')
    created_date = fields.Datetime(string='Tanggal Pendaftaran', default=fields.Datetime.now)
    is_active = fields.Boolean(string='Status Aktif', default=True)
    patients_ids = fields.Many2many('ai_clinic.ai_patients', string='Pasien')
    medical_records_ids = fields.One2many('ai_clinic.ai_patients_medical_records', 'doctor_id', string='History Pemeriksaan')