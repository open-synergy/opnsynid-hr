# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ResCompany(models.Model):
    _inherit = "res.company"

    timesheet_submit_grp_ids = fields.Many2many(
        string="Allowed To Submit to Manager",
        comodel_name="res.groups",
        relation="rel_timesheet_allowed_submit_groups",
        column1="company_id",
        column2="group_id",
    )
    timesheet_approve_grp_ids = fields.Many2many(
        string="Allowed To Approve",
        comodel_name="res.groups",
        relation="rel_timesheet_allowed_approve_groups",
        column1="company_id",
        column2="group_id",
    )
    timesheet_refuse_grp_ids = fields.Many2many(
        string="Allowed To Refuse",
        comodel_name="res.groups",
        relation="rel_timesheet_allowed_refuse_groups",
        column1="company_id",
        column2="group_id",
    )
    timesheet_set2draft_grp_ids = fields.Many2many(
        string="Allowed To Set To Draft",
        comodel_name="res.groups",
        relation="rel_timesheet_allowed_set2draft_groups",
        column1="company_id",
        column2="group_id",
    )

    @api.model
    def _get_timesheet_button_policy_map(self):
        return [
            ("submit_ok",
                "timesheet_submit_grp_ids"),
            ("approve_ok",
                "timesheet_approve_grp_ids"),
            ("refuse_ok",
                "timesheet_refuse_grp_ids"),
            ("set2draft_ok",
                "timesheet_set2draft_grp_ids"),
        ]

    @api.multi
    def _get_timesheet_button_policy(self, policy_field):
        self.ensure_one()
        result = False
        button_group_ids = []
        user = self.env.user
        group_ids = user.groups_id.ids

        button_group_ids += getattr(
            self, policy_field).ids

        if not button_group_ids:
            result = True
        else:
            if (set(button_group_ids) & set(group_ids)):
                result = True
        return result
