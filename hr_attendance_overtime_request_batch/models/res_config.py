# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResConfig(models.TransientModel):
    _inherit = "hr.overtime_config_setting"

    overtime_request_batch_sequence_id = fields.Many2one(
        string="Overtime Request Batch Sequence",
        comodel_name="ir.sequence",
        related="company_id.overtime_request_batch_sequence_id",
    )
    overtime_request_batch_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Overtime Request",
        comodel_name="res.groups",
        relation="rel_overtime_request_batch_allowed_confirm_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.overtime_request_batch_confirm_grp_ids",
    )
    overtime_request_batch_valid_grp_ids = fields.Many2many(
        string="Allowed To Validate Overtime Request",
        comodel_name="res.groups",
        relation="rel_overtime_request_batch_allowed_valid_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.overtime_request_batch_valid_grp_ids",
    )
    overtime_request_batch_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel Overtime Request",
        comodel_name="res.groups",
        relation="rel_overtime_request_batch_allowed_cancel_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.overtime_request_batch_cancel_grp_ids",
    )
    overtime_request_batch_restart_grp_ids = fields.Many2many(
        string="Allowed To Restart Overtime Request",
        comodel_name="res.groups",
        relation="rel_overtime_request_batch_allowed_restart_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.overtime_request_batch_restart_grp_ids",
    )
    overtime_request_batch_generate_grp_ids = fields.Many2many(
        string="Allowed To Generate Overtime Request",
        comodel_name="res.groups",
        relation="rel_overtime_request_batch_allowed_generate_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.overtime_request_batch_generate_grp_ids",
    )
