# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrCareerTransitionType(models.Model):
    _name = "hr.career_transition_type"
    _description = "Career Transition Type"

    name = fields.Char(
        string="Career Transition Type",
        required=True
    )
    code = fields.Char(
        string="Code",
    )
    description = fields.Text(
        string="Description"
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )
    require_reason = fields.Boolean(
        string="Require Reason",
    )
    reason_ids = fields.One2many(
        string="Reasons",
        comodel_name="hr.career_transition_type_reason",
        inverse_name="type_id",
    )
    # Config
    limit = fields.Integer(
        string="Transition Limit",
        default=0,
    )
    need_previous_contract = fields.Boolean(
        string="Need Previous Contract",
    )
    create_new_contract = fields.Boolean(
        string="Create New Contract",
    )
    # What to change
    change_company = fields.Boolean(
        string="Change Company?",
    )
    change_job_title = fields.Boolean(
        string="Change Job Title",
    )
    change_department = fields.Boolean(
        string="Change Department",
    )
    change_working_schedule = fields.Boolean(
        string="Change Working Schedule",
    )
    change_wage = fields.Boolean(
        string="Change Wage",
    )

    sequence_id = fields.Many2one(
        string="Sequence",
        comodel_name="ir.sequence",
        company_dependent=True,
    )
    confirm_grp_ids = fields.Many2many(
        string="Allowed to Confirm",
        comodel_name="res.groups",
        relation="rel_confirm_career_transition",
        column1="type_id",
        column2="group_id",
    )
    approve_grp_ids = fields.Many2many(
        string="Allowed to Approve",
        comodel_name="res.groups",
        relation="rel_approve_career_transition",
        column1="type_id",
        column2="group_id",
    )
    open_grp_ids = fields.Many2many(
        string="Allowed to Start Process",
        comodel_name="res.groups",
        relation="rel_open_career_transition",
        column1="type_id",
        column2="group_id",
    )
    valid_grp_ids = fields.Many2many(
        string="Allowed to Validate",
        comodel_name="res.groups",
        relation="rel_finish_career_transition",
        column1="type_id",
        column2="group_id",
    )
    cancel_grp_ids = fields.Many2many(
        string="Allowed to Cancel",
        comodel_name="res.groups",
        relation="rel_cancel_career_transition",
        column1="type_id",
        column2="group_id",
    )
    restart_grp_ids = fields.Many2many(
        string="Allowed to Restart",
        comodel_name="res.groups",
        relation="rel_finish_career_transition",
        column1="type_id",
        column2="group_id",
    )

    @api.multi
    def _get_transition_limit(self, transition_reason):
        self.ensure_one()
        limit = 0
        if transition_reason:
            limit = transition_reason.limit
        else:
            limit = self.limit
        return limit
