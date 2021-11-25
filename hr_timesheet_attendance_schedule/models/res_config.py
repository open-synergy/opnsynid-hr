# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ResConfig(models.TransientModel):
    _inherit = "hr.attendance_config_setting"

    early_attendance_buffer = fields.Float(
        string="Early Attendance Buffer",
        related="company_id.early_attendance_buffer",
    )
    late_attendance_buffer = fields.Float(
        string="Late Attendance Buffer",
        related="company_id.late_attendance_buffer",
    )
    schedule_change_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Attendance Schedule Change",
        comodel_name="res.groups",
        related="company_id.schedule_change_confirm_grp_ids",
    )
    schedule_change_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel Attendance Schedule Change",
        comodel_name="res.groups",
        related="company_id.schedule_change_cancel_grp_ids",
    )
    schedule_change_restart_grp_ids = fields.Many2many(
        string="Allowed To Restart Attendance Schedule Change",
        comodel_name="res.groups",
        related="company_id.schedule_change_restart_grp_ids",
    )
    schedule_change_restart_val_grp_ids = fields.Many2many(
        string="Allowed To Restart Approval",
        comodel_name="res.groups",
        related="company_id.schedule_change_restart_val_grp_ids",
    )
    max_att_sign_in = fields.Integer(
        string="Maximum Of Sign In",
        related="company_id.max_att_sign_in",
    )
    max_att_sign_out = fields.Integer(
        string="Maximum Of Sign Out",
        related="company_id.max_att_sign_out",
    )
