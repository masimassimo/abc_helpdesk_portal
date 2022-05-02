# -*- coding: utf-8 -*-
# from odoo import http


# class AbcHelpdeskPortalExt(http.Controller):
#     @http.route('/abc_helpdesk_portal_ext/abc_helpdesk_portal_ext/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_helpdesk_portal_ext/abc_helpdesk_portal_ext/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_helpdesk_portal_ext.listing', {
#             'root': '/abc_helpdesk_portal_ext/abc_helpdesk_portal_ext',
#             'objects': http.request.env['abc_helpdesk_portal_ext.abc_helpdesk_portal_ext'].search([]),
#         })

#     @http.route('/abc_helpdesk_portal_ext/abc_helpdesk_portal_ext/objects/<model("abc_helpdesk_portal_ext.abc_helpdesk_portal_ext"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_helpdesk_portal_ext.object', {
#             'object': obj
#         })
