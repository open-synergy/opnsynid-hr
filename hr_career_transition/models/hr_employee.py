# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.multi
    @api.depends(
        "career_transition_ids",
        "career_transition_ids.state",
    )
    def _compute_career_transition(self):
        for employee in self:
            transition = False
            transitions = employee.career_transition_ids.\
                filtered(lambda r: r.state == "valid")
            if len(transitions) > 0:
                transition = transitions[0]
            employee.latest_career_transition_id = transition

    career_transition_ids = fields.One2many(
        string="Career Transitions",
        comodel_name="hr.career_transition",
        inverse_name="employee_id",
    )
    latest_career_transition_id = fields.Many2one(
        string="Latest Career Transition",
        comodel_name="hr.career_transition",
        compute="_compute_career_transition",
        store=True,
        readonly=True,
    )
