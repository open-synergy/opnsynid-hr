# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api, fields


class GamificationGoal(models.Model):
    _inherit = "gamification.goal"

    @api.multi
    @api.depends(
        "definition_id",
        "state",
        "closed",
        "line_id",
        "current",
    )
    def _compute_point(self):
        for rec in self:
            if rec.state == "reached":
                if rec.line_id.reach_point_method == "fixed":
                    rec.point = rec.line_id.reach_point
                elif rec.line_id.reach_point_method == "multiply":
                    rec.point = rec.line_id.reach_point * rec.current
            elif rec.state == "failed":
                if rec.line_id.fail_point_method == "fixed":
                    rec.point = rec.line_id.fail_point
                elif rec.line_id.fail_point_method == "multiply":
                    rec.point = rec.line_id.fail_point * rec.current

    point = fields.Float(
        string="Point",
        required=True,
        default=0.0,
        compute="_compute_point",
        store=True,
    )
