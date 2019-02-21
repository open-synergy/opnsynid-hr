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
    date_format = fields.Char(
        string="Date Format",
        required=True,
    )
    time_format = fields.Char(
        string="Time Format",
        required=True,
    )
    sign_in_code = fields.Char(
        string="Sign In Code",
        required=False,
    )
    sign_out_code = fields.Char(
        string="Sign Out Code",
        required=False,
    )
    delimiter = fields.Selection(
        string="Delimiter",
        selection=[
            (",", ","),
            (";", ";"),
            (":", ":"),
            ("\t", "{tab}"),
            (" ", "{space}")
        ],
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
