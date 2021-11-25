# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class HrEmployee(models.Model):
    _name = "hr.employee"
    _inherit = [
        "hr.employee",
        "base.sequence_document",
    ]

    employee_code = fields.Char(
        string="Employee Code",
        default="/",
        required=True,
        copy=False,
    )

    @api.multi
    def action_create_identification_id(self):
        for document in self:
            document._create_identification_id()

    @api.multi
    def _create_identification_id(self):
        self.ensure_one()
        sequence = self._create_sequence()
        self.write(
            {
                "employee_code": sequence,
            }
        )
