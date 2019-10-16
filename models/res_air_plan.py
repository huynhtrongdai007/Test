# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResAirLlan(models.Model):
    _name = 'res.air.plan'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name')
    code = fields.Char('Code')

    date_from = fields.Date('Date From')
    date_to = fields.Date('Date To')

    place_from = fields.Char('Place From')
    place_to = fields.Char('Place To')
