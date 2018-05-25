# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api
from openerp.addons.hr_attendance.hr_attendance import hr_attendance


@api.multi
def _altern_si_so(self):
    return True


class HrAttendanceMonkeypatch(models.TransientModel):
    _name = "hr.attendance_monkeypatch"

    def _register_hook(self, cr):
        hr_attendance._altern_si_so = _altern_si_so
        _super = super(HrAttendanceMonkeypatch, self)
        return _super._register_hook(cr)
