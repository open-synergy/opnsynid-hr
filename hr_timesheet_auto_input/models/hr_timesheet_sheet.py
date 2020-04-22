# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, fields, api


class HrTimesheetSheet(models.Model):
    _inherit = "hr_timesheet_sheet.sheet"

    current_timesheet_account_id = fields.Many2one(
        string="Current Timesheet Account",
        comodel_name="account.analytic.account",
        readonly=True,
    )
    current_product_id = fields.Many2one(
        string="Current Product",
        comodel_name="product.product",
        readonly=True,
    )
    current_task_id = fields.Many2one(
        string="Current Task",
        comodel_name="project.task",
        readonly=True,
    )
