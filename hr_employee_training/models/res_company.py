# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    employee_training_allowed_confirm_group_ids = fields.Many2many(
        string="Allowed Confirm Employee Training",
        comodel_name="res.groups",
        relation="rel_company_emp_training_allowed_confirm",
        column1="company_id",
        column2="group_id",
    )
    employee_training_allowed_approve_group_ids = fields.Many2many(
        string="Allowed Approve Employee Training",
        comodel_name="res.groups",
        relation="rel_company_emp_training_allowed_approve",
        column1="company_id",
        column2="group_id",
    )
    employee_training_allowed_start_group_ids = fields.Many2many(
        string="Allowed Start Employee Training",
        comodel_name="res.groups",
        relation="rel_company_emp_training_allowed_start",
        column1="company_id",
        column2="group_id",
    )
    employee_training_allowed_finish_group_ids = fields.Many2many(
        string="Allowed Finish Employee Training",
        comodel_name="res.groups",
        relation="rel_company_emp_training_allowed_finish",
        column1="company_id",
        column2="group_id",
    )
    employee_training_allowed_cancel_group_ids = fields.Many2many(
        string="Allowed Cancel Employee Training",
        comodel_name="res.groups",
        relation="rel_company_emp_training_allowed_cancel",
        column1="company_id",
        column2="group_id",
    )
    employee_training_allowed_restart_group_ids = fields.Many2many(
        string="Allowed Restart Employee Training",
        comodel_name="res.groups",
        relation="rel_company_emp_training_allowed_restart",
        column1="company_id",
        column2="group_id",
    )
