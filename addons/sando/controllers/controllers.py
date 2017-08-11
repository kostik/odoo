# -*- coding: utf-8 -*-
from openerp import http

# class Sando(http.Controller):
#     @http.route('/sando/sando/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sando/sando/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sando.listing', {
#             'root': '/sando/sando',
#             'objects': http.request.env['sando.sando'].search([]),
#         })

#     @http.route('/sando/sando/objects/<model("sando.sando"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sando.object', {
#             'object': obj
#         })