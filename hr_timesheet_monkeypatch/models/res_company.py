# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    check_timesheet_equal_attendance = fields.Boolean(
        string="Check Equal Timesheet Attendance",
        default=True,
    )
