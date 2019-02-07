# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ResConfig(models.TransientModel):
    _name = "hr.career_administration_config_setting"
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
    module_hr_join_transition = fields.Boolean(
        string="Manage Join Transition",
    )
    module_hr_mutation_transition = fields.Boolean(
        string="Manage Mutation Transition",
    )
    module_hr_promotion_transition = fields.Boolean(
        string="Manage Promotion Transition",
    )
    module_hr_demotion_transition = fields.Boolean(
        string="Manage Demotion Transition",
    )
    module_hr_assignment_transition = fields.Boolean(
        string="Manage New Assignment Transition",
    )
    module_hr_termination_transition = fields.Boolean(
        string="Manage Termination Transition",
    )

    module_hr_career_transition_payroll = fields.Boolean(
        string="Payroll",
    )
    module_hr_career_transition_payroll_account = fields.Boolean(
        string="Payroll With Accounting",
    )
    module_hr_career_transition_payslip_input_policy = fields.Boolean(
        string="Payslip Input Type Policy",
    )
    module_hr_career_timesheet_computation = fields.Boolean(
        string="Timesheet Computation",
    )
