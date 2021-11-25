# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from lxml import etree
from openerp import api, fields, models


class HrOvertimeRequestByEmployee(models.TransientModel):
    _name = "hr.overtime_request_by_employee"

    employee_ids = fields.Many2many(
        string="Employee(s)",
        comodel_name="hr.employee",
        column1="request_id",
        column2="employee_id",
        relation="overtime_request_by_employee_rel",
    )

    @api.model
    def fields_view_get(
        self, view_id=None, view_type="form", toolbar=False, submenu=False
    ):
        res = super(HrOvertimeRequestByEmployee, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu
        )
        doc = etree.XML(res["arch"])
        domain = []
        department_id = self._context.get("department_id", False)
        manager_id = self._context.get("manager_id", False)
        if department_id:
            domain.append(("department_id", "=", department_id))
        if manager_id:
            domain.append(("parent_id", "=", manager_id))
        if domain:
            for node in doc.xpath("//field[@name='employee_ids']"):
                node.set("domain", str(domain))
        res["arch"] = etree.tostring(doc)
        return res

    @api.multi
    def _prepare_data(self, request_batch_id, employee_id, batch):
        date_start = batch.date_start
        date_end = batch.date_end
        manager_id = batch.manager_id.id or False
        department_id = batch.department_id.id or False

        data = {
            "date_start": date_start,
            "date_end": date_end,
            "manager_id": manager_id,
            "department_id": department_id,
            "employee_id": employee_id,
            "request_batch_id": request_batch_id,
        }
        return data

    @api.multi
    def action_generate(self):
        self.ensure_one()
        obj_overtime_request = self.env["hr.overtime_request"]
        obj_overtime_request_batch = self.env["hr.overtime_request_batch"]
        context = self._context
        active_id = context["active_id"]
        if active_id:
            criteria = [("id", "=", active_id)]
            batch = obj_overtime_request_batch.search(criteria)

        if self.employee_ids and batch:
            for employee in self.employee_ids:
                data = self._prepare_data(active_id, employee.id, batch)
                obj_overtime_request.create(data)

        return {"type": "ir.actions.act_window_close"}
