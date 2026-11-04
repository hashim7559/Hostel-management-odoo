from odoo import fields, models

class HostelRoom(models.Model):
    _name = "hostel.room"
    _description = "Hostel Room"
    _rec_name = 'room_number'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string="Order Reference",
        required=True,
        copy=False,
        readonly=False,
        index="trigram",
        default=lambda s: s.env._("New"),
    )
    room_number = fields.Integer(string="Room Number")
    room_type = fields.Selection(selection=[('single', 'Single'),('double', 'Double')], string="Room Type", default='single')
    bed_count = fields.Integer(string="Number of Bed")
    base_rent = fields.Integer(string="Base Rent")
    facilities_id = fields.Many2many('hostel.facility', string="Facilities")
    room_status = fields.Selection(  selection=[("empty", "Empty"),("partial", "Partial"),("full", "Full")], string="Room Status", default="empty")



