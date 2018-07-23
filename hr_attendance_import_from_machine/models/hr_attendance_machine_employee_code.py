# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api, _
from openerp.exceptions import Warning as UserError


class HrAttendanceMachineEmployeeCode(models.Model):
    _name = "hr.attendance_machine_employee_code"
    _description = "Attendance Machine's Employee Code"

    attendance_machine_id = fields.Many2one(
        string="Machine",
        comodel_name="hr.attendance_machine",
    )
    employee_id = fields.Many2one(
        string="Employee",
        comodel_name="hr.employee",
        required=True,
    )
    employee_code_machine = fields.Char(
        string="Employee Code Machine",
        required=True,
    )

    @api.constrains("attendance_machine_id", "employee_id")
    def _check_duplicate_employee(self):
        obj_machine = self.env["hr.attendance_machine_employee_code"]
        criteria = [
            ("id", "!=", self.id),
            ("employee_id", "=", self.employee_id.id),
            ("attendance_machine_id", "=", self.attendance_machine_id.id),
        ]
        result = obj_machine.search_count(criteria)
        if result > 0:
            raise UserError(_("Duplicate employee"))
