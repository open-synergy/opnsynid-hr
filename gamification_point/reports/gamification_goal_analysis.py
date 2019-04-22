# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class GamificationGoalAnalysis(models.Model):
    _inherit = "gamification.goal_analysis"
    _auto = False

    point = fields.Float(
        string="Point",
    )

    def _select(self):
        _super = super(GamificationGoalAnalysis, self)
        select_str = _super._select()
        select_str += """
        ,
        SUM(a.point) AS point
        """
        return select_str
