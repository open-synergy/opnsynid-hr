# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    early_attendance_buffer = fields.Float(
        string="Early Attendance Buffer",
        default=0.0,
        required=True,
    )
    late_attendance_buffer = fields.Float(
        string="Late Attendance Buffer",
        default=0.0,
        required=True,
    )
