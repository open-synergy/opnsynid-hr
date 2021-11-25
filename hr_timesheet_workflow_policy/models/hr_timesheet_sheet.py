# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import SUPERUSER_ID, api, fields, models


class HrTimesheetSheet(models.Model):
    _inherit = "hr_timesheet_sheet.sheet"

    @api.multi
    @api.depends(
        "state",
        "company_id",
    )
    def _compute_policy(self):
        for batch in self:
            if self.env.user.id == SUPERUSER_ID:
                batch.submit_ok = (
                    batch.approve_ok
                ) = batch.refuse_ok = batch.set2draft_ok = True
                continue

            if batch.company_id:
                company = batch.company_id
                for policy in company._get_timesheet_button_policy_map():
                    setattr(
                        batch,
                        policy[0],
                        company._get_timesheet_button_policy(policy[1]),
                    )

    submit_ok = fields.Boolean(
        string="Can Submit to Manager",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    approve_ok = fields.Boolean(
        string="Can Approve",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    refuse_ok = fields.Boolean(
        string="Can Refuse",
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
