# -*- coding: utf-8 -*-
# Copytright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrPayslipRunProcessInputLine(models.Model):
    _name = "hr.payslip_run_process_input_line"
    _description = "HR Payslip Run Process Input Line"

    name = fields.Many2one(
        string="Filename",
        comodel_name="hr.payslip_run_imported_input_file"
    )
    employee_code = fields.Char(
        string="Employee Code"
    )
    input_code = fields.Char(
        string="Code"
    )
    amount = fields.Float(
        string="Amount"
    )
    input_id = fields.Many2one(
        string="Input",
        comodel_name="hr.payslip.input"
    )
    run_id = fields.Many2one(
        string="Payslip Run",
        comodel_name="hr.payslip.run"
    )
