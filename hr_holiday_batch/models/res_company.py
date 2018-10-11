# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ResCompany(models.Model):
    _inherit = "res.company"

    leave_request_batch_sequence_id = fields.Many2one(
        string="Leave Request Batch Sequence",
        comodel_name="ir.sequence",
    )
    leave_request_batch_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Leave Request Batch",
        comodel_name="res.groups",
        relation="rel_leave_request_batch_allowed_confirm_groups",
        column1="company_id",
        column2="group_id",
    )
    leave_request_batch_valid_grp_ids = fields.Many2many(
        string="Allowed To Validate Leave Request Batch",
        comodel_name="res.groups",
        relation="rel_leave_request_batch_allowed_valid_groups",
        column1="company_id",
        column2="group_id",
    )
    leave_request_batch_refuse_grp_ids = fields.Many2many(
        string="Allowed To Refuse Leave Request Batch",
        comodel_name="res.groups",
        relation="rel_leave_request_batch_allowed_refuse_groups",
        column1="company_id",
        column2="group_id",
    )
    leave_request_batch_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel Leave Request Batch",
        comodel_name="res.groups",
        relation="rel_leave_request_batch_allowed_cancel_groups",
        column1="company_id",
        column2="group_id",
    )
    leave_request_batch_restart_grp_ids = fields.Many2many(
        string="Allowed To Restart Leave Request Batch",
        comodel_name="res.groups",
        relation="rel_leave_request_batch_allowed_restart_groups",
        column1="company_id",
        column2="group_id",
    )
    leave_request_batch_generate_grp_ids = fields.Many2many(
        string="Allowed To Generate Leave Request Batch",
        comodel_name="res.groups",
        relation="rel_leave_request_batch_allowed_generate_groups",
        column1="company_id",
        column2="group_id",
    )
    allocation_request_batch_sequence_id = fields.Many2one(
        string="Allocation Request Batch Sequence",
        comodel_name="ir.sequence",
    )
    allocation_request_batch_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Allocation Request Batch",
        comodel_name="res.groups",
        relation="rel_allocation_request_batch_allowed_confirm_groups",
        column1="company_id",
        column2="group_id",
    )
    allocation_request_batch_valid_grp_ids = fields.Many2many(
        string="Allowed To Validate Allocation Request Batch",
        comodel_name="res.groups",
        relation="rel_allocation_request_batch_allowed_valid_groups",
        column1="company_id",
        column2="group_id",
    )
    allocation_request_batch_refuse_grp_ids = fields.Many2many(
        string="Allowed To Refuse Allocation Request Batch",
        comodel_name="res.groups",
        relation="rel_allocation_request_batch_allowed_refuse_groups",
        column1="company_id",
        column2="group_id",
    )
    allocation_request_batch_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel Allocation Request Batch",
        comodel_name="res.groups",
        relation="rel_allocation_request_batch_allowed_cancel_groups",
        column1="company_id",
        column2="group_id",
    )
    allocation_request_batch_restart_grp_ids = fields.Many2many(
        string="Allowed To Restart Allocation Request Batch",
        comodel_name="res.groups",
        relation="rel_allocation_request_batch_allowed_restart_groups",
        column1="company_id",
        column2="group_id",
    )
    allocation_request_batch_generate_grp_ids = fields.Many2many(
        string="Allowed To Generate Allocation Request Batch",
        comodel_name="res.groups",
        relation="rel_allocation_request_batch_allowed_generate_groups",
        column1="company_id",
        column2="group_id",
    )

    @api.model
    def _get_leave_batch_button_policy_map(self):
        return [
            ("confirm_ok",
                "leave_request_batch_confirm_grp_ids"),
            ("valid_ok",
                "leave_request_batch_valid_grp_ids"),
            ("cancel_ok",
                "leave_request_batch_cancel_grp_ids"),
            ("refuse_ok",
                "leave_request_batch_refuse_grp_ids"),
            ("restart_ok",
                "leave_request_batch_restart_grp_ids"),
            ("generate_ok",
                "leave_request_batch_generate_grp_ids"),
        ]

    @api.model
    def _get_allocation_batch_button_policy_map(self):
        return [
            ("confirm_ok",
                "allocation_request_batch_confirm_grp_ids"),
            ("valid_ok",
                "allocation_request_batch_valid_grp_ids"),
            ("cancel_ok",
                "allocation_request_batch_cancel_grp_ids"),
            ("refuse_ok",
                "allocation_request_batch_refuse_grp_ids"),
            ("restart_ok",
                "allocation_request_batch_restart_grp_ids"),
            ("generate_ok",
                "allocation_request_batch_generate_grp_ids"),
        ]

    @api.multi
    def _get_holiday_batch_button_policy(self, policy_field):
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
