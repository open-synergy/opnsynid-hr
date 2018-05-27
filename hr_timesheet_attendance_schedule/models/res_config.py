# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResConfig(models.TransientModel):
    _inherit = "hr.attendance_config_setting"

    early_attendance_buffer = fields.Float(
        string="Early Attendance Buffer",
        related="company_id.early_attendance_buffer",
    )
    late_attendance_buffer = fields.Float(
        string="Late Attendance Buffer",
        related="company_id.late_attendance_buffer",
    )
