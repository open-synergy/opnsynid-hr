# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api
from datetime import datetime
from datetime import timedelta


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    @api.model
    def get_worked_day_lines(
        self, contract_ids, date_from, date_to, context=None
    ):
        res = super(HrPayslip, self).get_worked_day_lines(
            contract_ids, date_from, date_to, context=None)
        number_of_days = 0.0
        day_from = datetime.strptime(date_from, "%Y-%m-%d")
        day_to = datetime.strptime(date_to, "%Y-%m-%d")
        nb_of_days = (day_to - day_from).days + 1
        contract_id = res[0]["contract_id"]
        contract = self.env["hr.contract"].browse([contract_id])[0]
        for day in range(0, nb_of_days):
            work_scheduled = contract.employee_id.work_scheduled_on_day(
                date_dt=day_from + timedelta(days=day))
            if work_scheduled:
                number_of_days += 1.0
                res[0].update({"number_of_days": number_of_days})
        return res
