# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, fields


class HrTimesheetSheet(models.Model):
    _inherit = "hr_timesheet_sheet.sheet"

    current_timesheet_account_id = fields.Many2one(
        string="Current Timesheet Account",
        comodel_name="account.analytic.account",
        readonly=True,
    )
