# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime

from openerp import _, api, fields, models
from openerp.exceptions import ValidationError


class HrTimesheetMassGenerate(models.TransientModel):
    _name = "hr.timesheet_mass_generate"
    _description = "HR Timesheet Mass Generate"

    date_from = fields.Date(
        string="Date From",
        default=datetime.now().strftime("%Y-%m-%d"),
        required=True,
    )

    date_to = fields.Date(
        string="Date To",
        default=datetime.now().strftime("%Y-%m-%d"),
        required=True,
    )

    employee_ids = fields.Many2many(
        string="Employee",
        comodel_name="hr.employee",
        relation="hr_employee_generate_manual_rel",
        column1="wizard_id",
        column2="employee_id",
        required=True,
    )

    @api.constrains("date_from", "date_to")
    def _check_date(self):
        strWarning = _("Date From must be greater than Date To")
        if self.date_from and self.date_to:
            if self.date_from > self.date_to:
                raise ValidationError(strWarning)

    @api.multi
    def _prepare_data_timesheet(self, employee):
        data = {}
        if self._check_data(employee):
            data = {
                "employee_id": employee.id,
                "date_from": self.date_from,
                "date_to": self.date_to,
            }
        return data

    @api.multi
    def _check_data(self, employee):
        obj_hr_timesheet_sheet = self.env["hr_timesheet_sheet.sheet"]

        if not employee.user_id:
            raise ValidationError(
                _(
                    "Employee {name} must be linked to a user.".format(
                        name=employee.name
                    )
                )
            )

        if not employee.journal_id:
            raise ValidationError(
                _(
                    "Employee {name} must have analytic journal.".format(
                        name=employee.name
                    )
                )
            )

        criteria = [
            ("employee_id", "=", employee.id),
            ("date_from", "<=", self.date_from),
            ("date_to", ">=", self.date_to),
        ]

        timesheet_sheet = obj_hr_timesheet_sheet.search(criteria)

        if timesheet_sheet:
            raise ValidationError(
                _("Timesheet already exists for {name}.".format(name=employee.name))
            )
        return True

    @api.multi
    def button_generate(self):
        obj_hr_timesheet_sheet = self.env["hr_timesheet_sheet.sheet"]

        for employee in self.employee_ids:
            data = self._prepare_data_timesheet(employee)
            obj_hr_timesheet_sheet.create(data)

        return {"type": "ir.actions.act_window_close"}
