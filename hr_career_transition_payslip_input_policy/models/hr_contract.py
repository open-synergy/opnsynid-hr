# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class HrContract(models.Model):
    _inherit = "hr.contract"

    @api.multi
    def _get_input_types_dict(self):
        self.ensure_one()
        result = []
        for input_type in self.input_type_ids:
            result.append(
                (
                    0,
                    0,
                    {
                        "input_type_id": input_type.input_type_id.id,
                        "amount": input_type.amount,
                    },
                )
            )
        return result
