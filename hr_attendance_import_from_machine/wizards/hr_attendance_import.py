# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import base64
import csv
from datetime import datetime
from tempfile import TemporaryFile

import pytz
from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT


class HrAttendanceImport(models.TransientModel):
    _name = "hr.attendance_import"

    attendance_machine_id = fields.Many2one(
        string="Machine", comodel_name="hr.attendance_machine", required=True
    )
    data = fields.Binary(string="File", required=True)

    @api.multi
    def get_csv_detail(self):
        dict_field = {}
        dict_date = {}
        obj_csv_detail = self.env["hr.attendance_machine_csv_detail"]

        machine_id = self.attendance_machine_id

        criteria = [("attendance_machine_id", "=", machine_id.id)]

        csv_detail_ids = obj_csv_detail.search(criteria)

        if csv_detail_ids:
            for csv_detail in csv_detail_ids:
                field_name = csv_detail.field_id.name
                field_type = csv_detail.field_id.ttype
                format_date = csv_detail.date_format
                csv_column = csv_detail.csv_column

                if field_type != "datetime":
                    dict_field[field_name] = {"csv_column": csv_column}
                else:
                    dict_date[format_date] = {"csv_column": csv_column}
                    dict_field[field_name] = dict_date
            return dict_field
        else:
            raise UserError(_("No CSV Details"))

    @api.multi
    def check_employee_code(self, row, column):
        try:
            employee_code = row[column]
        except Exception:
            return False

        return employee_code

    @api.multi
    def check_employee_id(self, employee_code):
        result = False
        obj_employee_code = self.env["hr.attendance_machine_employee_code"]
        machine_id = self.attendance_machine_id

        criteria = [
            ("attendance_machine_id", "=", machine_id.id),
            ("employee_code_machine", "=", employee_code),
        ]

        employee_id = obj_employee_code.search(criteria).employee_id

        if employee_id:
            result = employee_id.id
        return result

    @api.multi
    def get_employee_data(self, row, employee_code_column):
        result = False
        employee_code = self.check_employee_code(row, employee_code_column)

        if employee_code:
            result = self.check_employee_id(employee_code)
        return result

    @api.multi
    def check_date(self, row, date_format, column, line_num):
        try:
            str_date = row[column]
        except Exception:
            return True, "Invalid date column"

        try:
            date_format = date_format
        except Exception:
            return True, "Not date format found"

        try:
            dt_date = datetime.strptime(str_date, date_format).strftime(date_format)
        except Exception:
            return True, "Invalid Date Format on Line {} {}".format(
                str_date, date_format
            )

        return False, dt_date

    @api.multi
    def check_time(self, row, time_format, column, line_num):
        try:
            str_time = row[column]
        except Exception:
            return True, "Invalid time column"

        try:
            time_format = time_format
        except Exception:
            return True, "Not time format found"

        try:
            dt_time = datetime.strptime(str_time, time_format).strftime(time_format)
        except Exception:
            return True, "Invalid Time Format on Line %s" % (str(line_num))

        return False, dt_time

    @api.multi
    def check_datetime(self, row, date_format, time_format, column, line_num):
        try:
            str_datetime = row[column]
        except Exception:
            return True, "Invalid date column"

        try:
            datetime_format = date_format + " " + time_format
        except Exception:
            return True, "Not date or time format found"

        try:
            dt_datetime = datetime.strptime(str_datetime, datetime_format)
        except Exception:
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
        format_utc = datetime.strftime(convert_utc, DEFAULT_SERVER_DATETIME_FORMAT)

        return format_utc

    @api.multi
    def get_name_data(
        self, detail_format, row, date_format, time_format, column, line_num
    ):
        if detail_format == "datetime":
            test_error, dt_date = self.check_datetime(
                row, date_format, time_format, column, line_num
            )
        if detail_format == "date":
            test_error, dt_date = self.check_date(row, date_format, column, line_num)

        if detail_format == "time":
            test_error, dt_date = self.check_time(row, time_format, column, line_num)

        if test_error:
            raise UserError(_("%s") % (dt_date,))

        return dt_date

    @api.multi
    def check_sign_in_out(self, row, column, line_num, sign_in_code, sign_out_code):
        try:
            sign_in_out = row[column]
        except Exception:
            err_msg = "Invalid Sign In/Out Column on line %s" % (str(line_num))
            return True, err_msg

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

        machine_id = self.attendance_machine_id
        date_format = machine_id.date_format
        time_format = machine_id.time_format
        sign_in_code = machine_id.sign_in_code
        sign_out_code = machine_id.sign_out_code
        detail_date = False
        detail_time = False
        detail_datetime = False

        csv_detail = self.get_csv_detail()

        for detail in csv_detail:
            if detail == "employee_id":
                employee_code_column = csv_detail[detail]["csv_column"]
                data_employee = self.get_employee_data(row, employee_code_column)
                data[detail] = data_employee
            elif (
                "date" in csv_detail[detail]
                or "time" in csv_detail[detail]
                or "datetime" in csv_detail[detail]
            ):
                for detail_format in csv_detail[detail]:
                    column = csv_detail[detail][detail_format]["csv_column"]
                    if detail_format == "date":
                        detail_date = self.get_name_data(
                            detail_format,
                            row,
                            date_format,
                            time_format,
                            column,
                            line_num,
                        )
                    elif detail_format == "time":
                        detail_time = self.get_name_data(
                            detail_format,
                            row,
                            date_format,
                            time_format,
                            column,
                            line_num,
                        )
                    else:
                        detail_datetime = self.get_name_data(
                            detail_format,
                            row,
                            date_format,
                            time_format,
                            column,
                            line_num,
                        )
                if detail_date and detail_time:
                    datetime_format = date_format + " " + time_format
                    data_name = detail_date + " " + detail_time
                    dt_datetime = datetime.strptime(data_name, datetime_format)
                else:
                    dt_datetime = detail_datetime
                data[detail] = self._convert_datetime_utc(dt_datetime)
            elif detail == "action":
                action_column = csv_detail[detail]["csv_column"]
                test_error, sign_in_out = self.check_sign_in_out(
                    row, action_column, line_num, sign_in_code, sign_out_code
                )
                if test_error:
                    raise UserError(_("%s") % (sign_in_out,))
                else:
                    if sign_in_out == 1:
                        action = "sign_in"
                    else:
                        action = "sign_out"
                data[detail] = action
            else:
                data_column = csv_detail[detail]["csv_column"]
                data[detail] = row[data_column]

        return data

    @api.model
    def _prepare_attendance_domain(self, employee_id, name):
        criteria = [("employee_id", "=", employee_id), ("name", "=", name)]
        return criteria

    @api.multi
    def check_attendance(self, employee_id, name):
        obj_hr_attendance = self.env["hr.attendance"]

        criteria = self._prepare_attendance_domain(employee_id, name)

        count_attd = obj_hr_attendance.search_count(criteria)
        return count_attd

    @api.multi
    def check_attendance_action(self, employee_id, name):
        obj_hr_attendance = self.env["hr.attendance"]

        criteria = [("employee_id", "=", employee_id), ("name", "<", name)]

        attd = obj_hr_attendance.search(criteria, order="name desc", limit=1)
        if attd:
            if attd.action == "sign_in":
                return "sign_out"
            else:
                return "sign_in"
        else:
            return "sign_in"

    @api.model
    def _check_attendance_creation(self, employee_id, attendance_date):
        result = False
        if employee_id:
            count_attd = self.check_attendance(employee_id, attendance_date)
            if count_attd == 0:
                result = True
            else:
                result = False

        return result

    @api.multi
    def button_import(self):
        self.ensure_one()

        obj_hr_attendance = self.env["hr.attendance"]

        machine_id = self.attendance_machine_id
        delimiter_format = machine_id.delimiter
        first_row_header = machine_id.first_row_header

        fileobj = TemporaryFile("w+")
        fileobj.write(base64.decodestring(self.data))
        fileobj.seek(0)

        delimiter = delimiter_format.decode("string_escape")

        reader = csv.reader(fileobj, delimiter=delimiter)

        if first_row_header:
            reader.next()  # noqa: B305

        line_num = 1

        for row in reader:
            data = self.prepare_data(row, line_num)

            check_creation = self._check_attendance_creation(
                data["employee_id"],
                data["name"],
            )

            if check_creation:
                if "action" not in data:
                    action = self.check_attendance_action(
                        data["employee_id"], data["name"]
                    )
                    data["action"] = action
                obj_hr_attendance.create(data)
            line_num += 1

        fileobj.close()
        return {"type": "ir.actions.act_window_close"}
