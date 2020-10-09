# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openerp import api, models


class HrHolidays(models.Model):
    _name = "hr.holidays"
    _inherit = [
        "hr.holidays",
        "tier.validation",
    ]
    _state_from = [
        "draft",
        "confirm",
    ]
    _state_to = [
        "validate",
    ]
    _cancel_state = "refuse"

    @api.multi
    def validate_tier(self):
        _super = super(HrHolidays, self)
        _super.validate_tier()
        for document in self:
            if document.validated:
                document.signal_workflow("validate")

    @api.multi
    def restart_validation(self):
        _super = super(HrHolidays, self)
        _super.restart_validation()
        for document in self:
            document.request_validation()

    @api.multi
    def holidays_confirm(self):
        _super = super(HrHolidays, self)
        _super.holidays_confirm()
        for document in self:
            document.request_validation()
