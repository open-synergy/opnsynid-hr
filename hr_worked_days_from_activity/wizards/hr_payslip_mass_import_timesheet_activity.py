# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class HrPayslipMassImportTimesheetActivity(models.TransientModel):
    _name = "hr.payslip.mass_import_timesheet_activity"
    _description = "Hr Payslip Mass Import Timesheet Activity"

    @api.multi
    def button_import_activity(self):
        obj_hr_payslip = self.env["hr.payslip"]
        active_ids = self.env.context["active_ids"]

        for record in obj_hr_payslip.browse(active_ids):
            record.action_import_timesheet_activity()

        return True
