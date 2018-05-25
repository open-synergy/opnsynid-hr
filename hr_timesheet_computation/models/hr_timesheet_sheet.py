# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrTimesheetSheet(models.Model):
    _inherit = "hr_timesheet_sheet.sheet"

    computation_ids = fields.One2many(
        string="Computations",
        comodel_name="hr.timesheet_computation",
        inverse_name="sheet_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )

    @api.multi
    def action_compute_timesheet(self):
        for sheet in self:
            sheet._clear_computation()
            sheet._get_computation()
            sheet._compute_timesheet()

    @api.multi
    def _clear_computation(self):
        self.ensure_one()
        self.computation_ids.unlink()

    @api.multi
    def _get_computation(self):
        self.ensure_one()
        items = self.env["hr.timesheet_computation_item"]
        computations = []
        contracts = self.contract_ids
        for contract in contracts:
            if contract.computation_ids:
                items += contract.computation_ids.mapped("item_id")
        items = set(items)
        for item in items:
            data = {
                "item_id": item.id,
                "amount": 0.0,
            }
            computations.append((0, 0, data))
        self.write({"computation_ids": computations})

    @api.multi
    def _compute_timesheet(self):
        self.ensure_one()
        self.computation_ids.action_compute()
