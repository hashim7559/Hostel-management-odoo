from odoo import fields,models

class HostelStudent(models.Model):
    _name="hostel.student"
    _description = "Hostel Student"
    _rec_name = 'student_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    INVOICE_STATUS = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    ]

    student_name = fields.Char(string="Student Name")
    student_email = fields.Char(string="Student Email")
    student_phone = fields.Integer(string="Student Phone")
    student_address = fields.Text(string="Student Address")
    student_code = fields.Integer(string="Student Code")
    student_dob = fields.Datetime( string="Student DOB")
    student_age = fields.Integer( string="Student Age")
    room_id = fields.Many2one("hostel.room", string="Room")
    invoice_status = fields.Selection(selection=INVOICE_STATUS,string="Invoice Status")

