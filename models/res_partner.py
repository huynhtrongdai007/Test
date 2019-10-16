# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    fit_id = fields.Many2one('yuemei.fit', string="FIT")
    nkdh_ids = fields.One2many('nkdh.line', 'partner_id', string='History Travel')
