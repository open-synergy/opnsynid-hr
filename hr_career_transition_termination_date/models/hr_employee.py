# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.multi
    @api.depends(
        "termination_transition_ids",
        "termination_transition_ids.effective_date",
        "termination_transition_ids.state",
    )
    def _compute_termination_date(self):
        for employee in self:
            termination_date = False
            termination_transition_id = False
            terminations = employee.termination_transition_ids.\
                filtered(lambda r: r.state == "valid")
            if len(terminations) > 0:
                termination = terminations[0]
                termination_date = termination.effective_date
                termination_transition_id = termination.id
            employee.date_termination = termination_date
            employee.termination_transition_id = termination_transition_id

    date_termination = fields.Date(
        string="Termination Date",
        compute="_compute_termination_date",
        store=True,
        readonly=True,
    )
    termination_transition_id = fields.Many2one(
        string="Termination Transition",
        comodel_name="hr.termination_transition",
        compute="_compute_termination_date",
        store=True,
        readonly=True,
    )
