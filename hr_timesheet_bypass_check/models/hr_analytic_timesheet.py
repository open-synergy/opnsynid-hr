# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api


class HrAnalyticTimesheet(models.Model):
    _name = "hr.analytic.timesheet"
    _inherit = "hr.analytic.timesheet"

    @api.multi
    def _check(self):
        no_check = self.env.context.get("no_check", False)

        if not no_check:
            _super = super(HrAnalyticTimesheet, self)
            _super._check()

        return True
