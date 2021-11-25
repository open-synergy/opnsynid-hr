# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import SUPERUSER_ID, api, fields, models


class HrPayslipRun(models.Model):
    _inherit = "hr.payslip.run"

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id.id

    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        default=lambda self: self._default_company_id(),
        readonly=False,
    )

    @api.multi
    @api.depends(
        "state",
        "company_id",
    )
    def _compute_policy(self):
        for batch in self:
            if self.env.user.id == SUPERUSER_ID:
                batch.close_ok = batch.generate_ok = batch.set2draft_ok = True
                continue

            if batch.company_id:
                company = batch.company_id
                for policy in company._get_payslip_run_button_policy_map():
                    setattr(
                        batch,
                        policy[0],
                        company._get_payslip_button_policy(policy[1]),
                    )

    close_ok = fields.Boolean(
        string="Can Close",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    generate_ok = fields.Boolean(
        string="Can Generate",
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
