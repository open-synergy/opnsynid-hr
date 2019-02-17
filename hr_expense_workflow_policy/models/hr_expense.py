# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api, fields


class HrExpenseExpense(models.Model):
    _name = "hr.expense.expense"
    _inherit = ["hr.expense.expense", "base.workflow_policy_object"]

    @api.multi
    @api.depends(
        "journal_id",
    )
    def _compute_policy(self):
        _super = super(HrExpenseExpense, self)
        _super._compute_policy()

    confirm_ok = fields.Boolean(
        string="Can Confirm",
        compute="_compute_policy",
        store=False,
    )
    validate_ok = fields.Boolean(
        string="Can Approve",
        compute="_compute_policy",
        store=False,
    )
    refuse_ok = fields.Boolean(
        string="Can Refuse",
        compute="_compute_policy",
        store=False,
    )
    done_ok = fields.Boolean(
        string="Can Generate Accounting Entries",
        compute="_compute_policy",
        store=False,
    )
    restart_ok = fields.Boolean(
        string="Can Restart",
        compute="_compute_policy",
        store=False,
    )
    view_ok = fields.Boolean(
        string="Can View Accounting Entries",
        compute="_compute_policy",
        store=False,
    )
