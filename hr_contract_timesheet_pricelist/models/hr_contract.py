# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrContract(models.Model):
    _name = "hr.contract"
    _inherit = "hr.contract"

    timesheet_pricelist_ids = fields.One2many(
        string="Timesheet Pricelist",
        comodel_name="hr.contract_timesheet_pricelist",
        inverse_name="contract_id",
    )
