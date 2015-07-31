from datetime import timedelta
from openerp import _, api, fields, models

"""
    OpenAcademy session module
"""


class Session(models.Model):
    _name = "openacademy.session"

    name = fields.Char(required=True)

    start_date = fields.Date(default=fields.Date.today)

    end_date  = fields.Date(string="End Date", store=True,
        compute='_get_end_date', inverse='_set_end_date' )

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

    @api.one
    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        if self.instructor_id and self.instructor_id in self.attendee_ids:
            raise exception.ValidationError(_("A session's instructor can't be an attendee"))

    @api.one
    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        if not (self.start_date and self.duration):
            self.end_date = self.start_date
            return

        # Add duration to start_date, but: Monday + 5 days = Saturday, so
        # subtract one second to get on Friday instead
        start = fields.Datetime.from_string(self.start_date)
        duration = timedelta(days=self.duration, seconds=-1)
        self.end_date = start + duration

    @api.one
    def _set_end_date(self):
        if not (self.start_date and self.end_date):
            return

        # Compute the difference between dates, but: Friday - Monday = 4 days,
        # so add one day to get 5 days instead
        start_date = fields.Datetime.from_string(self.start_date)
        end_date = fields.Datetime.from_string(self.end_date)
        self.duration = (end_date - start_date).days + 1

    state = fields.Selection([
         ('draft', "Draft"),
         ('confirmed', "Confirmed"),
         ('done', "Done"),
    ], default='draft')

    @api.one
    def action_draft(self):
        self.state = 'draft'

    @api.one
    def action_confirm(self):
        self.state = 'confirmed'

    @api.one
    def action_done(self):
        self.state = 'done'