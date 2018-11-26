# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    @api.model
    def _default_employee_id(self):
        if len(self.env.user.employee_ids) > 0:
            return self.env.user.employee_ids[0].id

    employee_id = fields.Many2one(
        default=lambda self: self._default_employee_id(),
    )

    department_id = fields.Many2one(
        string="Department",
        comodel_name="hr.department",
        ondelete="restrict",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )

    @api.multi
    def onchange_employee_id(
            self, date_from, date_to,
            employee_id=False, contract_id=False):
        _super = super(HrPayslip, self)
        result = _super.onchange_employee_id(
            date_from, date_to, employee_id, contract_id)
        result["value"]["department_id"] = False
        obj_employee = self.env["hr.employee"]
        employee = obj_employee.browse([employee_id])[0]
        if employee.department_id:
            result["value"]["department_id"] = employee.department_id.id
        return result
