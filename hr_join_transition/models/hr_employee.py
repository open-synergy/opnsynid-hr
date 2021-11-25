# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.multi
    @api.depends(
        "join_transition_ids",
        "join_transition_ids.state",
    )
    def _compute_career_transition(self):
        _super = super(HrEmployee, self)
        _super._compute_career_transition()

    join_transition_ids = fields.One2many(
        string="Join Transitions",
        comodel_name="hr.join_transition",
        inverse_name="employee_id",
    )
