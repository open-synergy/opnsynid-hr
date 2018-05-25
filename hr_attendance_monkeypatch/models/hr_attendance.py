# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api
from openerp.exceptions import Warning as UserError


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    @api.multi
    def _altern_si_so(self):
        _super = super(HrAttendance, self)
        return _super._altern_si_so()

    _constraints = [
        (_altern_si_so,
            "Error! Sign in (resp. Sign out) must follow Sign out "
            "(resp. Sign in)",
            ["action"]),
    ]

    @api.constrains("action")
    def _check_test(self):
        if not self._do_check():
            return True

        prev_attns = self._get_prev_attendance()
        next_attns = self._get_next_attendance()
        str_warning = """Error! Sign in (resp. Sign out) must
                      follow Sign out (resp. Sign in)"""

        if prev_attns and prev_attns[0].action == self.action:
            raise UserError(str_warning)
        elif next_attns and next_attns[0].action == self.action:
            raise UserError(str_warning)
        elif (not prev_attns) and (not next_attns) and \
                self.action != "sign_in":
            raise UserError(str_warning)

        return True

    @api.multi
    def _do_check(self):
        self.ensure_one()

        skip = self._context.get("skip_attendance_check", False)
        if skip:
            return False

        company = self.env.user.company_id
        return company.check_attendance

    @api.multi
    def _get_prev_attendance(self):
        self.ensure_one()
        criteria = [
            ("employee_id", "=", self.employee_id.id),
            ("name", "<", self.name),
            ("action", "in", ["sign_in", "sign_out"]),
        ]
        return self.search(criteria)

    @api.multi
    def _get_next_attendance(self):
        self.ensure_one()
        criteria = [
            ("employee_id", "=", self.employee_id.id),
            ("name", ">", self.name),
            ("action", "in", ["sign_in", "sign_out"]),
        ]
        return self.search(criteria)
