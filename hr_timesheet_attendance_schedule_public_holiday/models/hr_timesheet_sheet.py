# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models, api


class HrTimesheetSheet(models.Model):
    _inherit = "hr_timesheet_sheet.sheet"

    @api.multi
    def _check_existing_schedule(self, dt_start, dt_end):
        _super = super(HrTimesheetSheet, self)
        res = _super._check_existing_schedule(dt_start, dt_end)

        conv_date = fields.Date.from_string(dt_start)
        obj_base_public_holiday = \
            self.env["base.public.holiday"]
        if obj_base_public_holiday.is_public_holiday(conv_date):
            return False
        else:
            return res
