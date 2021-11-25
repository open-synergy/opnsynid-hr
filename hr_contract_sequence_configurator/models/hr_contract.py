# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class HrContract(models.Model):
    _name = "hr.contract"
    _inherit = [
        "hr.contract",
        "base.sequence_document",
    ]

    @api.model
    def _default_name(self):
        return "/"

    name = fields.Char(
        default=lambda self: self._default_name(),
        string="# Document",
    )

    @api.model
    def create(self, values):
        _super = super(HrContract, self)
        result = _super.create(values)
        sequence = result._create_sequence()
        result.write(
            {
                "name": sequence,
            }
        )
        return result
