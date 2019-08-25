# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResConfig(models.TransientModel):
    _inherit = "hr.attendance_config_setting"

    check_timesheet_equal_attendance = fields.Boolean(
        string="Check Equal Timesheet Attendance",
        related="company_id.check_timesheet_equal_attendance",
    )
