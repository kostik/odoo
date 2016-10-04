# -*- coding: utf-8 -*-
from openerp import fields
from openerp import models


class hr_mis(models.Model):
    """
    From 1: http://redmine.kostik.net/redmine/issues/401
    """
    _name = 'hr.employee'
    _inherit = 'hr.employee'

    personal_number = fields.Char('Personal Number', required=True, help="Personal number in the MCD")
    other_name = fields.Char('Other Name')
    distinctive_marks = fields.Char('Distinctive Marks')

    height = fields.Integer('Height', help="cm")    # http://redmine.kostik.net/redmine/issues/409
    weight = fields.Integer('Weight', help="lbs")   # http://redmine.kostik.net/redmine/issues/409


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
