# -*- coding: utf-8 -*-
# © 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from .base import BaseTestHrPayslip


class TestWorkedDaysFromActivity(BaseTestHrPayslip):
    def test_1(self):
        self.timesheet1.button_confirm()
        self.timesheet1.signal_workflow("done")
        self.timesheet2.button_confirm()
        self.timesheet2.signal_workflow("done")
        self.assertEqual(self.timesheet1.state, "done")
        self.payslip.compute_sheet()
        self.payslip.action_import_timesheet_activity()
        criteria1 = [
            ("import_from_activity", "=", True),
            ("code", "=", "TSCONS"),
            ("payslip_id", "=", self.payslip.id),
        ]
        wds = self.obj_wd.search(criteria1)
        self.assertEqual(len(wds), 1)
        self.assertEqual(wds[0].number_of_hours, 8.0)
        criteria2 = [
            ("import_from_activity", "=", True),
            ("code", "=", "TSADM"),
            ("payslip_id", "=", self.payslip.id),
        ]
        wds = self.obj_wd.search(criteria2)
        self.assertEqual(len(wds), 1)
        self.assertEqual(wds[0].number_of_hours, 10.0)

    def test_2(self):
        self.payslip.compute_sheet()
        self.payslip.action_import_timesheet_activity()
        criteria1 = [
            ("import_from_activity", "=", True),
            ("code", "=", "TSCONS"),
            ("payslip_id", "=", self.payslip.id),
        ]
        wds = self.obj_wd.search(criteria1)
        self.assertEqual(len(wds), 1)
        self.assertEqual(wds[0].number_of_hours, 0.0)
        criteria2 = [
            ("import_from_activity", "=", True),
            ("code", "=", "TSADM"),
            ("payslip_id", "=", self.payslip.id),
        ]
        wds = self.obj_wd.search(criteria2)
        self.assertEqual(len(wds), 1)
        self.assertEqual(wds[0].number_of_hours, 0.0)
