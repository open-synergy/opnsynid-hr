# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrTraining(models.Model):
    _inherit = "hr.training"

    @api.multi
    @api.depends(
        "analytic_account_id",
    )
    def _compute_analytic_line(self):
        for rec in self:
            obj_line = self.env["account.analytic.line"]
            criteria = [
                ("account_id", "child_of", rec.analytic_account_id.id),
            ]
            rec.analytic_line_ids = obj_line.search(criteria).ids

    analytic_account_id = fields.Many2one(
        string="Parent Analytic Account",
        comodel_name="account.analytic.account",
        domain=[
            ("type", "=", "view"),
        ],
    )
    analytic_line_ids = fields.Many2many(
        string="Cost and Revenue",
        comodel_name="account.analytic.line",
        compute="_compute_analytic_line",
    )
