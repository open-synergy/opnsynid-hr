# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api


class HrAttendanceImport(models.TransientModel):
    _inherit = "hr.attendance_import"

    @api.model
    def _prepare_attendance_domain(self, employee_id, name):
        _super = super(HrAttendanceImport, self)
        criteria = _super._prepare_attendance_domain(employee_id, name)
        criteria += [
            "|",
            ("sheet_id", "=", False),
            ("sheet_id.state", "not in", ["confirm", "done"]),
        ]
        return criteria
