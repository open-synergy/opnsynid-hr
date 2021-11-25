# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    payslip_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm",
        comodel_name="res.groups",
        relation="rel_payslip_allowed_confirm_groups",
        column1="company_id",
        column2="group_id",
    )
    payslip_refund_grp_ids = fields.Many2many(
        string="Allowed To Refund",
        comodel_name="res.groups",
        relation="rel_payslip_allowed_refund_groups",
        column1="company_id",
        column2="group_id",
    )
    payslip_compute_grp_ids = fields.Many2many(
        string="Allowed To Compute Sheet",
        comodel_name="res.groups",
        relation="rel_payslip_allowed_compute_groups",
        column1="company_id",
        column2="group_id",
    )
    payslip_set2draft_grp_ids = fields.Many2many(
        string="Allowed To Set To Draft",
        comodel_name="res.groups",
        relation="rel_payslip_allowed_set2draft_groups",
        column1="company_id",
        column2="group_id",
    )
    payslip_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel",
        comodel_name="res.groups",
        relation="rel_payslip_allowed_cancel_groups",
        column1="company_id",
        column2="group_id",
    )
    payslip_run_close_grp_ids = fields.Many2many(
        string="Allowed To Close",
        comodel_name="res.groups",
        relation="rel_payslip_run_allowed_close_groups",
        column1="company_id",
        column2="group_id",
    )
    payslip_run_generate_grp_ids = fields.Many2many(
        string="Allowed To Generate Payslips",
        comodel_name="res.groups",
        relation="rel_payslip_run_allowed_generate_groups",
        column1="company_id",
        column2="group_id",
    )
    payslip_run_set2draft_grp_ids = fields.Many2many(
        string="Allowed To Compute Sheet",
        comodel_name="res.groups",
        relation="rel_payslip_run_allowed_set2draft_groups",
        column1="company_id",
        column2="group_id",
    )

    @api.model
    def _get_payslip_button_policy_map(self):
        return [
            ("confirm_ok", "payslip_confirm_grp_ids"),
            ("refund_ok", "payslip_refund_grp_ids"),
            ("compute_ok", "payslip_compute_grp_ids"),
            ("set2draft_ok", "payslip_set2draft_grp_ids"),
            ("cancel_ok", "payslip_cancel_grp_ids"),
        ]

    @api.model
    def _get_payslip_run_button_policy_map(self):
        return [
            ("close_ok", "payslip_run_close_grp_ids"),
            ("generate_ok", "payslip_run_generate_grp_ids"),
            ("set2draft_ok", "payslip_run_set2draft_grp_ids"),
        ]

    @api.multi
    def _get_payslip_button_policy(self, policy_field):
        self.ensure_one()
        result = False
        button_group_ids = []
        user = self.env.user
        group_ids = user.groups_id.ids

        button_group_ids += getattr(self, policy_field).ids

        if not button_group_ids:
            result = True
        else:
            if set(button_group_ids) & set(group_ids):
                result = True
        return result
