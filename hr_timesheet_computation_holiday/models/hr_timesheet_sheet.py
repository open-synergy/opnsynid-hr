# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class HrTimesheetSheet(models.Model):
    _inherit = "hr_timesheet_sheet.sheet"

    holiday_ids = fields.One2many(
        string="Holidays",
        comodel_name="hr.holidays",
        inverse_name="sheet_id",
    )
