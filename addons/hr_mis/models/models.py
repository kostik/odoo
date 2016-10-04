# -*- coding: utf-8 -*-
from openerp import models, fields, _

class hr_mis(models.Model):
    """
    From 1: http://redmine.kostik.net/redmine/issues/401
    """
    _name = 'hr.employee'
    _inherit = 'hr.employee'

    personal_number = fields.Char('Personal Number', required=True, help="Personal number in the MCD")
    other_name = fields.Char('Other Name')
    distinctive_marks = fields.Char('Distinctive Marks')

    height = fields.Integer('Height', help="cm", default=0)    # http://redmine.kostik.net/redmine/issues/409
    weight = fields.Integer('Weight', help="lbs", default=0)   # http://redmine.kostik.net/redmine/issues/409

    race = fields.Selection(
        [
            (1, "Kachin"),
            (2, "Kayah"),
            (3, "Kayin"),
            (4, "Chin"),
            (5, "Bamar"),
            (6, "Mon"),
            (7, "Rakhine"),
            (8, "Shan"),
            (9, "Other Race"),
            (10, "Not stated")
        ],
        string="Race",
        default=10
    )

    religion = fields.Selection(
        [
            (1, "Buddhist"),
            (2, "Islam"),
            (3, "Christian"),
            (4, "Hindu"),
            (5, "Animist"),
            (6, "Confucion"),
            (7, "Sikh"),
            (8, "Jew"),
            (9, "Other Religion"),
            (10, "Not Stated")
        ],
        string="Religion",
        default=10
    )

    salary_rate_id = fields.Many2one("hr.salary_rate", "Salary rate")

    identification_id = fields.Char(string="NRC Number", help="1-15 characters", size=15)
    qualification = fields.Char("Qualification")

    place_of_birth_id = fields.Many2one("hr.birth_place", "Place of birth")
    position_name_at_start = fields.Char("Position started", help="Position started as civil staff")
    date_started = fields.Date("Date started", help="Date started as civil staff")

    # Supporter for the jobs http://redmine.kostik.net/redmine/issues/417
    previous_position_and_place = fields.Char("Previous position abd place")
    military_record_ids = fields.One2many('hr.military_record', 'employee_id', string="Military records")
    distinction = fields.Text("Distinction, Certification")

    #address_id = fields.many2one('res.partner', 'Current Address'),
    #address_home_id = fields.many2one('res.partner', 'Permanent Address'),


    #     name = fields.Char()
    #     value = fields.Integer()
    #     value2 = fields.Float(compute="_value_pc", store=True)
    #     description = fields.Text()
    #
    #     @api.depends('value')
    #     def _value_pc(self):
    #         self.value2 = float(self.value) / 100


class hr_birth_place(models.Model):
    """
    http://redmine.kostik.net/redmine/issues/406
    """
    _name = 'hr.birth_place'
    name = fields.Char("Birth place", required=True)

class hr_salary_rate(models.Model):
    """
    http://redmine.kostik.net/redmine/issues/403
    """
    _name = 'hr.salary_rate'
    name = fields.Char("Position", required=True)

    salary_from = fields.Integer("from", required=True)
    salary_step = fields.Integer("step")
    salary_to = fields.Integer("to")


class hr_military_record(models.Model):
    """
     If you work in Military before
     (a)Personal ID
     (b)Date of Joining and leaving from there.
     (c)Reason for leaving
     (d)Military Army name that you worked
     (e)Summary when working in Military
     (f)Pension Salary


    """

    _name = 'hr.military_record'
    name = fields.Char("Personal ID", required=True)

    date_joined = fields.Date("Date joined", required=True)
    date_resigned = fields.Date("Date resigned", required=True)
    reason_for_leaving = fields.Char("Resign reason")

    division = fields.Char("Division(s)", required=True)
    summary = fields.Text("Career Summary")

    pension = fields.Integer("Pension")

    employee_id = fields.Many2one('hr.employee', ondelete='cascade', string="Employee")
