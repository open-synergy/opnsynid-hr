# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    def _default_payslip_type(self):
        return self.env['hr.payslip.type'].search([])[:1]

    payslip_type_id = fields.Many2one(
        string="Payslip Type",
        comodel_name="hr.payslip.type",
        default=_default_payslip_type
    )
