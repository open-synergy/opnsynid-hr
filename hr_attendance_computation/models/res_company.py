# -*- coding: utf-8 -*-
# Copyright 2011 Domsense srl (<http://www.domsense.com>)
# Copyright 2011-15 Agile Business Group sagl (<http://www.agilebg.com>)
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from __future__ import division
from openerp import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    working_time_precision = fields.Float(
        string='Working time precision',
        help='The precision used to analyse working times over working '
             'schedule (hh:mm)',
        required=True,
        default=1.0 / 60,
    )

    @api.multi
    def update_attendance_data(self):
        attendance_pool = self.env['hr.attendance']
        attendances = attendance_pool.search([])
        attendances.button_dummy()
        return True
