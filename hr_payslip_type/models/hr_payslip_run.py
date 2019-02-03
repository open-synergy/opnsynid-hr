# Copyright 2017-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class HrPayslipRun(models.Model):
    _inherit = "hr.payslip.run"

    payslip_type_id = fields.Many2one(
        string="Payslip Type",
        comodel_name="hr.payslip.type"
    )
