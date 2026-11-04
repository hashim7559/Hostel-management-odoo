from odoo import fields, models

class HostelFacility(models.Model):
    _name = 'hostel.facility'
    _description = 'Hostel Facility'
    _rec_name = 'facility_name'

    facility_name=fields.Char(string="Facility Name")
    monthly_charge = fields.Float(string="Monthly Charge")