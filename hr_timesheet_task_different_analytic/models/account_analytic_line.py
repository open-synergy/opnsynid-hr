# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=R8110
from openerp import _, models


class AccountAnalyticLine(models.Model):
    _name = "account.analytic.line"
    _inherit = "account.analytic.line"

    def _check_task_project(self, cr, uid, ids):
        return True

    _constraints = [
        (
            _check_task_project,
            _("Error! Task must belong to the project."),
            ["task_id", "account_id"],
        ),
    ]
