# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class AccountAnalyticAccount(models.Model):
    _name = "account.analytic.account"
    _inherit = "account.analytic.account"

    timesheet_account_allowed_product_categ_ids = fields.Many2many(
        string="Allowed Product Categories",
        comodel_name="product.category",
        relation="rel_timesheet_account_2_product_categ",
        column1="analytic_account_id",
        column2="product_categ_id",
    )
    timesheet_account_allowed_product_ids = fields.Many2many(
        string="Allowed Product",
        comodel_name="product.product",
        domain=[("type", "=", "service")],
        relation="rel_timesheet_account_2_product",
        col1="analytic_account_id",
        col2="product_id",
    )
