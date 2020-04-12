# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api


class HrAnalyticTimesheet(models.Model):
    _name = "hr.analytic.timesheet"
    _inherit = "hr.analytic.timesheet"

    @api.onchange(
        "account_id",
        "user_id",
        "product_id",
    )
    def onchange_pricelist_id(self):
        self.pricelist_id = False
        obj_ts_pricelist = self.env["hr.analytic_account_timesheet_pricelist"]
        if self.account_id and self.user_id and self.product_id:
            criteria = [
                ("analytic_account_id", "=", self.account_id.id),
                ("user_id", "=", self.user_id.id),
                ("product_id", "=", self.product_id.id)
            ]
            ts_pricelists = obj_ts_pricelist.search(criteria)
            if len(ts_pricelists) > 0:
                self.pricelist_id = ts_pricelists[0].pricelist_id.id

    @api.onchange(
        "product_id",
        "unit_amount",
        "journal_id",
        "product_uom_id",
        "pricelist_id",
        "date",
    )
    def onchange_amount(self):
        _super = super(HrAnalyticTimesheet, self)
        _super.onchange_amount()

        is_sale_line = False
        obj_uom = self.env["product.uom"]
        obj_precision = self.env["decimal.precision"]

        if self.journal_id:
            if self.journal_id.type == "sale":
                is_sale_line = True

        if self.pricelist_id:
            pricelist = self.pricelist_id
            ctx1 = {}
            if self.date:
                ctx1.update({"date": self.date})
            amount_unit = pricelist.with_context(ctx1).price_get(
                prod_id=self.product_id.id,
                qty=self.unit_amount)[pricelist.id]
            amount = obj_uom._compute_price(
                self.product_id.uom_id.id,
                amount_unit,
                self.product_uom_id.id) * self.unit_amount

            prec = obj_precision.precision_get("Account")
            result = round(amount, prec)
            if not is_sale_line:
                result *= -1.0

            self.amount = result
