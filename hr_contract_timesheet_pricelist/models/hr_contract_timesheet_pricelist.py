# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrContractTimesheetPricelist(models.Model):
    _name = "hr.contract_timesheet_pricelist"
    _description = "Employee Contract Timesheet Pricelist"

    contract_id = fields.Many2one(
        string="Contract",
        comodel_name="hr.contract",
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
