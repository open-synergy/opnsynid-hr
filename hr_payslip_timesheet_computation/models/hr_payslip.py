# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    @api.multi
    @api.depends(
        "employee_id", "date_from", "date_to")
    def _compute_computation_ids(self):
        obj_sheet = self.env["hr_timesheet_sheet.sheet"]
        for payslip in self:
            computation_ids = []
            criteria = [
                ("employee_id", "=", payslip.employee_id.id),
                ("date_from", ">=", payslip.date_from),
                ("date_to", "<=", payslip.date_to),
                ("state", "=", "done"),
            ]
            timesheets = obj_sheet.search(criteria)
            for timesheet in timesheets:
                computation_ids += timesheet.computation_ids.ids
            payslip.timesheet_computation_ids = [(6, 0, computation_ids)]

    timesheet_computation_ids = fields.Many2many(
        string="Timesheet Computations",
        comodel_name="hr.timesheet_computation",
        compute="_compute_computation_ids",
        relation="rel_payslip_2_timesheet_computation",
        column1="payslip_id",
        column2="computation_id",
        store=True,
    )
    timesheet_computation_summary_ids = fields.One2many(
        string="Timesheet Computation Summary",
        comodel_name="hr.timesheet_computation_summary",
        inverse_name="payslip_id",
    )
