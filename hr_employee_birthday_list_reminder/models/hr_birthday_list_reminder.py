# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)

try:
    import pandas as pd
except (ImportError, IOError) as err:
    _logger.debug(err)


class HrBirthdayListReminder(models.Model):
    _name = "hr.birthday_list_reminder"
    _inherit = [
        "mail.thread",
    ]
    _description = "Employee Birthday Reminder"

    name = fields.Char(
        string="Description",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    list_type = fields.Selection(
        string="Type",
        selection=[
            ("all", "All Employee"),
            ("manual", "Manual Selection"),
        ],
        default="manual",
        required=True,
    )

    @api.multi
    def _compute_employee(self):
        obj_hr_employee =\
            self.env["hr.employee"]

        for document in self:
            employee_ids =\
                obj_hr_employee.search(
                    document._prepare_employee_data())
            employee_birthday_list =\
                document._get_birthday_list(employee_ids)
            document.employee_ids = employee_birthday_list

    employee_ids = fields.Many2many(
        string="Employee(s)",
        comodel_name="hr.employee",
        compute="_compute_employee",
        store=False,
    )
    manual_employee_ids = fields.Many2many(
        string="Employee(s)",
        comodel_name="hr.employee",
        relation="rel_birthday_reminder_2_manual_employee",
        column1="reminder_id",
        columnt2="employee_id",
    )
    date_start_offset = fields.Integer(
        string="Date Start Offset",
        required=True,
        default=0,
    )
    date_start_offset_period = fields.Selection(
        string="Date Start Offset Period",
        selection=[
            ("day", "Day"),
            ("month", "Month"),
        ],
        default="day",
        required=True,
    )
    date_end_offset = fields.Integer(
        string="Date End Offset",
        required=True,
        default=0,
    )
    date_end_offset_period = fields.Selection(
        string="Date End Offset Period",
        selection=[
            ("day", "Day"),
            ("month", "Month"),
        ],
        default="day",
        required=True,
    )
    cron_id = fields.Many2one(
        string="Cron",
        comodel_name="ir.cron",
        readonly=True,
    )
    email_template_id = fields.Many2one(
        string="Email Template",
        comodel_name="email.template",
    )
    recipient_partner_ids = fields.Many2many(
        string="Recipient(s)",
        comodel_name="res.partner",
        relation="rel_birthday_reminder_2_recipient",
        column1="reminder_id",
        column2="partner_id",
    )
    note = fields.Text(
        string="Note",
    )

    @api.multi
    def _compute_date_offset(self):
        self.ensure_one()
        date_start_offset =\
            self.date_start_offset
        date_end_offset =\
            self.date_end_offset
        date_start_offset_period =\
            self.date_start_offset_period
        date_end_offset_period =\
            self.date_end_offset_period
        dt_now = pd.to_datetime(datetime.now())
        # Compute Date Start Offset
        if date_start_offset_period == "day":
            dt_start =\
                dt_now + pd.DateOffset(
                    days=date_start_offset)
        else:
            dt_start =\
                dt_now + pd.DateOffset(
                    months=date_start_offset)
        # Compute Date End Offset
        if date_end_offset_period == "day":
            dt_end =\
                dt_now + pd.DateOffset(
                    days=date_end_offset)
        else:
            dt_end =\
                dt_now + pd.DateOffset(
                    months=date_end_offset)
        # Convert offset from datetime to date
        date_start_conv =\
            datetime.strftime(dt_start, "%Y-%m-%d")
        date_end_conv =\
            datetime.strftime(dt_end, "%Y-%m-%d")
        return date_start_conv, date_end_conv

    @api.multi
    def _prepare_employee_data(self):
        self.ensure_one()
        if self.list_type == "all":
            result = []
        else:
            result = [
                ("id", "in", self.manual_employee_ids.ids),
            ]
        return result

    @api.multi
    def _get_birthday_list(self, employee_ids):
        self.ensure_one()
        employee_birtday_list = []

        date_start_conv, date_end_conv =\
            self._compute_date_offset()
        current_year =\
            datetime.now().year

        for employee in employee_ids:
            if employee.birthday:
                birthday = employee.birthday
                date = datetime.strptime(birthday, '%Y-%m-%d')
                conv_birtday = date.replace(year=current_year)
                str_birthday =\
                    datetime.strftime(conv_birtday, "%Y-%m-%d")
                if (
                    str_birthday >= date_start_conv and
                    str_birthday <= date_end_conv
                ):
                    employee_birtday_list.append(employee.id)
        return employee_birtday_list

    @api.multi
    def action_create_cron(self):
        for document in self:
            document._generate_cron()

    @api.multi
    def action_delete_cron(self):
        for document in self:
            document.cron_id.unlink()

    @api.multi
    def _generate_cron(self):
        self.ensure_one()
        data = self._prepare_cron_data()
        obj_cron = self.env["ir.cron"]
        cron = obj_cron.create(data)
        self.write({"cron_id": cron.id})

    @api.multi
    def _prepare_cron_data(self):
        self.ensure_one()
        cron_name = "Employee Birthday Reminder: %s" % (
            self.name)
        return {
            "name": cron_name,
            "user_id": self.env.user.id,
            "active": True,
            "interval_number": 30,
            "interval_type": "days",
            "numberofcall": -1,
            "doall": True,
            "model": "hr.birthday_list_reminder",
            "function": "cron_send_email",
            "args": "(%s,)" % (self.id),
        }

    @api.model
    def cron_send_email(self, reminder_id):
        reminder = self.browse([reminder_id])[0]
        reminder._send_email()

    @api.multi
    def _send_email(self):
        self.ensure_one()
        obj_template = self.env["email.template"]
        obj_mail = self.env["mail.mail"]

        if self.email_template_id and self.recipient_partner_ids:
            template = self.email_template_id
            # TODO: Use email.template send_mail method
            email_dict = obj_template.generate_email(
                template_id=template.id, res_id=self.id)
            mail = obj_mail.create(email_dict)
            mail.write(
                {"recipient_ids": [(6, 0, self.recipient_partner_ids.ids)]})
            mail.send()
