# -*- coding: utf-8 -*-
from openerp import api
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

    hair = fields.Selection([("Black", "Black"), ("Brown", "Brown"), ("Other", "Other")], string="Hair",
                            default=None)  # http://redmine.kostik.net/redmine/issues/407
    eyes = fields.Selection([("Black", "Black"), ("Brown", "Brown"), ("Blue", "Blue"), ("Other", "Other")],
                            string="Eyes", default=None)  # http://redmine.kostik.net/redmine/issues/408
    height = fields.Integer('Height', help="cm")  # http://redmine.kostik.net/redmine/issues/409
    weight = fields.Integer('Weight', help="lbs")  # http://redmine.kostik.net/redmine/issues/409

    race = fields.Selection(RACE_CHOICES, string="Race", default=10)
    religion = fields.Selection(RELIGION_CHOICES, string="Religion", default=10)

    salary_rate_id = fields.Many2one("hr.salary_rate", "Salary rate")

    identification_id = fields.Char(string="NRC Number", help="up to 30 characters", size=30)
    qualification = fields.Char("Qualification")

    place_of_birth_id = fields.Many2one("hr.birth_place", "Place of birth")
    position_name_at_start = fields.Char("Position started", help="Position started as civil staff")
    date_started = fields.Date("Date started", help="Date started as civil staff")


    recommender_id = fields.Many2one('hr.recommender',
                                       string="Recommender") # Supporter for the jobs http://redmine.kostik.net/redmine/issues/417

    previous_position_and_place = fields.Char("Previous position and place")
    military_record_ids = fields.One2many('hr.military_record', 'employee_id', string="Military records")
    distinction = fields.Text("Distinction, Certification")
    criminal_records = fields.Text("Criminal records")

    fathers_name = fields.Char("Father's name")
    relative_ids = fields.One2many('hr.relative', 'employee_id', string="Relatives")

    political_activity = fields.Text(
        "Political Activity")  # Activity,Rank and Duties for Political in Student life http://redmine.kostik.net/redmine/issues/419

    recommender_ids = fields.Many2many('hr.recommender',
                                       string="Recommenders")  # Supporter Name (Headmaster, Administrator,Police Officer,Military Officer’s Name, Address (Full) http://redmine.kostik.net/redmine/issues/420
    hobby_ids = fields.Many2many('hr.hobby')
    military_colleague_ids = fields.Many2many(
        'hr.military_colleague', help="Friends list who is in the Military, Police:  their names, positions, addresses")  # Friends list who working in Military,Police and Political and their Name, Position,Address

    club_record_ids = fields.One2many('hr.club_record', 'employee_id', string="Club and Organizations")

    form2_id = fields.One2many('hr.form2', 'employee_id', string="Form 2")
    form3_id = fields.One2many('hr.form3', 'employee_id', string="Form 3")
    form4_id = fields.One2many('hr.form4', 'employee_id', string="Form 4")
    form5_id = fields.One2many('hr.form5', 'employee_id', string="Form 5")
    form6_id = fields.One2many('hr.form6', 'employee_id', string="Form 6")
    form7_id = fields.One2many('hr.form7', 'employee_id', string="Form 7")
    form8_id = fields.One2many('hr.form8', 'employee_id', string="Form 8")


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
    name = fields.Char("Name", compute='compute_name', store=True)

    position = fields.Char("Position", required=True)
    salary_from = fields.Integer("from", required=True)
    salary_step = fields.Integer("step")
    salary_to = fields.Integer("to")

    @api.depends('position', 'salary_from', 'salary_step', 'salary_to')
    def compute_name(self):
        try:
            self.name = u'{}: {}-{}-{}'.format(self.position, self.salary_from, self.salary_step, self.salary_to)
        except ValueError:
            self.name = '***'


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
            ("Child", "Child"),
            ("Sibling", "Sibling"),
            ("Spouse", "Spouse"),
            ("Spouse's Father", "Spouse's Father"),
            ("Spouse's Mother", "Spouse's Mother"),
            ("Spouse's Sibling", "Spouse's Sibling")

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
    name = fields.Char("Name", required=True)


class hr_club_record(models.Model):
    _name = "hr.club_record"
    name = fields.Char("Rank", required=True)
    club_id = fields.Many2one("hr.club", ondelete='cascade', string="Club")
    employee_id = fields.Many2one('hr.employee', ondelete='cascade', string="Employee")


class hr_hobby(models.Model):
    _name = "hr.hobby"
    name = fields.Char("Hobby", required=True)


class hr_military_colleague(models.Model):
    _name = "hr.military_colleague"
    name = fields.Char("Name", required=True)
    position = fields.Char("Position")
    address = fields.Text("Address")


