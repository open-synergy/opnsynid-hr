# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api


class HrTimesheetComputationItem(models.Model):
    _inherit = "hr.timesheet_computation_item"

    @api.multi
    def _get_localdict(self, sheet):
        _super = super(HrTimesheetComputationItem, self)
        result = _super._get_localdict(sheet)
        result.update({"overtimes": sheet.overtime_ids})
        return result
