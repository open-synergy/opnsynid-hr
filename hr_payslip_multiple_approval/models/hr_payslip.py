# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class HrPayslip(models.Model):
    _name = "hr.payslip"
    _inherit = ["hr.payslip", "tier.validation"]
    _state_from = ["verify"]
    _state_to = ["done"]
