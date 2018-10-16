# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class HrExpense(models.Model):
    _name = "hr.expense.expense"
    _inherit = ["hr.expense.expense", "tier.validation"]
    _state_from = ["confirm"]
    _state_to = ["accepted"]
