# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

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

    # Timesheet
    module_ssi_timesheet_attendance = fields.Boolean(
        string="Attendance",
    )
    # module_ssi_timesheet_attendance_related_attachment = fields.Boolean(
    #     "Attendance - Related Attachment",
    # )
    # module_ssi_timesheet_attendance_custom_information = fields.Boolean(
    #     "Attendance - Custom Information",
    # )
    # module_ssi_timesheet_attendance_status_check = fields.Boolean(
    #     "Attendance - Status Check",
    # )
    # module_ssi_timesheet_attendance_state_change_constrains = fields.Boolean(
    #     "Attendance - State Change Constrains",
    # )
    # module_ssi_timesheet_attendance_qrcode = fields.Boolean(
    #     "Attendance - QR Code",
    # )

    # Worklog
    module_ssi_work_log_mixin = fields.Boolean(
        string="Worklog",
    )
    # module_ssi_worklog_mixin_related_attachment = fields.Boolean(
    #     "Worklog - Related Attachment",
    # )
    # module_ssi_worklog_mixin_custom_information = fields.Boolean(
    #     "Worklog - Custom Information",
    # )
    # module_ssi_worklog_mixin_status_check = fields.Boolean(
    #     "Worklog - Status Check",
    # )
    # module_ssi_worklog_mixin_state_change_constrains = fields.Boolean(
    #     "Worklog - State Change Constrains",
    # )
    # module_ssi_worklog_mixin_qrcode = fields.Boolean(
    #     "Worklog - QR Code",
    # )

    # Holiday
    module_ssi_hr_holiday = fields.Boolean(
        string="Holiday",
    )

    # Overtime
    module_ssi_hr_overtime = fields.Boolean(
        string="Overtime",
    )
    # module_ssi_hr_overtime_related_attachment = fields.Boolean(
    #     "Overtime - Related Attachment",
    # )
    # module_ssi_hr_overtime_custom_information = fields.Boolean(
    #     "Overtime - Custom Information",
    # )
    # module_ssi_hr_overtime_status_check = fields.Boolean(
    #     "Overtime - Status Check",
    # )
    # module_ssi_hr_overtime_state_change_constrains = fields.Boolean(
    #     "Overtime - State Change Constrains",
    # )
    # module_ssi_hr_overtime_qrcode = fields.Boolean(
    #     "Overtime - QR Code",
    # )

    # Payroll
    module_ssi_hr_payroll = fields.Boolean(
        string="Payslip",
    )
    module_ssi_hr_payroll_batch = fields.Boolean(
        string="Payslip Batch",
    )
    # module_ssi_hr_payroll_related_attachment = fields.Boolean(
    #     "Payroll - Related Attachment",
    # )
    # module_ssi_hr_payroll_custom_information = fields.Boolean(
    #     "Payroll - Custom Information",
    # )
    # module_ssi_hr_payroll_status_check = fields.Boolean(
    #     "Payroll - Status Check",
    # )
    # module_ssi_hr_payroll_state_change_constrains = fields.Boolean(
    #     "Payroll - State Change Constrains",
    # )
    # module_ssi_hr_payroll_qrcode = fields.Boolean(
    #     "Payroll - QR Code",
    # )

    # Reimbursement
    module_ssi_hr_reimbursement = fields.Boolean(
        string="Reimbursement",
    )
    # module_ssi_hr_reimbursement_related_attachment = fields.Boolean(
    #     "Reimbursement - Related Attachment",
    # )
    # module_ssi_hr_reimbursement_custom_information = fields.Boolean(
    #     "Reimbursement - Custom Information",
    # )
    # module_ssi_hr_reimbursement_status_check = fields.Boolean(
    #     "Reimbursement - Status Check",
    # )
    # module_ssi_hr_reimbursement_state_change_constrains = fields.Boolean(
    #     "Reimbursement - State Change Constrains",
    # )
    # module_ssi_hr_reimbursement_qrcode = fields.Boolean(
    #     "Reimbursement - QR Code",
    # )

    # Cash Advance
    module_ssi_hr_cash_advance = fields.Boolean(
        string="Cash Advance",
    )

    # Expense Account
    module_ssi_hr_expense_account = fields.Boolean(
        string="Expense Account",
    )
    # module_ssi_hr_expense_account_related_attachment = fields.Boolean(
    #     "Expense Account - Related Attachment",
    # )
    # module_ssi_hr_expense_account_custom_information = fields.Boolean(
    #     "Expense Account - Custom Information",
    # )
    # module_ssi_hr_expense_account_status_check = fields.Boolean(
    #     "Expense Account - Status Check",
    # )
    # module_ssi_hr_expense_account_state_change_constrains = fields.Boolean(
    #     "Expense Account - State Change Constrains",
    # )
    # module_ssi_hr_expense_account_qrcode = fields.Boolean(
    #     "Expense Account - QR Code",
    # )
