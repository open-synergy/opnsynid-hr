# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api, fields


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    @api.model
    def _default_payslip_type(self):
        payslip_type_normal = self.env.ref(
            "hr_payslip_type.hr_payslip_type_normal"
        )
        return payslip_type_normal.id

    payslip_type_id = fields.Many2one(
        string="Payslip Type",
        comodel_name="hr.payslip.type",
        default=_default_payslip_type
    )
