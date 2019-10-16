# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class AgendaAgenda(models.Model):
    _name = 'agenda.agenda'

    agenda_line_date = fields.Date(string='Date', default=fields.Date.today)
    name = fields.Char('Description')

    fit_id = fields.Many2one('yuemei.fit', string="FIT")
    sang1 = fields.Char('Ăn sáng')
    sang2 = fields.Char('Buổi sáng')
    trua1 = fields.Char('Ăn trưa')
    trua2 = fields.Char('Buổi trưa')
    toi1 = fields.Char('Ăn tối')
    toi2 = fields.Char('Buổi tối')
