# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _name = "res.config.settings"
    _inherit = [
        "res.config.settings",
        "abstract.config.settings",
    ]

    module_ssi_hr_join_transition = fields.Boolean(
        string="Join Transition",
    )
    module_ssi_hr_promotion_transition = fields.Boolean(
        string="Promotion Transition",
    )
    module_ssi_hr_mutation_transition = fields.Boolean(
        string="Mutation Transition",
    )
    module_ssi_hr_demotion_transition = fields.Boolean(
        string="Demotion Transition",
    )
    module_ssi_hr_termination_transition = fields.Boolean(
        string="Termination Transition",
    )
    module_ssi_hr_new_assignment_transition = fields.Boolean(
        string="New Assignment Transition",
    )
    module_ssi_hr_award = fields.Boolean(
        string="Award",
    )
    module_ssi_hr_dicipline = fields.Boolean(
        string="Dicipline",
    )
    module_ssi_timesheet_attendance = fields.Boolean(
        string="Attendance",
    )
    module_ssi_worklog_mixin = fields.Boolean(
        string="Worklog",
    )
    module_ssi_hr_holiday = fields.Boolean(
        string="Holiday",
    )
    module_ssi_hr_overtime = fields.Boolean(
        string="Overtime",
    )
    module_ssi_hr_payroll = fields.Boolean(
        string="Payroll",
    )
    module_ssi_hr_reimbursement = fields.Boolean(
        string="Reimbursement",
    )
    module_ssi_hr_cash_advance = fields.Boolean(
        string="Cash Advance",
    )
    module_ssi_hr_expense_account = fields.Boolean(
        string="Expense Account",
    )
