# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class HrAnalyticTimesheet(models.Model):
    _name = "hr.analytic.timesheet"
    _inherit = "hr.analytic.timesheet"

    timesheet_account_allowed_product_categ_ids = fields.Many2many(
        string="Allowed Product Categories",
        comodel_name="product.category",
        related="account_id.timesheet_account_allowed_product_categ_ids",
        readonly=True,
    )
    timesheet_account_allowed_product_ids = fields.Many2many(
        string="Allowed Product",
        comodel_name="product.product",
        related="account_id.timesheet_account_allowed_product_ids",
        readonly=True,
    )
