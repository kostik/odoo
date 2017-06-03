# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


class res_partner(osv.osv):
    _inherit = 'res.partner'

    _columns = {
        'aeo_status': fields.boolean(string='AEO status')
    }
