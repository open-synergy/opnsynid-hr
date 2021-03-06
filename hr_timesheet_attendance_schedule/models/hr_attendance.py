# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from dateutil.relativedelta import relativedelta
from openerp import models, fields, api, _
from openerp.exceptions import Warning as UserError


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    @api.multi
    @api.depends("name")
    def _compute_schedule(self):
        obj_schedule = self.env["hr.timesheet_attendance_schedule"]
        for attn in self:
            company = attn.employee_id.company_id
            early_buffer = fields.Datetime.from_string(attn.name) + \
                relativedelta(hours=company.early_attendance_buffer)
            early_buffer = fields.Datetime.to_string(early_buffer)
            late_buffer = fields.Datetime.from_string(attn.name) + \
                relativedelta(hours=-company.late_attendance_buffer)
            late_buffer = fields.Datetime.to_string(late_buffer)

            criteria = [
                ("employee_id", "=", attn.employee_id.id),
                ("date_start", "<=", early_buffer),
                ("date_end", ">=", late_buffer),
            ]
            schedules = obj_schedule.search(criteria, limit=1)
            attn.schedule_id = schedules[0].id if len(schedules) > 0 else False

    schedule_id = fields.Many2one(
        string="Attendance Schedule",
        comodel_name="hr.timesheet_attendance_schedule",
        compute="_compute_schedule",
        store=True,
    )

    @api.constrains(
        "schedule_id",
    )
    def _check_att_sign_in_out(self):
        for document in self:
            company = document.employee_id.company_id

            if not document.schedule_id:
                continue

            if company.max_att_sign_in > 0:
                len_att_sign_in = \
                    len(document.schedule_id.attendance_ids.filtered(
                        lambda x: x.action == "sign_in"))
                if len_att_sign_in > company.max_att_sign_in:
                    msg = _("Total Sign In has reached maximum "
                            "attempts per schedule")
                    raise UserError(msg)

            if company.max_att_sign_out > 0:
                len_att_sign_out = \
                    len(document.schedule_id.attendance_ids.filtered(
                        lambda x: x.action == "sign_out"))
                if len_att_sign_out > company.max_att_sign_out:
                    msg = _("Total Sign Out has reached maximum "
                            "attempts per schedule")
                    raise UserError(msg)
