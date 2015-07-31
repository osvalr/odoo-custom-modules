from openerp import _, exceptions, fields, models

"""
This module create model for OpenAcademy Course
"""


class Course(models.Model):
    """
    This class represents a Course for OpenAcademy module
    """

    _name = "openacademy.course"

    name = fields.Char(string=_("Title"), required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string=_("Responsible"), index=True);

    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string=_('Sessions'));

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         _("The title of the course should not be the description")),

        ('name_unique',
         'UNIQUE(name)',
         _("The course title must be unique")),
    ]
