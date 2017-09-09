# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrHolidayStatus(models.Model):
    _inherit = "hr.holidays.status"

    limit_day_per_request = fields.Boolean(
        string="Limit Days Per Request",
    )
    day_limit_per_request = fields.Integer(
        string="Days Limit Per Request",
    )
