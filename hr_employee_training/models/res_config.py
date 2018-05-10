# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ResConfig(models.TransientModel):
    _name = "hr.training.config.setting"
    _inherit = "res.config.settings"

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id.id

    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        required=True,
        default=lambda self: self._default_company_id(),
    )
    employee_training_allowed_confirm_group_ids = fields.Many2many(
        string="Allowed Confirm Employee Training",
        comodel_name="res.groups",
        relation="rel_company_emp_training_allowed_confirm",
        column1="company_id",
        column2="group_id",
        related="company_id.employee_training_allowed_confirm_group_ids",
    )
    employee_training_allowed_approve_group_ids = fields.Many2many(
        string="Allowed Approve Employee Training",
        comodel_name="res.groups",
        relation="rel_company_emp_training_allowed_approve",
        column1="company_id",
        column2="group_id",
        related="company_id.employee_training_allowed_approve_group_ids",
    )
    employee_training_allowed_start_group_ids = fields.Many2many(
        string="Allowed Start Employee Training",
        comodel_name="res.groups",
        relation="rel_company_emp_training_allowed_start",
        column1="company_id",
        column2="group_id",
        related="company_id.employee_training_allowed_start_group_ids",
    )
    employee_training_allowed_finish_group_ids = fields.Many2many(
        string="Allowed Finish Employee Training",
        comodel_name="res.groups",
        relation="rel_company_emp_training_allowed_finish",
        column1="company_id",
        column2="group_id",
        related="company_id.employee_training_allowed_finish_group_ids",
    )
    employee_training_allowed_cancel_group_ids = fields.Many2many(
        string="Allowed Cancel Employee Training",
        comodel_name="res.groups",
        relation="rel_company_emp_training_allowed_cancel",
        column1="company_id",
        column2="group_id",
        related="company_id.employee_training_allowed_cancel_group_ids",
    )
    employee_training_allowed_restart_group_ids = fields.Many2many(
        string="Allowed Restart Employee Training",
        comodel_name="res.groups",
        relation="rel_company_emp_training_allowed_restart",
        column1="company_id",
        column2="group_id",
        related="company_id.employee_training_allowed_restart_group_ids",
    )
    module_hr_employee_training_allowance = fields.Boolean(
        string="Manage Training Allowance",
    )
    module_hr_employee_training_budget = fields.Boolean(
        string="Manage Training Budget",
    )
    module_hr_employee_training_experience = fields.Boolean(
        string="Experience",
    )
    module_hr_employee_training_analytic = fields.Boolean(
        string="Analytic Account",
    )
    module_hr_employee_training_job_family_modelling = fields.Boolean(
        string="Job Family Modelling",
    )
    module_hr_employee_training_organization_unit = fields.Boolean(
        string="Organization Unit",
    )
