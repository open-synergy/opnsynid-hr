# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models
from openerp.tools.translate import _


class HrHolidays(models.Model):
    _inherit = "hr.holidays"

    @api.multi
    @api.depends(
        "holiday_status_id",
        "type",
    )
    def _compute_day_limit_per_request(self):
        for leave in self:
            limit = -1
            leave_status = leave.holiday_status_id
            if leave_status.limit_day_per_request and leave.type == "remove":
                limit = leave_status.day_limit_per_request
            leave.day_limit_per_request = limit

    day_limit_per_request = fields.Integer(
        string="Day Limit Per Request",
        compute="_compute_day_limit_per_request",
        store=True,
    )

    @api.constrains(
        "day_limit_per_request",
        "number_of_days_temp",
    )
    def _constraint_day(self):
        if self.day_limit_per_request != -1:
            if self.number_of_days_temp > self.day_limit_per_request:
                strWarning = _("Limit per request exceed")
                raise models.ValidationError(strWarning)
