from openerp import fields, models
'''
This module create model for OpenAcademy Course
'''


class Course(models.Model):
    """
    This class represents a Course for OpenAcademy module
    """

    _name = "openacademy.course"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()