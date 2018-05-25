# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.tools.translate import _


class HrTimesheetComputation(models.Model):
    _name = "hr.timesheet_computation"
    _description = "Timesheet Computation"

    @api.model
    def _default_amount(self):
        return 0.0

    sheet_id = fields.Many2one(
        string="Timesheet",
        comodel_name="hr_timesheet_sheet.sheet",
    )
    item_id = fields.Many2one(
        string="Computation Item",
        comodel_name="hr.timesheet_computation_item",
        required=True,
    )
    amount = fields.Float(
        string="Computation Result",
        required=True,
        default=lambda self: self._default_amount(),
    )

    _sql_constrains = [
        ("item_unique", "unique(sheet_id, item_id)", _("No duplicate item")),
    ]

    @api.multi
    def _compute(self):
        self.ensure_one()
        return self.item_id._compute(self.sheet_id)

    @api.multi
    def action_compute(self):
        for computation in self:
            computation.write(computation._prepare_compute_data())

    @api.multi
    def _prepare_compute_data(self):
        self.ensure_one()
        return {
            "amount": self._compute(),
        }
