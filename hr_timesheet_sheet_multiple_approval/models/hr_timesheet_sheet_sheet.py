# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import api, models


class HrTimesheetSheetSheet(models.Model):
    _name = "hr_timesheet_sheet.sheet"
    _inherit = [
        "hr_timesheet_sheet.sheet",
        "tier.validation",
    ]
    _state_from = [
        "draft",
        "confirm",
    ]
    _state_to = [
        "done",
    ]
    _cancel_state = "draft"

    @api.multi
    def validate_tier(self):
        _super = super(HrTimesheetSheetSheet, self)
        _super.validate_tier()
        for document in self:
            if document.validated:
                document.signal_workflow("done")

    @api.multi
    def restart_validation(self):
        _super = super(HrTimesheetSheetSheet, self)
        _super.restart_validation()
        for document in self:
            document.request_validation()

    @api.multi
    def button_confirm(self):
        _super = super(HrTimesheetSheetSheet, self)
        _super.button_confirm()
        for document in self:
            document.request_validation()

    @api.multi
    def action_set_to_draft(self):
        self.ensure_one()
        _super = super(HrTimesheetSheetSheet, self)
        _super.action_set_to_draft()
        self.definition_id = False
        self.reviewer_partner_ids = False
        self.review_ids = False
