# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class NkdhLine(models.Model):
    _name = 'nkdh.line'

    name = fields.Char('Name')
    fit_id = fields.Many2one('yuemei.fit', string="FIT")
    partner_id = fields.Many2one('res.partner', string="Customer")

    date1 = fields.Date('date come')
    place1 = fields.Char('place come')
    flight1 = fields.Char('Flight come')
    time1 = fields.Float('time 1 ')
    time2 = fields.Float('time 2 ')

    date2 = fields.Date('date leave')
    place2 = fields.Char('place leave')
    flight2 = fields.Char('Flight leave ')
    time3 = fields.Float('time 3')
    time4 = fields.Float('time 4')

    ks_check_in = fields.Date('KS check in')
    ks_check_out = fields.Date('KS check out')

    passport = fields.Char('Passport')
    visa = fields.Char('Visa')
