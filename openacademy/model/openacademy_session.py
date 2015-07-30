from openerp import _, api, fields, models

"""
    OpenAcademy session module
"""


class Session(models.Model):
    _name = "openacademy.session"

    name = fields.Char(required=True)

    start_date = fields.Date(default=fields.Date.today)

    duration = fields.Float(digits=(6, 2), help= "Duration in Days")

    seats = fields.Integer(string="Number of seats")

    active = fields.Boolean(default=True)

    instructor_id = fields.Many2one('res.partner', string="Instructor",
        domain=['|',
                ('instructor', '=', True),
                ('category_id.name','ilike','Teacher')])

    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string='Course', required=True)

    attendee_ids = fields.Many2many('res.partner', string='Attendees')

    taken_seats = fields.Float(string="Taken seats", compute="_taken_seats")

    @api.one
    @api.depends('seats','attendee_ids')
    def _taken_seats(self):
        if not self.seats:
            self.taken_seats = .0
        else:
            self.taken_seats = 100.0 * len(self.attendee_ids)/self.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0 :
            return {
                'warning':{
                    'title' : _("Incorrect 'seats' value"),
                    'message' : _("The number of available seats may not be negative"),
                }
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning' : {
                    'title' : _("Too many attendess"),
                    'message' : _("Increase seats or remove excess attendees"),
                }
            }
