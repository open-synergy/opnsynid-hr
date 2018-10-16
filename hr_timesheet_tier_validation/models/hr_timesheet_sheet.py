# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class HrTimesheetSheet(models.Model):
    _name = "hr_timesheet_sheet.sheet"
    _inherit = ["hr_timesheet_sheet.sheet", "tier.validation"]
    _state_from = ["confirm"]
    _state_to = ["done"]
