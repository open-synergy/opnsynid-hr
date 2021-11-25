# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import SUPERUSER_ID, api, fields, models


class HrHolidays(models.Model):
    _inherit = "hr.holidays"

    @api.multi
    @api.depends(
        "department_id",
        "state",
        "type",
    )
    def _compute_policy(self):
        for holiday in self:
            if self.env.user.id == SUPERUSER_ID:
                holiday.confirm_ok = (
                    holiday.approve_ok
                ) = holiday.refuse_ok = holiday.validate_ok = holiday.restart_ok = True
                continue

            if holiday.department_id:
                department = holiday.department_id
                for policy in department._get_holiday_button_policy_map(self.type):
                    setattr(
                        holiday,
                        policy[0],
                        department._get_holiday_button_policy(policy[1]),
                    )
            else:
                holiday.confirm_ok = (
                    holiday.approve_ok
                ) = holiday.refuse_ok = holiday.validate_ok = holiday.restart_ok = False

    confirm_ok = fields.Boolean(
        string="Can Confirm",
        compute="_compute_policy",
        store=False,
    )
    approve_ok = fields.Boolean(
        string="Can Approve",
        compute="_compute_policy",
        store=False,
    )
    refuse_ok = fields.Boolean(
        string="Can Refuse",
        compute="_compute_policy",
        store=False,
    )
    restart_ok = fields.Boolean(
        string="Can Restart",
        compute="_compute_policy",
        store=False,
    )
    validate_ok = fields.Boolean(
        string="Can Validate",
        compute="_compute_policy",
        store=False,
    )
