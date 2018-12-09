# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrContract(models.Model):
    _inherit = "hr.contract"

    computation_ids = fields.One2many(
        string="Timesheet Computations",
        comodel_name="hr.contract_timesheet_computation",
        inverse_name="contract_id",
    )
