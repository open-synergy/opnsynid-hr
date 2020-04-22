# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, fields, api


class WizardTimesheetAutoInput(models.TransientModel):
    _name = "hr_timesheet_sheet.sheet.auto_input"
    _description = "Timesheet Auto Input"

    timesheet_account_id = fields.Many2one(
        string="Timesheet Account",
        comodel_name="account.analytic.account",
        domain=[("type", "<>", "view")],
    )
    task_id = fields.Many2one(
        string="Task",
        comodel_name="project.task",
    )
    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.product",
        domain=[("type", "=", "service")],
    )
    description = fields.Text(
        string="Description",
    )

    @api.multi
    @api.onchange(
        "timesheet_account_id",
    )
    def onchange_task_id(self):
        self.task_id = False
        if self.timesheet_account_id:
            obj_project = self.env["project.project"]
            criteria = [
                ("analytic_account_id", "=", self.timesheet_account_id.id)
            ]
            project_ids = obj_project.search(criteria)
            if project_ids:
                task_id = project_ids.tasks.ids
            return {"domain": {"task_id": [("id", "in", task_id)]}}

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
            "current_product_id": self.product_id.id,
            "current_task_id": self.task_id.id,
        }

    @api.multi
    def _prepare_absent_data(self):
        self.ensure_one()
        return {
            "current_timesheet_account_id": False,
            "current_product_id": False,
            "current_task_id": False,
        }

    @api.multi
    def _prepare_analytic_timesheet_data(self, sheet_ids):
        self.ensure_one()
        account_id =\
            sheet_ids.current_timesheet_account_id.id
        task_id =\
            sheet_ids.current_task_id.id
        product_id =\
            sheet_ids.current_product_id.id
        journal_id =\
            sheet_ids.employee_id.journal_id.id
        difference =\
            sheet_ids.total_difference

        return {
            "sheet_id": sheet_ids.id,
            "name": self.description,
            "account_id": account_id,
            "task_id": task_id,
            "product_id": product_id,
            "journal_id": journal_id,
            "unit_amount": difference,
        }

    @api.multi
    def create_analytic_timesheet(self, sheet_ids):
        obj_hr_analytic_timesheet =\
            self.env["hr.analytic.timesheet"]
        obj_hr_analytic_timesheet.create(
            self._prepare_analytic_timesheet_data(sheet_ids))
        return True

    @api.multi
    def action_ok(self):
        self.ensure_one()
        obj_hr_timesheet_sheet =\
            self.env["hr_timesheet_sheet.sheet"]
        active_id = self.env.context.get("active_id", False)

        criteria = [
            ("id", "=", active_id)
        ]
        hr_timesheet_sheet_ids =\
            obj_hr_timesheet_sheet.search(criteria)

        if self.state_attendance == "present":
            hr_timesheet_sheet_ids.write(self._prepare_present_data())
        else:
            self.create_analytic_timesheet(hr_timesheet_sheet_ids)
            hr_timesheet_sheet_ids.write(self._prepare_absent_data())

        hr_timesheet_sheet_ids.attendance_action_change()
        return {"type": "ir.actions.act_window_close"}
