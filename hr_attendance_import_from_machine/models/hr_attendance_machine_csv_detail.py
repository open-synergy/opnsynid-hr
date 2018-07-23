# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api, _
from openerp.exceptions import Warning as UserError


class HrAttendanceMachineCsvDetail(models.Model):
    _name = "hr.attendance_machine_csv_detail"
    _description = "Attendance Machiene's CSV Format"

    attendance_machine_id = fields.Many2one(
        string="Machine",
        comodel_name="hr.attendance_machine",
        required=True,
        ondelete="cascade",
    )
    csv_column = fields.Integer(
        string="Column",
        required=True,
    )
    field_id = fields.Many2one(
        string="Field",
        comodel_name="ir.model.fields",
        domain="[('model', '=', 'hr.attendance')]",
        required=True,
    )

    @api.constrains("attendance_machine_id", "csv_column")
    def _check_duplicate_column(self):
        obj_machine = self.env["hr.attendance_machine_csv_detail"]
        criteria = [
            ("id", "!=", self.id),
            ("csv_column", "=", self.csv_column),
            ("attendance_machine_id.id", "=", self.attendance_machine_id.id),
        ]
        result = obj_machine.search_count(criteria)
        if result > 0:
            raise UserError(_("Duplicate column"))

    @api.constrains("attendance_machine_id", "field_id")
    def _check_duplicate_field(self):
        obj_machine = self.env["hr.attendance_machine_csv_detail"]
        criteria = [
            ("id", "!=", self.id),
            ("field_id.id", "=", self.field_id.id),
            ("attendance_machine_id", "=", self.attendance_machine_id.id),
        ]
        result = obj_machine.search_count(criteria)
        if result > 0:
            raise UserError(_("Duplicate field"))
