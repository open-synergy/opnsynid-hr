# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, fields


class ResConfig(models.TransientModel):
    _inherit = "hr.attendance_config_setting"

    timesheet_sheet_sequence_id = fields.Many2one(
        string="Timesheet Sheet Sequence",
        comodel_name="ir.sequence",
        related="company_id.timesheet_sheet_sequence_id",
        store=False,
    )
