# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class HRPayslipRun(models.Model):
    _name = "hr.payslip.run"
    _inherit = ["hr.payslip.run", "mail.thread"]
