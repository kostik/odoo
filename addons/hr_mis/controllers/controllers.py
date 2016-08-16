# -*- coding: utf-8 -*-
from openerp import http

# class HrMis(http.Controller):
#     @http.route('/hr_mis/hr_mis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_mis/hr_mis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_mis.listing', {
#             'root': '/hr_mis/hr_mis',
#             'objects': http.request.env['hr_mis.hr_mis'].search([]),
#         })

#     @http.route('/hr_mis/hr_mis/objects/<model("hr_mis.hr_mis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_mis.object', {
#             'object': obj
#         })