# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrAttendanceMachine(models.Model):
    _name = "hr.attendance_machine"
    _description = "Attendance Machine"

    name = fields.Char(
        string="Name",
        required=True,
    )
    date_format = fields.Selection(
        string="Date Format",
        selection=[
            ("%d/%m/%Y", "dd/mm/yyyy"),
            ("%m/%d/%Y", "mm/dd/yyyy"),
            ("%Y/%m/%d", "yyyy/mm/dd")
        ],
        required=True,
    )
    time_format = fields.Selection(
        string="Time Format",
        selection=[
            ("%H:%M:%S", "HH:MM:SS"),
            ("%H:%M", "HH:MM"),
            ("%H%M", "HHMM")
        ],
        required=True,
    )
    sign_in_code = fields.Char(
        string="Sign In Code",
        required=True,
    )
    sign_out_code = fields.Char(
        string="Sign Out Code",
        required=True,
    )
    delimiter = fields.Char(
        string="Delimiter",
        default=",",
        required=True,
    )
    first_row_header = fields.Boolean(
        string="First Row Header",
    )
    csv_detail_ids = fields.One2many(
        string="CSV Details",
        comodel_name="hr.attendance_machine_csv_detail",
        inverse_name="attendance_machine_id",
    )
    employee_code_ids = fields.One2many(
        string="Employee Code",
        comodel_name="hr.attendance_machine_employee_code",
        inverse_name="attendance_machine_id",
    )
