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
        _super = super(HrAnalyticTimesheet, self)
        _super.onchange_pricelist_id()
        obj_pricelist = self.env["hr.contract_timesheet_pricelist"]

        if not self.pricelist_id and \
                self.user_id and \
                self.product_id:
            employees = self.user_id.employee_ids
            if len(employees) > 0:
                # TODO: Revisit later
                employee = employees[0]
                if employee.contract_id:
                    contract = employee.contract_id
                    criteria = [
                        ("contract_id", "=", contract.id),
                        ("product_id", "=", self.product_id.id),
                    ]
                    price_items = obj_pricelist.search(criteria)
                    if len(price_items) > 0:
                        self.pricelist_id = price_items[0].pricelist_id.id
