# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, api, fields


class HrTimesheetSheetSheet(models.Model):
    _name = "hr_timesheet_sheet.sheet"
    _inherit = [
        "hr_timesheet_sheet.sheet",
        "base.sequence_document",
    ]

    name = fields.Char(
        string="# Document",
        default="/",
        copy=False,
    )

    @api.model
    def create(self, values):
        _super = super(HrTimesheetSheetSheet, self)
        result = _super.create(values)
        sequence = result._create_sequence()
        result.write({
            "name": sequence,
        })
        return result

    @api.multi
    def name_get(self):
        _super = super(HrTimesheetSheetSheet, self)
        res = _super.name_get()
        result = []
        for rec in self:
            if rec.name:
                result.append((rec.id, rec.name))
            else:
                result = res
        return result
