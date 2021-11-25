# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.multi
    @api.depends(
        "termination_transition_ids",
        "termination_transition_ids.state",
    )
    def _compute_career_transition(self):
        _super = super(HrEmployee, self)
        _super._compute_career_transition()

    termination_transition_ids = fields.One2many(
        string="Termination Transitions",
        comodel_name="hr.termination_transition",
        inverse_name="employee_id",
    )
