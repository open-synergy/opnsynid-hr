# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ResConfig(models.TransientModel):
    _inherit = "hr.attendance_config_setting"

    check_attendance = fields.Boolean(
        string="Check Attendance Entry",
        related="company_id.check_attendance",
    )
