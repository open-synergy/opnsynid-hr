# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from dateutil.relativedelta import relativedelta
from openerp import models, fields, api


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    @api.multi
    @api.depends("name")
    def _compute_overtime(self):
        obj_overtime = self.env["hr.overtime_request"]
        for attn in self:
            company = attn.employee_id.company_id
            start_buffer = fields.Datetime.from_string(attn.name) + \
                relativedelta(hours=company.start_overtime_buffer)
            start_buffer = fields.Datetime.to_string(start_buffer)
            end_buffer = fields.Datetime.from_string(attn.name) + \
                relativedelta(hours=-company.end_overtime_buffer)
            end_buffer = fields.Datetime.to_string(end_buffer)

            criteria = [
                ("employee_id", "=", attn.employee_id.id),
                ("date_start", "<=", start_buffer),
                ("date_end", ">=", end_buffer),
            ]
            overtimes = obj_overtime.search(criteria, limit=1)
            attn.overtime_id = overtimes[0].id if len(overtimes) > 0 else False

    overtime_id = fields.Many2one(
        string="Overtime Request",
        comodel_name="hr.overtime_request",
        compute="_compute_overtime",
        store=True,
    )
