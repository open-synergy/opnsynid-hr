# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    early_attendance_buffer = fields.Float(
        string="Early Attendance Buffer",
        default=0.0,
        required=True,
    )
    late_attendance_buffer = fields.Float(
        string="Late Attendance Buffer",
        default=0.0,
        required=True,
    )
    schedule_change_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Attendance Schedule Change",
        comodel_name="res.groups",
        relation="rel_company_2_group_schedule_change_confirm",
        column1="company_id",
        column2="group_id",
    )
    schedule_change_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel Attendance Schedule Change",
        comodel_name="res.groups",
        relation="rel_company_2_group_schedule_change_cancel",
        column1="company_id",
        column2="group_id",
    )
    schedule_change_restart_grp_ids = fields.Many2many(
        string="Allowed To Approve Attendance Schedule Change",
        comodel_name="res.groups",
        relation="rel_company_2_group_schedule_change_restart",
        column1="company_id",
        column2="group_id",
    )
    schedule_change_restart_val_grp_ids = fields.Many2many(
        string="Allow To Restart Approval",
        comodel_name="res.groups",
        relation="rel_company_2_group_schedule_change_restart_val",
        column1="company_id",
        column2="group_id",
    )
    max_att_sign_in = fields.Integer(
        string="Maximum Of Sign In",
        default=0,
        required=False,
    )
    max_att_sign_out = fields.Integer(
        string="Maximum Of Sign Out",
        default=0,
        required=False,
    )
