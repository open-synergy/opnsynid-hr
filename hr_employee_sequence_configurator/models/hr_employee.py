# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class HrEmployee(models.Model):
    _name = "hr.employee"
    _inherit = [
        "hr.employee",
        "base.sequence_document",
    ]

    identification_id = fields.Char(
        string="Identification No",
        default="/",
        required=True,
        copy=False,
    )

    @api.model
    def create(self, values):
        _super = super(HrEmployee, self)
        result = _super.create(values)
        sequence = result._create_sequence()
        result.write({
            "identification_id": sequence,
        })
        return result
