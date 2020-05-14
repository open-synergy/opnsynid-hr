# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, fields, api


class WizardTimesheetAutoInput(models.TransientModel):
    _name = "hr_timesheet_sheet.sheet.auto_input"
    _description = "Timesheet Auto Input"

    @api.model
    def _default_sheet_id(self):
        active_id =\
            self.env.context.get("active_id", False)
        return active_id

    sheet_id = fields.Many2one(
        string="Timesheet",
        comodel_name="hr_timesheet_sheet.sheet",
        default=lambda self: self._default_sheet_id(),
    )
    timesheet_account_id = fields.Many2one(
        string="Timesheet Account",
        comodel_name="account.analytic.account",
        domain=[
            ("type", "<>", "view"),
            ("use_timesheets", "=", True)
        ],
    )
    description = fields.Text(
        string="Description",
    )

    @api.model
    def _default_state_attendance(self):
        state_attendance =\
            self.env.context.get("state_attendance", False)
        return state_attendance

    state_attendance = fields.Selection(
        string="State Attendance",
        selection=[
            ("present", "Present"),
            ("absent", "Absent"),
        ],
        default=lambda self: self._default_state_attendance(),
    )

    @api.multi
    def _prepare_present_data(self):
        self.ensure_one()
        return {
            "current_timesheet_account_id": self.timesheet_account_id.id,
        }

    @api.multi
    def _prepare_absent_data(self):
        self.ensure_one()
        return {
            "current_timesheet_account_id": False,
        }

    @api.multi
    def _prepare_analytic_timesheet_data(self):
        self.ensure_one()
        account_id =\
            self.sheet_id.current_timesheet_account_id.id
        journal_id =\
            self.sheet_id.employee_id.journal_id.id
        difference =\
            self.sheet_id.total_difference

        return {
            "sheet_id": self.sheet_id.id,
            "name": self.description,
            "account_id": account_id,
            "journal_id": journal_id,
            "unit_amount": difference,
        }

    @api.multi
    def create_analytic_timesheet(self):
        obj_hr_analytic_timesheet =\
            self.env["hr.analytic.timesheet"]
        obj_hr_analytic_timesheet.create(
            self._prepare_analytic_timesheet_data())
        return True

    @api.multi
    def action_ok(self):
        self.ensure_one()

        if self.state_attendance == "present":
            self.sheet_id.write(self._prepare_present_data())
        else:
            self.create_analytic_timesheet()
            self.sheet_id.write(self._prepare_absent_data())

        self.sheet_id.attendance_action_change()
        return {"type": "ir.actions.act_window_close"}
