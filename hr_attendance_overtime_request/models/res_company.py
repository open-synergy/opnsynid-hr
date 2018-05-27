# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ResCompany(models.Model):
    _inherit = "res.company"

    overtime_request_sequence_id = fields.Many2one(
        string="Overtime Request Sequence",
        comodel_name="ir.sequence",
    )
    overtime_request_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Overtime Request",
        comodel_name="res.groups",
        relation="rel_overtime_request_allowed_confirm_groups",
        column1="company_id",
        column2="group_id",
    )
    overtime_request_valid_grp_ids = fields.Many2many(
        string="Allowed To Validate Overtime Request",
        comodel_name="res.groups",
        relation="rel_overtime_request_allowed_valid_groups",
        column1="company_id",
        column2="group_id",
    )
    overtime_request_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel Overtime Request",
        comodel_name="res.groups",
        relation="rel_overtime_request_allowed_cancel_groups",
        column1="company_id",
        column2="group_id",
    )
    overtime_request_restart_grp_ids = fields.Many2many(
        string="Allowed To Restart Overtime Request",
        comodel_name="res.groups",
        relation="rel_overtime_request_allowed_restart_groups",
        column1="company_id",
        column2="group_id",
    )

    @api.model
    def _get_partner_arrangement_button_policy_map(self):
        return [
            ("confirm_ok",
                "overtime_request_confirm_grp_ids"),
            ("valid_ok", "overtime_request_valid_grp_ids"),
            ("cancel_ok", "overtime_request_cancel_grp_ids"),
            ("restart_ok", "overtime_request_restart_grp_ids"),
        ]

    @api.multi
    def _get_overtime_request_button_policy(self, policy_field):
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
