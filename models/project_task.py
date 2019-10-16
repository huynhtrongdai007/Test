# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    fit_id = fields.Many2one('yuemei.fit', string="FIT")
