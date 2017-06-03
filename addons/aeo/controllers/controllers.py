# -*- coding: utf-8 -*-
from openerp import http

# class Aeo(http.Controller):
#     @http.route('/aeo/aeo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aeo/aeo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aeo.listing', {
#             'root': '/aeo/aeo',
#             'objects': http.request.env['aeo.aeo'].search([]),
#         })

#     @http.route('/aeo/aeo/objects/<model("aeo.aeo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aeo.object', {
#             'object': obj
#         })