# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openerp import api, models


class HrPayslip(models.Model):
    _name = "hr.payslip"
    _inherit = [
        "hr.payslip",
        "tier.validation",
    ]
    _state_from = [
        "draft",
        "verify",
    ]
    _state_to = [
        "done",
    ]

    @api.multi
    def validate_tier(self):
        _super = super(HrPayslip, self)
        _super.validate_tier()
        for document in self:
            if document.validated:
                document.signal_workflow("button_done")

    @api.multi
    def restart_validation(self):
        _super = super(HrPayslip, self)
        _super.restart_validation()
        for document in self:
            document.request_validation()

    @api.multi
    def hr_verify_sheet(self):
        _super = super(HrPayslip, self)
        _super.hr_verify_sheet()
        for document in self:
            document.request_validation()
