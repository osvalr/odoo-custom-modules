from openerp import models, fields

"""
    OpenAcademy session module
"""


class Session(models.Model):
    _name = "openacademy.session"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help= "Duration in Days")
    seats = fields.Integer(string="Number of seats")
