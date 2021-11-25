# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class HrDiciplineType(models.Model):
    _name = "hr.dicipline_type"
    _description = "Dicipline Type"

    name = fields.Char(
        string="Dicipline Type",
        required=True,
    )
    code = fields.Char(
        string="Code",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(string="Note")
    reason_ids = fields.One2many(
        string="Dicipline Reason",
        comodel_name="hr.dicipline_reason",
        inverse_name="dicipline_type_id",
    )
    sequence_id = fields.Many2one(
        string="Sequence",
        comodel_name="ir.sequence",
        ondelete="set null",
        company_dependent=True,
    )
    dicipline_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Employee Dicipline",
        comodel_name="res.groups",
        relation="rel_dicipline_type_2_group_dicipline_confirm",
        column1="dicipline_type_id",
        column2="group_id",
    )
    dicipline_open_grp_ids = fields.Many2many(
        string="Allowed To Open Employee Dicipline",
        comodel_name="res.groups",
        relation="rel_dicipline_type_2_group_dicipline_open",
        column1="dicipline_type_id",
        column2="group_id",
    )
    dicipline_done_grp_ids = fields.Many2many(
        string="Allowed To Finish Employee Dicipline",
        comodel_name="res.groups",
        relation="rel_dicipline_type_2_group_dicipline_done",
        column1="dicipline_type_id",
        column2="group_id",
    )
    dicipline_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel Employee Dicipline",
        comodel_name="res.groups",
        relation="rel_dicipline_type_2_group_dicipline_cancel",
        column1="dicipline_type_id",
        column2="group_id",
    )
    dicipline_restart_grp_ids = fields.Many2many(
        string="Allowed To Restart Employee Dicipline",
        comodel_name="res.groups",
        relation="rel_dicipline_type_2_group_dicipline_restart",
        column1="dicipline_type_id",
        column2="group_id",
    )
    dicipline_restart_val_grp_ids = fields.Many2many(
        string="Allowed To Restart Validation Employee Dicipline",
        comodel_name="res.groups",
        relation="rel_dicipline_type_2_group_dicipline_restart_val",
        column1="dicipline_type_id",
        column2="group_id",
    )
