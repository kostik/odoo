# -*- coding: utf-8 -*-
import datetime
import re

from openerp import _
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


class sando_customs_regime_code(models.Model):
    _name = 'sando.customs_regime_code'
    name = fields.Char(
        string="Customs regime code",
        required=True
    )


class sando_vehicle_type(models.Model):
    _name = 'sando.vehicle_type'
    name = fields.Char(
        string="Vehicle type",
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
        size=10,
        readonly=True
    )

    active = fields.Boolean(
        default=True,
        track_visibility='onchange',
        help="Set active to false to hide the case without removing it."
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
        help="This is a free text field and can be used to include a Customs case number "
             "into the register",
    )

    offence_datetime = fields.Datetime(
        string="Offence date and time",
        track_visibility='onchange',
        help="This will enable analysis of exactly when offences take place and when used in conjunction with other "
             "fields may allow the analyst to identify “weak points” in coverage at each Customs office "
             "and border crossing. For example, importers may try to clear goods at the end of a shift when "
             "officers are fatigued or alternatively may time their clearance with exceptionally busy times at "
             "particular offices. If such trends are discovered then additional resources can be assigned.",

    )

    offence_code = fields.Many2one(
        "sando.offence_code",
        string="Offence Code",
        track_visibility='onchange',
    )

    profile = fields.Char(
        string="Risk Profile #",
        track_visibility='onchange',
        help="Profile # identifying the type of risk it was set up to counter."
             "Using the profile # will allow interrogation of the database to identify those profiles that "
             "are performing well and conversely, those that are failing to work. It will allow "
             "a performance measurement to be made and from that, "
             "non performing profiles can be amended or deleted appropriately.",
    )

    description_of_goods = fields.Text(
        string="Description of goods",
        track_visibility='onchange',
        help="Description of the goods as detailed as space allows. If possible should include Brand/Model numbers etc.",
    )

    customs_house = fields.Many2one(
        "sando.customs_house",
        string="Custom House Code",
        track_visibility='onchange',
        help="This information can be used by the analysts, in conjunction with other fields, to identify what types "
             "of offences are being detected at the various clearance offices and to create trend analysis"
             "and management reports. ",
    )

    case_officer = fields.Char(
        string="Case Officer",
        track_visibility='onchange',
        help="The full name of the officer that discovered the offence or gave the information.",
    )

    legal_act = fields.Char(
        string="Legal Act",
        track_visibility='onchange',
        help="Insert the Article, or regulation number under which the irregularity or offence "
             "was committed. Information such as this will help to identify the most common "
             "offences and may assist in identifying gaps or weaknesses in current legislation",
    )

    case_description = fields.Text(
        string="Case Description",
        track_visibility='onchange',
        help="A brief description of the case should be entered. "
             "Type of goods, type of offence, etc. "
             "Sometimes having just a code to describe an event is insufficient.",
    )

    route = fields.Char(
        string="Route",
        track_visibility='onchange',
        help="This is the route taken by the goods/means of transport from when the goods "
             "were dispatched to arrival in the Customs territory. It should include the country "
             "of origin/dispatch/transit countries.",
    )

    offender_name = fields.Char(
        string="Offender’s Name",
        track_visibility='onchange',
        help="Enter the full name(s) of the offender(s)",
    )

    offender_id_number = fields.Char(
        string="Offender’s TIN/passport/ID number",
        track_visibility='onchange',
        help="If the trader does not have a TIN then the passport or ID card number should be recorded",
    )

    offender_address = fields.Text(
        string="Offender’s address",
        track_visibility='onchange',
        help="Can be used to search if the offenders name is not known",
    )

    offender_phone = fields.Char(
        string="Offender’s telephone number",
        track_visibility='onchange',
        help="If an offender is using multiple identities to disguise his importations, "
             "using a name may not highlight previous importations. "
             "It is less likely that mobile phone numbers are changed and so recording "
             "this information may highlight duplicates where the same phone number "
             "is used by multiple identities",
    )

    offender_email = fields.Char(
        string="Offender’s email",
        track_visibility='onchange',
    )

    importer_or_exporter_name = fields.Char(
        string="Importer or Exporter Name",
        track_visibility='onchange',
        help="Can be searched to identify how many times specific individuals "
             "have been non-compliant. This is a useful tool for risk analysis",
    )

    importer_or_exporter_id_number = fields.Char(
        string="Importer's or Exporter’s TIN/Passport/ID number",
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
        help="If an offender is using multiple identities to disguise his importations, "
             "using a name may not highlight previous importations. "
             "It is less likely that mobile phone numbers are changed and so recording "
             "this information may highlight duplicates where the same phone number "
             "is used by multiple identities",
    )

    importer_or_exporter_email = fields.Char(
        string="Importer's or Exporter’s email",
        track_visibility='onchange',
    )

    name_of_customs_broker = fields.Char(
        string="Name of Customs Broker",
        track_visibility='onchange',
        help="Can be used to search for brokers that are regularly inputting incorrect "
             "declarations either by error or in collusion with importers",
    )

    broker_id_number = fields.Char(
        string="Broker’s TIN/Passport/ID Number",
        track_visibility='onchange',
        help="Customs Brokers often work in coordination with importers to evade controls and revenue. "
             "Using this field will enable analysis to be made of customs brokers that are involved "
             "in a higher number of infractions or offences than would be considered normal. "
             "It would also identify other traders that may represent a greater risk because "
             "of their association with non-compliant brokers",
    )
    broker_address = fields.Text(
        string="Broker’s address",
        track_visibility='onchange',
        help="Can be used to help track traders who change their identity. "
             "Often they retain their address. By using this field in a query, "
             "the database will display all traders that utilise this address.",
    )

    broker_phone = fields.Char(
        string="Broker’s telephone number",
        track_visibility='onchange',
        help="This field can be utilised to find traders that are itinerant (briefcase traders) "
             "and change their names and or addresses in order to deceive Customs when making declarations. "
             "It is more inconvenient to change phone numbers and therefore traders often retain the same "
             "number even though they utilise false names. Entering this field in a query will give a "
             "list of all traders using this phone number",
    )

    broker_email = fields.Char(
        string="Broker’s email",
        track_visibility='onchange',
    )

    exporter_or_supplier_name = fields.Char(
        string="Exporter’s or Supplier’s name",
        track_visibility='onchange',
        help="The name of the foreign exporter or supplier of the goods."
             "They may work in collusion with the importer in order to facilitate under valuation, "
             "misdescription, falsification of origin, or general underdeclaration. "
             "Search using this field will highlight all importations made where an irregularity has been found",
    )

    supplier_address = fields.Text(
        string="Supplier’s Address",
        track_visibility='onchange',
        help="Interrogation of the database using this assist to verify the identity "
             "and country of origin of suppliers that are/may be involved in certain types "
             "of offences such as undervaluation, misdescription. Queries using this field "
             "in conjunction with others will also reveal such things as which importers "
             "they deal with, what types of goods, etc. ",
    )

    transporter_or_haulier_name = fields.Char(
        string="Transporter or haulier’s name",
        track_visibility='onchange',
        help="Transport companies may pose a risk either because they assist the trade "
             "in smuggling goods or often because they undertake smuggling operations "
             "in their own right. Querying this field together with others may highlight "
             "associations with suppliers or importers who are known to be non- compliant "
             "and also those companies that use routes which pose a higher risk, "
             "for example through drug source countries",
    )

    transporter_id_number = fields.Char(
        string="Transporter’s TIN/Passport/ID Number",
        track_visibility='onchange',
    )

    transporter_address = fields.Text(
        string="Transporter’s address",
        track_visibility='onchange',
        help="Can be used to help track traders who change their identity. "
             "Often they retain their address. By using this field in a query, "
             "the database will display all traders that utilise this address",
    )

    transporter_phone = fields.Char(
        string="Transporter’s telephone number",
        track_visibility='onchange',
        help="Assists to search for associates of non compliant traders and those "
             "that use multiple names. Whereas many traders will change names "
             "on each declaration to mislead Customs, few will go to the trouble "
             "of changing cell and/or land line numbers as they will not expectCustoms to have the means to check",
    )

    transporter_email = fields.Char(
        string="Transporter’s email",
        track_visibility='onchange',
    )

    vehicle_driver_name = fields.Char(
        string="Vehicle driver’s name",
        track_visibility='onchange',
        help="This is required as drivers are often either involved in irregularities as accomplices to traders "
             "or are directly involved in carrying contraband in the vehicles whether or not the owner of the goods "
             "is involved in non-compliance.",
    )

    driver_id_number = fields.Char(
        string="Driver’s TIN/Passport/ID Number",
        track_visibility='onchange',
        help="Assists in the identification of persons that are regularly involved in non-compliance, "
             "smuggling or irregularities",
    )
    driver_address = fields.Text(
        string="Driver’s address",
        track_visibility='onchange',
        help="Can be used to help track persons of interest who change their identity. "
             "Often they retain their address. By using this field in a query, "
             "the database will display everyone that utilise this address",
    )

    driver_phone = fields.Char(
        string="Driver’s telephone number",
        track_visibility='onchange',
        help="Assists to search for associates of non compliant traders and those "
             "that use multiple names. Whereas many traders will change names "
             "on each declaration to mislead Customs, few will go to the trouble "
             "of changing cell and/or land line numbers as they will not expectCustoms to have the means to check",
    )

    driver_email = fields.Char(
        string="Driver’s email",
        track_visibility='onchange',
    )

    vehicle_type = fields.Many2one(
        "sando.vehicle_type",
        string="Vehicle type",
        track_visibility='onchange',
        help="Drop down menu that will give options categorizing what means of transport has been used "
             "covering vehicle "
             "(Freight, private, public transport vehicle), train (Freight or Passenger), "
             "Air (private, passenger, freight) or Other (enter details in Notes box). "
             "This will enable searches to be made that will show trends – certain "
             "types of goods smuggled using particular means of transport, etc.)",
        required=False,
    )

    vehicle_make_and_model = fields.Char(
        string="Make or brand name of vehicle or means of transport",
        track_visibility='onchange',
        help="Can potentially be used to identify particular methods of concealment on particular makes "
             "of vehicles/aircraft/containers",
    )

    harmonised_system_code = fields.Char(
        string="Harmonised System of Classification Code/Tariff Trade Code etc.",
        track_visibility='onchange',
    )

    country_of_origin = fields.Many2one(
        "res.country",
        string="Country of Origin",
        help="Enter the country of origin of the goods subject to the offence from the drop down menu. "
             "This may or may not be the country of supply! ",
        track_visibility='onchange',
    )

    country_of_departure = fields.Many2one(
        "res.country",
        string="Country of Departure",
        help="The country from which the goods are consigned. (Select from drop down menu)",
        track_visibility='onchange',
    )

    country_of_destination = fields.Many2one(
        "res.country",
        string="Country of Destination",
        help="The final destination of the goods. Select from drop down menu)",
        track_visibility='onchange',
    )
    weight_declared = fields.Float(
        string="Declared weight of the goods (Net) in kgs",
        help="Enter the net weight of the goods in Kgs as declared",
        track_visibility='onchange',
    )

    weight_actual = fields.Float(
        string="Actual weight of the goods (net) in Kgs",
        help="Enter the actual weight found if the offence includes "
             "underdeclaring the actual weight of the goods",
        track_visibility='onchange',

    )

    number_of_packages_declaration = fields.Integer(
        string="Number of packages entered on the declaration",
        help="Enables a judgement to be made concerning the significance of any potential offence in cases where "
             "underdeclaration of the number of packages is an issue",
        track_visibility='onchange',
    )

    number_of_packages_actual = fields.Integer(
        string="Actual Number of Packages",
        help="Enter the actual number of packages found during inspection if different from declared number",
        track_visibility='onchange',
    )

    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
    )

    value_declared = fields.Monetary(
        currency_field="currency_id",
        string="Declared Statistical Value",
        help="Allows comparison to be made between how much was declared and how much the goods were actually worth",
        track_visibility='onchange',
    )

    value_actual = fields.Monetary(
        currency_field="currency_id",
        string="Actual Statistical Value if different from Declared Statistical value",
        help="Allows comparison to be made between how much was declared and how much the goods were actually worth",
        track_visibility='onchange',
    )

    additional_duties = fields.Monetary(
        currency_field="currency_id",
        string="Additional duties resulting from offence",
        help="This is the total of all penalties imposed in relation to the specific offence. It indicates the "
             "magnitude of the problem and is useful in assessing the risk for future importations/exportations "
             "that will be made by the same principals. Enter any additional duties or taxes that have been levied "
             "on the offender as a result of the irregularity that was found.",
        track_visibility='onchange',
    )

    declaration_number = fields.Char(
        string="Declaration Number",
        track_visibility='onchange',
        help="Enables the system to identify the declaration in order to extract further data",
    )

    customs_regime_code = fields.Many2one(
        "sando.customs_regime_code",
        string="Customs regime code",
        track_visibility='onchange',
        help="Select the correct regime code (home use, warehousing, export, etc) from the drop down menu",
    )

    seized_goods = fields.Boolean(
        string="Seized Goods",
        track_visibility='onchange',
        help="Tick box indicating whether goods have been confiscated by Customs or not",
    )

    penalty_imposed = fields.Boolean(
        string="Penalty Imposed",
        track_visibility='onchange',
    )

    inspection_result = fields.Text(
        string="Inspection Result",
        track_visibility='onchange',
        help="This is an unlimited text box that can be used to describe what was found during the examination. "
             "For example, it could include specific cases that were examined, particular concealments "
             "or characteristics specific to smuggled goods. Should add basis for discovery of offence"
             "e.g Red Channel exam/Random exam/full exam/MACCS profile /x ray/ info received/voluntary declaration, "
             "etc",
    )

    @staticmethod
    def clean_phone_number(number):
        if number:
            val = re.sub('[^0-9]+', '', number)
            if val:
                return re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(val[:-1])) + val[-1]
        return number

    @api.onchange('driver_phone')
    def _onchange_driver_phone(self):
        self.driver_phone = self.clean_phone_number(self.driver_phone)

    @api.onchange('transporter_phone')
    def _onchange_transporter_phone(self):
        self.transporter_phone = self.clean_phone_number(self.transporter_phone)

    @api.onchange('broker_phone')
    def _onchange_broker_phone(self):
        self.broker_phone = self.clean_phone_number(self.broker_phone)

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

    @api.multi
    def unlink(self):
        from openerp.exceptions import AccessError
        raise AccessError(_("You are can not delete this record"))


