# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResConfig(models.TransientModel):
    _inherit = "hr.payroll_config_setting"

    payslip_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm",
        comodel_name="res.groups",
        relation="rel_payslip_allowed_confirm_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.payslip_confirm_grp_ids",
    )
    payslip_refund_grp_ids = fields.Many2many(
        string="Allowed To Refund",
        comodel_name="res.groups",
        relation="rel_payslip_allowed_refund_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.payslip_refund_grp_ids",
    )
    payslip_compute_grp_ids = fields.Many2many(
        string="Allowed To Compute Sheet",
        comodel_name="res.groups",
        relation="rel_payslip_allowed_compute_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.payslip_compute_grp_ids",
    )
    payslip_set2draft_grp_ids = fields.Many2many(
        string="Allowed To Set To Draft",
        comodel_name="res.groups",
        relation="rel_payslip_allowed_set2draft_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.payslip_set2draft_grp_ids",
    )
    payslip_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel",
        comodel_name="res.groups",
        relation="rel_payslip_allowed_cancel_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.payslip_cancel_grp_ids",
    )
    payslip_run_close_grp_ids = fields.Many2many(
        string="Allowed To Close",
        comodel_name="res.groups",
        relation="rel_payslip_run_allowed_close_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.payslip_run_close_grp_ids",
    )
    payslip_run_generate_grp_ids = fields.Many2many(
        string="Allowed To Generate Payslips",
        comodel_name="res.groups",
        relation="rel_payslip_run_allowed_generate_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.payslip_run_generate_grp_ids",
    )
    payslip_run_set2draft_grp_ids = fields.Many2many(
        string="Allowed To Compute Sheet",
        comodel_name="res.groups",
        relation="rel_payslip_run_allowed_set2draft_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.payslip_run_set2draft_grp_ids",
    )
