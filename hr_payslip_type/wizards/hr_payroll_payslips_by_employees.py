# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from openerp import api, models

_logger = logging.getLogger(__name__)


class HrPayslipEmployees(models.TransientModel):
    _inherit = "hr.payslip.employees"

    @api.multi
    def compute_sheet(self):
        res = super(HrPayslipEmployees, self).compute_sheet()
        obj_hr_payslip_run = self.env["hr.payslip.run"]
        payslip_run = obj_hr_payslip_run.browse(self.env.context["active_id"])
        payslip_type = (
            payslip_run.payslip_type_id and payslip_run.payslip_type_id.id or False
        )

        payslip_run.slip_ids.write({"payslip_type_id": payslip_type})
        payslip_run.slip_ids.compute_sheet()
        return res
