# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrAnalyticAccountTimesheetPricelist(models.Model):
    _name = "hr.analytic_account_timesheet_pricelist"
    _description = "Analytic Account's Timesheet Pricelist"

    analytic_account_id = fields.Many2one(
        string="Analytic Account",
        comodel_name="account.analytic.account",
    )
    user_id = fields.Many2one(
        string="User",
        comodel_name="res.users",
        required=True,
    )
    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.product",
        required=True,
    )
    pricelist_id = fields.Many2one(
        string="Timesheet Pricelist",
        comodel_name="product.pricelist",
        required=True,
    )
