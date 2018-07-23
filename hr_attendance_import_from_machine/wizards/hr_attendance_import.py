# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api, _
from openerp.exceptions import Warning as UserError
import base64
from tempfile import TemporaryFile
import csv
from datetime import datetime
import pytz
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT


class HrAttendanceImport(models.TransientModel):
    _name = "hr.attendance_import"

    attendance_machine_id = fields.Many2one(
        string="Machine",
        comodel_name="hr.attendance_machine",
        required=True
    )
    data = fields.Binary(
        string="File",
        required=True
    )

    @api.multi
    def get_csv_detail(self):
        dict_field = {}
        obj_csv_detail =\
            self.env["hr.attendance_machine_csv_detail"]

        machine_id =\
            self.attendance_machine_id

        criteria = [
            ("attendance_machine_id", "=", machine_id.id)
        ]

        csv_detail_ids =\
            obj_csv_detail.search(criteria)

        if csv_detail_ids:
            for csv_detail in csv_detail_ids:
                field_name =\
                    csv_detail.field_id.name
                csv_column =\
                    csv_detail.csv_column

                if field_name in dict_field:
                    raise UserError(
                        _("Duplicate Entry "
                          "for Field %s") % (field_name,))
                elif csv_column in dict_field:
                    raise UserError(
                        _("Duplicate Entry "
                          "for Column %s") % (csv_column,))
                else:
                    dict_field[field_name] = {
                        "csv_column": csv_column
                    }
            return dict_field
        else:
            raise UserError("No CSV Details")

    @api.multi
    def check_employee_code(self, row, column):
        try:
            employee_code = row[column]
        except:
            return True, "Invalid employee code column"

        return False, employee_code

    @api.multi
    def check_employee_id(self, employee_code):
        obj_employee_code =\
            self.env["hr.attendance_machine_employee_code"]
        machine_id =\
            self.attendance_machine_id

        criteria = [
            ("attendance_machine_id", "=", machine_id.id),
            ("employee_code_machine", "=", employee_code)
        ]

        employee_id =\
            obj_employee_code.search(criteria).employee_id

        if employee_id:
            return employee_id
        else:
            raise UserError(
                _("No Employee Defined for code %s") % (employee_code,))

    def check_datetime(
        self, row, date_format,
        time_format, column, line_num
    ):
        try:
            str_datetime = row[column]
        except:
            return True, "Invalid date column"

        try:
            datetime_format = date_format + " " + time_format
        except:
            return True, "Not date or time format found"

        try:
            dt_datetime = datetime.strptime(str_datetime, datetime_format)
        except:
            return True, "Invalid Datetime Format on Line %s" % (str(line_num))

        return False, dt_datetime

    @api.multi
    def _convert_datetime_utc(self, dt):
        user = self.env.user
        if user.tz:
            tz = pytz.timezone(user.tz)
        else:
            tz = pytz.utc

        convert_tz = tz.localize(dt)
        convert_utc = convert_tz.astimezone(pytz.utc)
        format_utc = datetime.strftime(
            convert_utc,
            DEFAULT_SERVER_DATETIME_FORMAT
        )

        return format_utc

    @api.multi
    def check_sign_in_out(
        self, row, column, line_num,
        sign_in_code, sign_out_code
    ):
        try:
            sign_in_out = row[column]
        except:
            return True,
            "Invalid Sign In/Out Column "
            "on line %s" % (str(line_num))

        if sign_in_out == sign_in_code:
            return False, 1
        elif sign_in_out == sign_out_code:
            return False, 0
        else:
            return True, "Wrong Sign in/out code on line %s" % (str(line_num))

    @api.multi
    def prepare_data(self, row, line_num):
        data = {}
        test_error = False

        machine_id =\
            self.attendance_machine_id
        date_format =\
            machine_id.date_format
        time_format =\
            machine_id.time_format
        sign_in_code =\
            machine_id.sign_in_code
        sign_out_code =\
            machine_id.sign_out_code

        csv_detail =\
            self.get_csv_detail()

        if "employee_id" in csv_detail:
            employee_code_column =\
                csv_detail["employee_id"]["csv_column"]
        else:
            raise UserError(
                _("No Field Define for Employee"))

        if "name" in csv_detail:
            date_column =\
                csv_detail["name"]["csv_column"]
        else:
            raise UserError(
                _("No Field Define for Date"))

        if "action" in csv_detail:
            action_column =\
                csv_detail["action"]["csv_column"]
        else:
            raise UserError(
                _("No Field Define for Action"))

        test_error, employee_code =\
            self.check_employee_code(
                row, employee_code_column)

        if test_error:
            raise UserError(
                _("%s") % (employee_code,))

        employee_id =\
            self.check_employee_id(employee_code)

        test_error, dt_date =\
            self.check_datetime(row, date_format, time_format,
                                date_column, line_num)

        if test_error:
            raise UserError(
                _("%s") % (dt_date,))

        dt_utc = self._convert_datetime_utc(dt_date)

        test_error, sign_in_out =\
            self.check_sign_in_out(row, action_column, line_num,
                                   sign_in_code, sign_out_code)
        if test_error:
            raise UserError(
                _("%s") % (sign_in_out,))
        else:
            if sign_in_out == 1:
                action = "sign_in"
            else:
                action = "sign_out"

        data = {
            "employee_id": employee_id.id,
            "name": dt_utc,
            "action": action
        }
        return data

    @api.multi
    def check_attendance(self, employee_id, name):
        obj_hr_attendance = self.env["hr.attendance"]

        criteria = [
            ("employee_id", "=", employee_id),
            ("name", "=", name)
        ]

        count_attd =\
            obj_hr_attendance.search_count(criteria)
        return count_attd

    @api.multi
    def button_import(self):
        self.ensure_one()

        obj_hr_attendance =\
            self.env["hr.attendance"]

        machine_id =\
            self.attendance_machine_id
        delimiter_format =\
            machine_id.delimiter
        first_row_header =\
            machine_id.first_row_header

        fileobj = TemporaryFile("w+")
        fileobj.write(base64.decodestring(self.data))
        fileobj.seek(0)

        if delimiter_format:
            delimiter = str(delimiter_format)
        else:
            delimiter = ","

        reader = csv.reader(fileobj, delimiter=delimiter)

        if first_row_header:
            reader.next()

        line_num = 1

        for row in reader:
            data = self.prepare_data(row, line_num)

            count_attd =\
                self.check_attendance(
                    data["employee_id"], data["name"])

            if count_attd == 0:
                obj_hr_attendance.create(data)
            line_num += 1

        fileobj.close()
        return {"type": "ir.actions.act_window_close"}
