# -*- coding: utf-8 -*-
from openerp import models, fields, _

RACE_CHOICES = [
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
]

RELIGION_CHOICES = [
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
]


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

    race = fields.Selection(RACE_CHOICES, string="Race", default=10)
    religion = fields.Selection(RELIGION_CHOICES, string="Religion", default=10)

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
    fathers_name = fields.Char("Father's name")
    relative_ids = fields.One2many('hr.relative', 'employee_id', string="Relatives")

    # Activity,Rank and Duties for Political in Student life http://redmine.kostik.net/redmine/issues/419
    # Supporter Name (Headmaster, Administrator,Police Officer,Military Officer’s Name, Address (Full) http://redmine.kostik.net/redmine/issues/420
    hobby_ids = fields.Many2many('hr.hobby')
    military_colleague_ids = fields.Many2many('hr.military_colleague') # Friends list who working in Military,Police and Political and their Name, Position,Address

    club_record_ids = fields.One2many('hr.club_record', 'employee_id', string="Club and Organizations")


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


class hr_relative(models.Model):
    """
    Staff's father name	U Pyu
    Father’s Race/Religion	Burma/Buddhist
    Father’s Job	Farmer
    Father’s Address	No.24, Botahtaung Street, Botahtaung Township
    Staff's mother name	Daw Wah
    Mother’s Race/Religion	Burma/Buddhist
    Mother’s Job	Nil
    Mother’s Address	Same with father
    Name of Brother & Sisters, Their Job and Their Address	Nil
    Wife/Spouse Name	Nil
    Wife/Spouse Race/Religion	Nil
    Job title of Wife/Spouse	Nil
    Wife/Spouse Address	Nil
    Wife/Spouse's Father Name	Nil
    Wife/Spouse’s father Race/Religion	Nil
    Wife/Spouse’s father Job	Nil
    Address of Wife/Spouse's Father	Nil
    Wife/Spouse's Mother Name	Nil
    Wife/Spouse’s mother Race/Religion	Nil
    Wife/Spouse’s mother Job	Nil
    Address of Wife/Spouse's Mother	Nil
    Wife/Spouse’s brother/sister Name	Nil
    Wife/Spouse’s brother/sister Race/Religion	Nil
    Wife/Spouse’s brother/sister Job	Nil
    Staff’s Son and Daughters Nil
    (a) Name, Birthdate, NRC
    (b) Job/Address
    """

    _name = 'hr.relative'
    name = fields.Selection(
        [
            ("Father", "Father"),
            ("Mother", "Mother"),
            ("Spouse", "Spouse"),
            ("Spouse's Father", "Spouse's Father"),
            ("Spouse's Mother", "Spouse's Mother"),
            ("Child", "Child"),
            ("Sibling", "Sibling")
        ], string="Relative", required=True)

    relative_name = fields.Char("Name")
    race = fields.Selection(RACE_CHOICES, string="Race", default=10)
    religion = fields.Selection(RELIGION_CHOICES, string="Religion", default=10)
    occupation = fields.Char("Occupation")
    address = fields.Text("Address")
    note = fields.Char("Note")
    employee_id = fields.Many2one('hr.employee', ondelete='cascade', string="Employee")


class hr_club(models.Model):
    _name = "hr.club"
    name = fields.Char("Name")


class hr_club_record(models.Model):
    _name = "hr.club_record"
    name = fields.Char("Rank")
    club_id = fields.Many2one("hr.club", ondelete='cascade', string="Club")
    employee_id = fields.Many2one('hr.employee', ondelete='cascade', string="Employee")


class hr_hobby(models.Model):
    _name = "hr.hobby"
    name = fields.Char("Hobby")


class military_colleague(models.Model):
    _name = "hr.military_colleague"
    name = fields.Char("Name")
    position = fields.Char("Position")
    address = fields.Text("Address")
