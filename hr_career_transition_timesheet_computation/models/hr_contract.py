# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class HrContract(models.Model):
    _inherit = "hr.contract"

    @api.multi
    def _get_timesheet_computation_item_dict(self):
        self.ensure_one()
        result = []
        for ts_item in self.computation_ids:
            result.append(
                (
                    0,
                    0,
                    {
                        "item_id": ts_item.item_id.id,
                    },
                )
            )
        return result
