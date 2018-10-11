# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api
import math
from lxml import etree


class HrHolidayByEmployee(models.TransientModel):
    _name = "hr.holiday_by_employee"

    employee_ids = fields.Many2many(
        string="Employee(s)",
        comodel_name="hr.employee",
        column1="request_id",
        column2="employee_id",
        relation="hr_holiday_by_employee_rel"
    )

    @api.model
    def fields_view_get(
        self, view_id=None, view_type='form', toolbar=False, submenu=False
    ):
        res = super(HrHolidayByEmployee, self).fields_view_get(
            view_id=view_id, view_type=view_type,
            toolbar=toolbar, submenu=submenu)
        doc = etree.XML(res['arch'])
        department_id =\
            self._context.get('department_id', False)
        if department_id:
            for node in doc.xpath("//field[@name='employee_ids']"):
                domain = "[('department_id', '=', department_id)]"
                node.set('domain', domain)
        res['arch'] = etree.tostring(doc)
        return res

    @api.multi
    def _prepare_data(self, request_batch_id,
                      employee, batch):
        department_id =\
            employee.department_id.id or False
        holiday_status_id =\
            batch.holiday_status_id.id or False
        name =\
            batch.name
        holiday_type =\
            batch.holiday_type
        holiday_request_type =\
            batch.type

        data = {
            "name": name,
            "department_id": department_id,
            "employee_id": employee.id,
            "holiday_status_id": holiday_status_id,
            "holiday_type": holiday_type,
            "type": holiday_request_type,
            "state": "draft"
        }
        if batch.type == "remove":
            diff_day =\
                self.env['hr.holidays']._get_number_of_days(
                    batch.date_start, batch.date_end)
            data["number_of_days_temp"] =\
                round(math.floor(diff_day))+1
            data["date_from"] =\
                batch.date_start
            data["date_to"] =\
                batch.date_end
            data["leave_batch_id"] =\
                request_batch_id
        else:
            data["number_of_days_temp"] =\
                batch.number_of_days
            data["allocation_batch_id"] =\
                request_batch_id
        return data

    @api.multi
    def action_generate(self):
        self.ensure_one()

        obj_hr_holiday = self.env["hr.holidays"]
        obj_leave_request_batch =\
            self.env["hr.holiday_batch_leave_request"]
        obj_allocation_request_batch =\
            self.env["hr.holiday_batch_allocation_request"]

        context = self._context
        active_id = context["active_id"]
        active_model = context["active_model"]

        if active_id:
            criteria = [
                ("id", "=", active_id)
            ]
            if active_model == "hr.holiday_batch_leave_request":
                batch =\
                    obj_leave_request_batch.search(criteria)
            else:
                batch =\
                    obj_allocation_request_batch.search(criteria)

        if self.employee_ids and batch:
            for employee in self.employee_ids:
                data =\
                    self._prepare_data(
                        active_id,
                        employee,
                        batch
                    )
                obj_hr_holiday.create(data)

        return {"type": "ir.actions.act_window_close"}
