# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api, SUPERUSER_ID


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    @api.multi
    @api.depends(
        "state",
        "company_id",
    )
    def _compute_policy(self):
        for batch in self:
            if self.env.user.id == SUPERUSER_ID:
                batch.confirm_ok = batch.refund_ok = \
                    batch.compute_ok = \
                    batch.set2draft_ok = \
                    batch.cancel_ok = True
                continue

            if batch.company_id:
                company = batch.company_id
                for policy in company.\
                        _get_payslip_button_policy_map():
                    setattr(
                        batch,
                        policy[0],
                        company.
                        _get_payslip_button_policy(
                            policy[1]),
                    )

    confirm_ok = fields.Boolean(
        string="Can Confirm",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    refund_ok = fields.Boolean(
        string="Can Refund",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    compute_ok = fields.Boolean(
        string="Can Compute Sheet",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    set2draft_ok = fields.Boolean(
        string="Can Set To Draft",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    cancel_ok = fields.Boolean(
        string="Can Cancel",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
