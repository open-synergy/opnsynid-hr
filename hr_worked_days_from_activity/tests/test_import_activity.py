# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from .base import BaseTestHrPayslip


class TestImportActivity(BaseTestHrPayslip):
    def test_import_activity(self):
        self.timesheet3.button_confirm()
        self.timesheet3.signal_workflow("done")
        self.assertEqual(
            self.timesheet3.state,
            "done")
        self.payslip_2.compute_sheet()

        wizard = self.wiz.with_context(
            active_model="hr.payslip",
            active_ids=[self.payslip_2.id]
        )
        wizard.button_import_activity()

        criteria = [
            ("import_from_activity", "=", True),
            ("code", "=", "TSADM"),
            ("payslip_id", "=", self.payslip_2.id),
        ]
        wds = self.obj_wd.search(criteria)
        self.assertEqual(
            len(wds),
            1)
        self.assertEqual(
            wds[0].number_of_hours,
            8.0)
