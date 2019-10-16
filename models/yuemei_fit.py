# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class YuemeiFit(models.Model):
    _name = 'yuemei.fit'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name')

    code = fields.Char('Code')
    team_name = fields.Char('Team')
    fight_no = fields.Many2one('res.air.plan', string='Fight No')
    customer_no = fields.Char('Customer no')

    employee_id = fields.Many2one('hr.employee', string='Operating staff')
    hotel_id = fields.Many2one('hotel.fit', string='Hotel')
    tour_guide_id = fields.Many2one('hr.employee', string='Tour guider')
    car_id = fields.Many2one('fleet.vehicle', string='Vehicle')

    sale_ids = fields.One2many('sale.order', 'fit_id', string='Sale')
    purchase_ids = fields.One2many('purchase.order', 'fit_id', string='Purchase')
    task_ids = fields.One2many('project.task', 'fit_id', string='Task')
    agenda_ids = fields.One2many('agenda.agenda', 'fit_id', string='Agenda')
    nkdh_ids = fields.One2many('nkdh.line', 'fit_id', string='History Travel')

    state = fields.Selection([
        ('draft', 'Quotation'),
        ('book', 'Reservation'),
        ('in_process', 'Operation'),
        ('paid', 'Reconciliation '),
        ('done', 'Evaluation'),
    ], string='Status', readonly=False, copy=False, index=True, track_visibility='onchange',
        default='draft')

    @api.multi
    def action_book(self):
        for p in self:
            p.write({'state': 'book'})
        return True

    @api.multi
    def action_in_process(self):
        for p in self:
            p.write({'state': 'in_process'})
        return True

    @api.multi
    def action_paid(self):
        for p in self:
            p.write({'state': 'paid'})
        return True

    @api.multi
    def action_done(self):
        for p in self:
            p.write({'state': 'done'})
        return True

    @api.multi
    def action_draft(self):
        for p in self:
            p.write({'state': 'draft'})
        return True