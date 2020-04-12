# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class AccountAnalyticAccount(models.Model):
    _name = "account.analytic.account"
    _inherit = "account.analytic.account"

    timesheet_pricelist_ids = fields.One2many(
        string="Timesheet Pricelist",
        comodel_name="hr.analytic_account_timesheet_pricelist",
        inverse_name="analytic_account_id",
    )
