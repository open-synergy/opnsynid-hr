# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class HrContractType(models.Model):
    _name = "hr.contract.type"
    _inherit = "hr.contract.type"

    employment_status_id = fields.Many2one(
        string="Employment Status",
        comodel_name="hr.employment_status",
    )
