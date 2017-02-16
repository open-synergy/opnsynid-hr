# -*- coding: utf-8 -*-
# Copytright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrPayslipRunImportedInputLine(models.Model):
    _name = "hr.payslip_run_imported_input_file"
    _description = "HR Payslip Run Imported Input Line"

    name = fields.Char(
        string="Filename",
        required=True
    )
    run_id = fields.Many2one(
        string="Payslip Run",
        comodel_name="hr.payslip.run"
    )
