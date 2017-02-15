# -*- coding: utf-8 -*-
# Copytright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrPayslipProcessLine(models.Model):
    _name = "hr.payslip_process_line"
    _description = "HR Payslip Process Line"

    name = fields.Char(
        string="Filename"
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