DEFAULT_EXPIRATION_DAYS = 365 * 6


class intelligence(models.Model):
    _name = 'sando.intelligence'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _description = "Intelligence record"
    _order = 'name desc'

    name = fields.Char(
        string='Serial Number',
        help='Prime key to allow the computer to link various information.'
             'If a record is deleted, the number is deleted and cannot be used again.'
             'This prevents different records from ever having the same serial number.'
             '(E.G. there will never be two records in the register with serial number 5)',
        size=10,
        readonly=True
    )

    active = fields.Boolean(
        default=True,
        track_visibility='onchange',
        help="Set active to false to hide the case without removing it."
    )

    report_datetime = fields.Datetime(
        string="Report date and time",
        track_visibility='onchange',
    )

    report_expiry_date = fields.Datetime(
        string="Report expiry date",
        track_visibility='onchange',
        default=datetime.datetime.now() + datetime.timedelta(days=DEFAULT_EXPIRATION_DAYS)
    )

    # customs_house = fields.Many2one(
    #     "sando.customs_house",
    #     string="Custom House Code",
    #     track_visibility='onchange',
    # )

    officer_reporting = fields.Char(
        string="Officer receiving information ",
        track_visibility='onchange',
    )

    officer_evaluating = fields.Char(
        string="Officer evaluating information ",
        track_visibility='onchange',
    )

    evaluation_source = fields.Selection(
        string='Evaluation source',
        selection=[
            (
                'A', 'No doubt regarding authenticity, trustworthiness, '
                     'integrity, competence, or, a history of complete reliability'
            ),
            (
                'B', 'Source from whom information received has in most instances proved to be reliable'
            ),
            (
                'C', 'Source from whom information received has in most instances proved to be unreliable'
            ),
            (
                'X', 'Reliability cannot be judged'
            ),

        ]
    )
    evaluation_intelligence = fields.Selection(
        string='Evaluation intelligence',
        selection=[
            (
                '1', 'No doubt about accuracy'
            ),
            (
                '2', "Information known personally to the source but not known personally "
                     "to the official who is passing it on"
            ),
            (
                '3', 'Information not known personally to the source but corroborated '
                     'by other information already recorded'
            ),
            (
                '4', 'Information which is not known personally to the source and cannot be independently corroborated'
            ),

        ]
    )

    evaluation = fields.Char(string="Evaluation 4x4",
                             compute='_set_evaluation', store=True, read_only=True,
                             track_visibility='onchange')

    reasons_for_suspicion = fields.Text(
        string="Reasons for suspicion",
        track_visibility='onchange',
    )

    activity_suspected = fields.Text(
        string="Suspected activity - details of information received",
        track_visibility='onchange',
    )

    goods = fields.Text(
        string="Goods description",
        track_visibility='onchange',
    )

    # activity_location = fields.Char(
    #     string="Location of activity",
    #     track_visibility='onchange',
    # )
    # flight_number = fields.Char(
    #     string="Flight Number",
    #     track_visibility='onchange',
    # )
    # travel_dates_from = fields.Date(
    #     string="Travel date (from)",
    #     track_visibility='onchange',
    # )
    # travel_dates_to = fields.Date(
    #     string="Travel date (to)",
    #     track_visibility='onchange',
    # )
    # associates = fields.Char(
    #     string="Associates",
    #     track_visibility='onchange',
    # )
    # vessel_name = fields.Char(
    #     string="Vessel name",
    #     track_visibility='onchange',
    # )
    # vessel_port_of_registration = fields.Char(
    #     string="Vessel port of registration",
    #     track_visibility='onchange',
    # )
    # vessel_owners = fields.Char(
    #     string="Vessel owners",
    #     track_visibility='onchange',
    # )
    # vessel_type = fields.Char(
    #     string="Vessel type",
    #     track_visibility='onchange',
    # )
    # aircraft_registration = fields.Char(
    #     string="Aircraft (General Aviation) registration",
    #     track_visibility='onchange',
    # )
    # aircraft_type = fields.Char(
    #     string="Aircraft type",
    #     track_visibility='onchange',
    # )

    sando_ids = fields.Many2many(
        'sando.sando',
        ondelete='restrict',
        string="Related offence records",
        track_visibility='onchange',
    )

    @api.depends("evaluation_source", "evaluation_intelligence")
    def _set_evaluation(self):
        self.evaluation = (self.evaluation_source or ' ') + (self.evaluation_intelligence or ' ')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('sando.intelligence')
        return super(intelligence, self).create(vals)

    @api.multi
    def unlink(self):
        from openerp.exceptions import AccessError
        raise AccessError(_("You are can not delete this record"))
