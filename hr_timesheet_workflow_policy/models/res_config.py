# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResConfig(models.TransientModel):
    _inherit = "hr.attendance_config_setting"

    timesheet_submit_grp_ids = fields.Many2many(
        string="Allowed To Submit to Manager",
        comodel_name="res.groups",
        relation="rel_timesheet_allowed_submit_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.timesheet_submit_grp_ids",
    )
    timesheet_approve_grp_ids = fields.Many2many(
        string="Allowed To Approve",
        comodel_name="res.groups",
        relation="rel_timesheet_allowed_approve_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.timesheet_approve_grp_ids",
    )
    timesheet_refuse_grp_ids = fields.Many2many(
        string="Allowed To Refuse",
        comodel_name="res.groups",
        relation="rel_timesheet_allowed_refuse_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.timesheet_refuse_grp_ids",
    )
    timesheet_set2draft_grp_ids = fields.Many2many(
        string="Allowed To Set To Draft",
        comodel_name="res.groups",
        relation="rel_timesheet_allowed_set2draft_groups",
        column1="company_id",
        column2="group_id",
        related="company_id.timesheet_set2draft_grp_ids",
    )
