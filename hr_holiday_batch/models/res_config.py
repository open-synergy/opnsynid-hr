# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResConfig(models.TransientModel):
    _inherit = "hr.holiday_config_setting"

    leave_request_batch_sequence_id = fields.Many2one(
        string="Leave Request Batch Sequence",
        comodel_name="ir.sequence",
        related="company_id.leave_request_batch_sequence_id",
    )
    leave_request_batch_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Leave Request Batch",
        comodel_name="res.groups",
        relation="rel_leave_request_batch_allowed_confirm_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.leave_request_batch_confirm_grp_ids",
    )
    leave_request_batch_valid_grp_ids = fields.Many2many(
        string="Allowed To Validate Leave Request Batch",
        comodel_name="res.groups",
        relation="rel_leave_request_batch_allowed_valid_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.leave_request_batch_valid_grp_ids",
    )
    leave_request_batch_refuse_grp_ids = fields.Many2many(
        string="Allowed To Refuse Leave Request Batch",
        comodel_name="res.groups",
        relation="rel_leave_request_batch_allowed_refuse_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.leave_request_batch_refuse_grp_ids",
    )
    leave_request_batch_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel Leave Request Batch",
        comodel_name="res.groups",
        relation="rel_leave_request_batch_allowed_cancel_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.leave_request_batch_cancel_grp_ids",
    )
    leave_request_batch_restart_grp_ids = fields.Many2many(
        string="Allowed To Restart Leave Request Batch",
        comodel_name="res.groups",
        relation="rel_leave_request_batch_allowed_restart_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.leave_request_batch_restart_grp_ids",
    )
    leave_request_batch_generate_grp_ids = fields.Many2many(
        string="Allowed To Generate Leave Request Batch",
        comodel_name="res.groups",
        relation="rel_leave_request_batch_allowed_generate_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.leave_request_batch_generate_grp_ids",
    )
    allocation_request_batch_sequence_id = fields.Many2one(
        string="Allocation Request Batch Sequence",
        comodel_name="ir.sequence",
        related="company_id.allocation_request_batch_sequence_id",
    )
    allocation_request_batch_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Allocation Request Batch",
        comodel_name="res.groups",
        relation="rel_allocation_request_batch_allowed_confirm_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.allocation_request_batch_confirm_grp_ids",
    )
    allocation_request_batch_valid_grp_ids = fields.Many2many(
        string="Allowed To Validate Allocation Request Batch",
        comodel_name="res.groups",
        relation="rel_allocation_request_batch_allowed_valid_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.allocation_request_batch_valid_grp_ids",
    )
    allocation_request_batch_refuse_grp_ids = fields.Many2many(
        string="Allowed To Refuse Allocation Request Batch",
        comodel_name="res.groups",
        relation="rel_allocation_request_batch_allowed_refuse_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.allocation_request_batch_refuse_grp_ids",
    )
    allocation_request_batch_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel Allocation Request Batch",
        comodel_name="res.groups",
        relation="rel_allocation_request_batch_allowed_cancel_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.allocation_request_batch_cancel_grp_ids",
    )
    allocation_request_batch_restart_grp_ids = fields.Many2many(
        string="Allowed To Restart Allocation Request Batch",
        comodel_name="res.groups",
        relation="rel_allocation_request_batch_allowed_restart_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.allocation_request_batch_restart_grp_ids",
    )
    allocation_request_batch_generate_grp_ids = fields.Many2many(
        string="Allowed To Generate Allocation Request Batch",
        comodel_name="res.groups",
        relation="rel_allocation_request_batch_allowed_generate_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.allocation_request_batch_generate_grp_ids",
    )
