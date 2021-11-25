# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    @api.multi
    @api.depends("employee_id", "date_from", "date_to")
    def _compute_loan_ids(self):
        obj_schedule = self.env["loan.out_payment_schedule"]
        for payslip in self:
            partner = payslip.employee_id.address_home_id
            if not partner:
                continue
            criteria = [
                ("loan_id.partner_id.id", "=", partner.id),
                ("schedule_date", ">=", payslip.date_from),
                ("schedule_date", "<=", payslip.date_to),
                ("state", "=", "active"),
            ]
            schedules = obj_schedule.search(criteria)
            payslip.loan_payment_schedule_ids = [(6, 0, schedules.ids)]

    loan_payment_schedule_ids = fields.Many2many(
        string="Loan Payment Schedules",
        comodel_name="loan.out_payment_schedule",
        compute="_compute_loan_ids",
        relation="rel_payslip_2_loan_payment_schedule",
        column1="payslip_id",
        column2="payment_schedule_id",
    )
