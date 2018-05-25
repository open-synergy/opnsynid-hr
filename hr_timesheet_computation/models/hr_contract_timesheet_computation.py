# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields
from openerp.tools.translate import _


class HrContractTimesheetComputation(models.Model):
    _name = "hr.contract_timesheet_computation"
    _description = "Contract's Timesheet Computation"

    contract_id = fields.Many2one(
        string="Contract",
        comodel_name="hr.contract",
    )
    item_id = fields.Many2one(
        string="Computation Item",
        comodel_name="hr.timesheet_computation_item",
        required=True,
    )

    _sql_constrains = [
        ("item_unique", "unique(contract_id, item_id)",
         _("No duplicate item")),
    ]
