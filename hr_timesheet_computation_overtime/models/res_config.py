# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class ResConfig(models.TransientModel):
    _inherit = "hr.overtime_config_setting"

    overtime_check_timesheet = fields.Boolean(
        string="Check Timesheet",
        related="company_id.overtime_check_timesheet",
    )
