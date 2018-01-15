# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrTraining(models.Model):
    _inherit = "hr.training"

    @api.multi
    @api.depends(
        "budget_id",
        "analytic_account_id",
    )
    def _compute_budget_line(self):
        for rec in self:
            obj_line = self.env["crossovered.budget.lines"]
            aa = rec.analytic_account_id
            if aa and rec.budget_id:
                criteria = [
                    ("crossovered_budget_id", "=", rec.budget_id.id),
                    ("analytic_account_id", "child_of", aa.id),
                ]
                rec.budget_line_ids = obj_line.search(criteria).ids

    budget_id = fields.Many2one(
        string="Budget",
        comodel_name="crossovered.budget",
    )
    budget_line_ids = fields.Many2many(
        string="Budget Line",
        comodel_name="crossovered.budget.lines",
        compute="_compute_budget_line",
    )