class hr_recommender(models.Model):  # http://redmine.kostik.net/redmine/issues/417
    _name = "hr.recommender"
    name = fields.Char("Name", required=True)
    position = fields.Char("Position")
    address = fields.Text("Address")


class hr_form2(models.Model):
    """
    http://redmine.kostik.net/redmine/issues/361
    """
    _name = "hr.form2"
    name = fields.Char("Position", required=True)
    order_number = fields.Char("Order #")
    order_date = fields.Date("Order date")
    date = fields.Date("Effective date", required=True)
    employee_id = fields.Many2one('hr.employee', ondelete='cascade', string="Employee")
    salary_rate_id = fields.Many2one("hr.salary_rate", "Salary rate")


    image = fields.Binary('Attachment')
    image_filename = fields.Char("Attachment filename")

class hr_form3(models.Model):
    """
    http://redmine.kostik.net/redmine/issues/362
    """
    _name = "hr.form3"
    name = fields.Text("Summary")
    status = fields.Text("Status")

    order_number = fields.Char("Order #", required=True)
    order_date = fields.Date("Order date", required=True)
    employee_id = fields.Many2one('hr.employee', ondelete='cascade', string="Employee")

    image = fields.Binary('Attachment')
    image_filename = fields.Char("Attachment filename")


class hr_form4(models.Model):
    """
    http://redmine.kostik.net/redmine/issues/363
    """
    _name = "hr.form4"
    name = fields.Char("Training")
    local = fields.Selection([("Local", "Local"), ("Foreign", "Foreign")], string="Place",
                            default=None)
    duration = fields.Char("Duration")
    qualification = fields.Char("Qualification")
    employee_id = fields.Many2one('hr.employee', ondelete='cascade', string="Employee")

    image = fields.Binary('Attachment')
    image_filename = fields.Char("Attachment filename")


class hr_educational_institution(models.Model):
    """
    http://redmine.kostik.net/redmine/issues/364
    """
    _name = "hr.educational_institution"
    name = fields.Char("Name", compute="compute_name", store=True)
    educational_institution = fields.Char("Educational institution", requied=True)
    location = fields.Char("Location", requied=True)

    @api.depends('educational_institution', 'location')
    def compute_name(self):
        try:
            self.name = u'{} @ {}'.format(self.educational_institution, self.location)
        except ValueError:
            self.name = '***'


class hr_external_department(models.Model):
    """
    http://redmine.kostik.net/redmine/issues/365
    """
    _name = "hr.external_department"
    name = fields.Char("Name", compute="compute_name", store=True)
    external_department = fields.Char("Department", requied=True)
    location = fields.Char("Location", requied=True)

    @api.depends('external_department', 'location')
    def compute_name(self):
        try:
            self.name = u'{} @ {}'.format(self.external_department, self.location)
        except ValueError:
            self.name = '***'


class hr_form5(models.Model):
    """
    http://redmine.kostik.net/redmine/issues/364
    """
    _name = "hr.form5"
    name = fields.Char("Class")
    date_from = fields.Date("From")
    date_to = fields.Date("To")
    employee_id = fields.Many2one('hr.employee', ondelete='cascade', string="Employee", requied=True)
    educational_institution_id = fields.Many2one("hr.educational_institution", string="Educational institution", requied=True)


class hr_form6(models.Model):
    """
    http://redmine.kostik.net/redmine/issues/365
    """
    _name = "hr.form6"
    name = fields.Char("Position", requied=True)

    external_department_id = fields.Many2one("hr.external_department", string="Department", requied=True)
    date_from = fields.Date("From")
    date_to = fields.Date("To")
    employee_id = fields.Many2one('hr.employee', ondelete='cascade', string="Employee", requied=True)

    image = fields.Binary('Attachment')
    image_filename = fields.Char("Attachment filename")


class hr_form7(models.Model):
    """
    http://redmine.kostik.net/redmine/issues/366
    """
    _name = "hr.form7"
    name = fields.Char("Reason", requied=True)
    date_from = fields.Date("From")
    date_to = fields.Date("To")
    employee_id = fields.Many2one('hr.employee', ondelete='cascade', string="Employee", requied=True)
    country_id = fields.Many2one("res.country", requied=True)


    image = fields.Binary('Attachment')
    image_filename = fields.Char("Attachment filename")


class hr_form8(models.Model):
    """
    http://redmine.kostik.net/redmine/issues/367
    """
    _name = "hr.form8"
    name = fields.Char("Description & Remarks", requied=True)
    employee_id = fields.Many2one('hr.employee', ondelete='cascade', string="Employee", requied=True)

    image = fields.Binary('Attachment')
    image_filename = fields.Char("Attachment filename")


#class hr_inernationa_workgroup