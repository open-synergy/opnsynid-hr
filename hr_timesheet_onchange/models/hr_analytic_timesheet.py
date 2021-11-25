# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError


class HrAnalyticTimesheet(models.Model):
    _name = "hr.analytic.timesheet"
    _inherit = "hr.analytic.timesheet"

    @api.depends(
        "product_id",
    )
    def _compute_allowed_product_uom_ids(self):
        obj_uom = self.env["product.uom"]
        for document in self:
            result = []
            if document.product_id:
                uom_categ = document.product_id.uom_id.category_id
                criteria = [
                    ("category_id", "=", uom_categ.id),
                ]
                result = obj_uom.search(criteria).ids
            document.allowed_product_uom_ids = result

    allowed_product_uom_ids = fields.Many2many(
        string="Allowed Product UoM(s)",
        comodel_name="product.uom",
        compute="_compute_allowed_product_uom_ids",
        store=False,
    )

    @api.onchange(
        "user_id",
    )
    def onchange_product_id(self):
        self.product_id = False
        if self.user_id:
            if len(self.user_id.employee_ids) > 0:
                employee = self.user_id.employee_ids[0]
                self.product_id = employee.product_id

    @api.onchange(
        "user_id",
    )
    def onchange_journal_id(self):
        self.journal_id = False
        if self.user_id:
            if len(self.user_id.employee_ids) > 0:
                employee = self.user_id.employee_ids[0]
                self.journal_id = employee.journal_id

    @api.onchange(
        "product_id",
        "journal_id",
    )
    def onchange_general_account_id(self):
        account = False
        is_sale_line = False

        if self.journal_id:
            if self.journal_id.type == "sale":
                is_sale_line = True

        if self.product_id:
            product = self.product_id
            if is_sale_line:
                account = product.property_account_income
                if not account:
                    account = product.categ_id.property_account_income_categ
                if not account:
                    err_msg = _("No income product defined for this product")
                    raise UserError(err_msg)
            else:
                account = product.property_account_expense
                if not account:
                    account = product.categ_id.property_account_expense_categ
                if not account:
                    err_msg = _("No expense product defined for this product")
                    raise UserError(err_msg)

        self.general_account_id = account

    @api.onchange(
        "product_id",
    )
    def onchange_uom_id(self):
        self.product_uom_id = False
        if self.product_id:
            self.product_uom_id = self.product_id.uom_id

    @api.onchange(
        "product_id",
        "unit_amount",
        "journal_id",
        "product_uom_id",
    )
    def onchange_amount(self):
        is_sale_line = False
        obj_price_type = self.env["product.price.type"]
        obj_precision = self.env["decimal.precision"]
        result = 0.0

        ctx = self.env.context.copy()
        if self.product_uom_id:
            ctx["uom"] = self.product_uom_id.id

        if self.journal_id:
            if self.journal_id.type == "sale":
                is_sale_line = True

        if self.product_id:
            product = self.product_id
            if is_sale_line:
                criteria = [
                    ("field", "=", "list_price"),
                ]
                price_type = obj_price_type.search(criteria)[0]
            else:
                criteria = [
                    ("field", "=", "standard_price"),
                ]
                price_type = obj_price_type.search(criteria)[0]

            amount_unit = product.with_context(ctx).price_get(price_type.field)[
                self.product_id.id
            ]

            prec = obj_precision.precision_get("Account")
            amount = amount_unit * self.unit_amount or 0.0
            result = round(amount, prec)
            if not is_sale_line:
                result *= -1.0
        self.amount = result
