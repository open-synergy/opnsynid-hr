# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


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
    schedule_change_confirm_grp_ids = fields.Many2one(
        string="Allowed To Confirm Attendance Schedule Change",
        comodel_name="res.groups",
        related="company_id.schedule_change_confirm_grp_ids",
    )
    schedule_change_approve_grp_ids = fields.Many2one(
        string="Allowed To Approve Attendance Schedule Change",
        comodel_name="res.groups",
        related="company_id.schedule_change_approve_grp_ids",
    )
    schedule_change_cancel_grp_ids = fields.Many2one(
        string="Allowed To Cancel Attendance Schedule Change",
        comodel_name="res.groups",
        related="company_id.schedule_change_cancel_grp_ids",
    )
    schedule_change_restart_grp_ids = fields.Many2one(
        string="Allowed To Restart Attendance Schedule Change",
        comodel_name="res.groups",
        related="company_id.schedule_change_restart_grp_ids",
    )
