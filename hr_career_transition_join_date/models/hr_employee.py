# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.multi
    @api.depends(
        "join_transition_ids",
        "join_transition_ids.effective_date",
        "join_transition_ids.state",
    )
    def _compute_join_date(self):
        for employee in self:
            join_date = False
            join_transition_id = False
            joins = employee.join_transition_ids.\
                filtered(lambda r: r.state == "valid")
            if len(joins) > 0:
                join = joins[0]
                join_date = join.effective_date
                join_transition_id = join.id
            employee.date_join = join_date
            employee.join_transition_id = join_transition_id

    date_join = fields.Date(
        string="Join Date",
        compute="_compute_join_date",
        store=True,
        readonly=True,
    )
    join_transition_id = fields.Many2one(
        string="Join Transition",
        comodel_name="hr.join_transition",
        compute="_compute_join_date",
        store=True,
        readonly=True,
    )
