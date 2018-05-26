# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrTimesheetSheet(models.Model):
    _inherit = "hr_timesheet_sheet.sheet"

    holiday_ids = fields.One2many(
        string="Holidays",
        comodel_name="hr.holidays",
        inverse_name="sheet_id",
    )
