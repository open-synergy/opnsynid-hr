# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class HrTimesheetSheet(models.Model):
    _inherit = "hr_timesheet_sheet.sheet"

    @api.multi
    @api.depends("employee_id", "date_from", "date_to")
    def _compute_contract(self):
        for sheet in self:
            criteria1 = [
                "&",
                ("date_end", "<=", sheet.date_to),
                ("date_end", ">=", sheet.date_from),
            ]
            criteria2 = [
                "&",
                ("date_start", "<=", sheet.date_to),
                ("date_start", ">=", sheet.date_from),
            ]
            criteria3 = [
                "&",
                ("date_start", "<=", sheet.date_from),
                "|",
                ("date_end", "=", False),
                ("date_end", ">=", sheet.date_to),
            ]
            criteria = (
                [
                    ("employee_id", "=", sheet.employee_id.id),
                    "|",
                    "|",
                ]
                + criteria1
                + criteria2
                + criteria3
            )
            contracts = self.env["hr.contract"].search(criteria)
            sheet.contract_ids = [(6, 0, contracts.ids)]

    contract_ids = fields.Many2many(
        string="Relevant Contract",
        comodel_name="hr.contract",
        compute="_compute_contract",
    )
