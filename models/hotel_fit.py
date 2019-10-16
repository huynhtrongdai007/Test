# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Hotel(models.Model):
    _name = 'hotel.fit'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Tên khách sạn')
    diachi = fields.Char('Địa chỉ')
    email = fields.Char('Email')
    sdt = fields.Char('Số điện thoại')
