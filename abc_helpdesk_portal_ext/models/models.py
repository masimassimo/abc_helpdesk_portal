# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class abc_helpdesk_portal_ext(models.Model):
#     _name = 'abc_helpdesk_portal_ext.abc_helpdesk_portal_ext'
#     _description = 'abc_helpdesk_portal_ext.abc_helpdesk_portal_ext'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
