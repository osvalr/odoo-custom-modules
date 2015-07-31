from openerp import _, exceptions, fields, models

"""
This module create model for OpenAcademy Course
"""


class Course(models.Model):
    """
    This class represents a Course for OpenAcademy module
    """

    _name = "openacademy.course"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True);

    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string='Sessions');

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]
