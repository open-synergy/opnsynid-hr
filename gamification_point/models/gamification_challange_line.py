# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class GamificationChallangeLine(models.Model):
    _inherit = "gamification.challenge.line"

    reach_point = fields.Float(
        string="Point Assigned When Goal Reached",
        required=True,
        default=0.0,
    )
    fail_point = fields.Float(
        string="Point Assigned When Goal Failed",
        required=True,
        default=0.0,
    )
