# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrAwardType(models.Model):
    _name = "hr.award_type"
    _description = "Award Type"

    name = fields.Char(
        string="Award Type",
        required=True,
    )
    code = fields.Char(
        string="Code",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(
        string="Note"
    )
    reason_ids = fields.One2many(
        string="Award Reason",
        comodel_name="hr.award_reason",
        inverse_name="award_type_id",
    )
    sequence_id = fields.Many2one(
        string="Sequence",
        comodel_name="ir.sequence",
        ondelete="set null",
        company_dependent=True,
    )
    award_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Employee Award",
        comodel_name="res.groups",
        relation="rel_award_type_2_group_award_confirm",
        column1="award_type_id",
        column2="group_id",
    )
    award_approve_grp_ids = fields.Many2many(
        string="Allowed To Approve Employee Award",
        comodel_name="res.groups",
        relation="rel_award_type_2_group_award_approve",
        column1="award_type_id",
        column2="group_id",
    )
    award_open_grp_ids = fields.Many2many(
        string="Allowed To Open Employee Award",
        comodel_name="res.groups",
        relation="rel_award_type_2_group_award_open",
        column1="award_type_id",
        column2="group_id",
    )
    award_done_grp_ids = fields.Many2many(
        string="Allowed To Finish Employee Award",
        comodel_name="res.groups",
        relation="rel_award_type_2_group_award_done",
        column1="award_type_id",
        column2="group_id",
    )
    award_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel Employee Award",
        comodel_name="res.groups",
        relation="rel_award_type_2_group_award_cancel",
        column1="award_type_id",
        column2="group_id",
    )
    award_restart_grp_ids = fields.Many2many(
        string="Allowed To Restart Employee Award",
        comodel_name="res.groups",
        relation="rel_award_type_2_group_award_restart",
        column1="award_type_id",
        column2="group_id",
    )
