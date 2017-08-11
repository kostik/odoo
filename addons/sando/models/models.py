# -*- coding: utf-8 -*-
import re

from openerp import api
from openerp import fields
from openerp import models
from openerp import osv


class sando_customs_house(models.Model):
    _name = 'sando.customs_house'
    name = fields.Char(
        string="Customs House/Clearance station name/code",
        required=True
    )


class sando_offence_code(models.Model):
    _name = 'sando.offence_code'
    name = fields.Char(
        string="Offence Code",
        required=True
    )


class sando(models.Model):
    _name = 'sando.sando'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _description = "Risk record"
    _order = 'name desc'

    name = fields.Char(
        string='Serial Number',
        help='Prime key to allow the computer to link various information.'
             'If a record is deleted, the number is deleted and cannot be used again.'
             'This prevents different records from ever having the same serial number.'
             '(E.G. there will never be two records in the register with serial number 5)',
        size=10, readonly=True)

    active = fields.Boolean(
        default=True,
        track_visibility='onchange',
        help="Set active to false to hide the tax without removing it."
    )

    # category_of_case = fields.Selection(
    #     selection=[('administrative', 'Administrative'), ('criminal', 'Criminal')],
    #     track_visibility='onchange',
    #     string="Category of Case",
    #     help="This box has a drop down menu giving 2 options,"
    #          "Administrative and Criminal."
    #          "The officer should select the appropriate type from the menu",
    #     required=True
    # )

    category_id = fields.Many2many(
        'sando.category',
        string='Tags',
        column1='sando_id',
        column2='category_id',
    )

    case_number = fields.Char(
        string="Local file reference number",
        track_visibility='onchange',
        help="This is a free text field and can be used to include a Customs case number"
             "into the register",
        required=True,
    )

    offence_datetime = fields.Datetime(
        string="Offence date and time",
        track_visibility='onchange',
        help="This will enable analysis of exactly when offences take place and when used in conjunction with other"
             "fields may allow the analyst to identify “weak points” in coverage at each Customs office"
             "and border crossing. For example, importers may try to clear goods at the end of a shift when"
             "officers are fatigued or alternatively may time their clearance with exceptionally busy times at"
             "particular offices. If such trends are discovered then additional resources can be assigned.",
        required=True,

    )

    offence_code = fields.Many2one(
        "sando.offence_code",
        string="Offence Code",
        track_visibility='onchange',
        required=True,
    )

    profile = fields.Char(
        string="Risk Profile #",
        track_visibility='onchange',
        help="Profile # identifying the type of risk it was set up to counter."
             "Using the profile # will allow interrogation of the database to identify those profiles that"
             "are performing well and conversely, those that are failing to work. It will allow"
             "a performance measurement to be made and from that,"
             "non performing profiles can be amended or deleted appropriately.",
        required=True,
    )

    description_of_goods = fields.Text(
        string="Description of goods",
        track_visibility='onchange',
        help="Description of the goods as detailed as space allows. If possible should include Brand/Model numbers etc.",
        required=True,
    )

    customs_house = fields.Many2one(
        "sando.customs_house",
        string="Custom House Code",
        track_visibility='onchange',
        help="This information can be used by the analysts, in conjunction with other fields, to identify what types"
             "of offences are being detected at the various clearance offices and to create trend analysis"
             "and management reports. ",
        required=True,

    )

    case_officer = fields.Char(
        string="Case Officer",
        track_visibility='onchange',
        help="The full name of the officer that discovered the offence or gave the information.",
        required=True,
    )

    legal_act = fields.Char(
        string="Legal Act",
        track_visibility='onchange',
        help="Insert the Article, or regulation number under which the irregularity or offence"
             "was committed. Information such as this will help to identify the most common"
             "offences and may assist in identifying gaps or weaknesses in current legislation",
        required=True,
    )

    case_description = fields.Text(
        string="Case Description",
        track_visibility='onchange',
        help="A brief description of the case should be entered."
             "Type of goods, type of offence, etc. "
             "Sometimes having just a code to describe an event is insufficient.",
        required=True,
    )

    route = fields.Char(
        string="Route",
        track_visibility='onchange',
        help="This is the route taken by the goods/means of transport from when the goods"
             "were dispatched to arrival in the Customs territory. It should include the country"
             "of origin/dispatch/transit countries.",
        required=True,
    )

    offender_name = fields.Char(
        string="Offender’s Name",
        track_visibility='onchange',
        help="Enter the full name(s) of the offender(s)",
        required=True,
    )

    offender_id_number = fields.Char(
        string="Offender’s TIN/passport/ID number",
        track_visibility='onchange',
        help="If the trader does not have a TIN then the passport or ID card number should be recorded",
        required=True,
    )

    offender_address = fields.Text(
        string="Offender’s address",
        track_visibility='onchange',
        help="Can be used to search if the offenders name is not known",
        required=True,
    )

    offender_phone = fields.Char(
        string="Offender’s telephone number",
        track_visibility='onchange',
        help="If an offender is using multiple identities to disguise his importations,"
             "using a name may not highlight previous importations."
             "It is less likely that mobile phone numbers are changed and so recording"
             "this information may highlight duplicates where the same phone number"
             "is used by multiple identities",
        required=True,
    )

    offender_email = fields.Char(
        string="Offender’s email",
        track_visibility='onchange',
        required=True,
    )

    importer_or_exporter_name = fields.Char(
        string="Importer or Exporter Name",
        track_visibility='onchange',
        help="Can be searched to identify how many times specific individuals"
             "have been non-compliant. This is a useful tool for risk analysis",
    )

    importer_or_exporter_tin_number = fields.Char(
        string="Importer's or Exporter’s TIN",
        track_visibility='onchange',
        help="If the trader does not have a TIN then the passport or ID card number should be recorded",
    )

    importer_or_exporter_id_number = fields.Char(
        string="Importer's or Exporter’s Passport/ID number",
        track_visibility='onchange',
        help="If the trader does not have a TIN then the passport or ID card number should be recorded",
    )
    importer_or_exporter_address = fields.Text(
        string="Importer's or Exporter’s address",
        track_visibility='onchange',
        help="Can be used to search if the offenders name is not known",
    )

    importer_or_exporter_phone = fields.Char(
        string="Importer's or Exporter’s telephone number",
        track_visibility='onchange',
        help="If an offender is using multiple identities to disguise his importations,"
             "using a name may not highlight previous importations."
             "It is less likely that mobile phone numbers are changed and so recording"
             "this information may highlight duplicates where the same phone number"
             "is used by multiple identities",
    )

    importer_or_exporter_email = fields.Char(
        string="Importer's or Exporter’s email",
        track_visibility='onchange',
    )

    @staticmethod
    def clean_phone_number(number):
        if number:
            val = re.sub('[^0-9]+', '', number)
            if val:
                return re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(val[:-1])) + val[-1]
        return number

    @api.onchange('offender_phone')
    def _onchange_offender_phone(self):
        self.offender_phone = self.clean_phone_number(self.offender_phone)

    @api.onchange('importer_or_exporter_phone')
    def _onchange_importer_or_exporter_phone(self):
        self.importer_or_exporter_phone = self.clean_phone_number(self.importer_or_exporter_phone)

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('sando.sando')
        return super(sando, self).create(vals)

    def ValidateEmail(self, cr, uid, ids, email):
        if email:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
                return True
            else:
                raise osv.osv.except_osv('Invalid Email %s' % email, 'Please enter a valid email address')

        return True
