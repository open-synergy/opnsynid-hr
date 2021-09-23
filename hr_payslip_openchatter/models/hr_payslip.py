# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class HRPayslip(models.Model):
    _name = "hr.payslip"
    _inherit = ["hr.payslip", "mail.thread"]
