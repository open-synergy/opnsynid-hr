# -*- coding: utf-8 -*-
# Copytright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrPayslipImportedLine(models.Model):
    _name = "hr.payslip_imported_line"
    _description = "HR Payslip Imported Line"

    name = fields.Char(
        string="Filename"
    )
    run_id = fields.Many2one(
        string="Payslip Run",
        comodel_name="hr.payslip.run"
    )
