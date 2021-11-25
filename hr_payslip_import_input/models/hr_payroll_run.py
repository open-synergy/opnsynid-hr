# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class HrPayslipRun(models.Model):
    _inherit = "hr.payslip.run"

    process_inputs = fields.One2many(
        string="Process Inputs",
        comodel_name="hr.payslip_run_process_input_line",
        inverse_name="run_id",
        readonly=True,
    )
    imported_files = fields.One2many(
        string="Imported Files",
        comodel_name="hr.payslip_run_imported_input_file",
        inverse_name="run_id",
        readonly=True,
    )
