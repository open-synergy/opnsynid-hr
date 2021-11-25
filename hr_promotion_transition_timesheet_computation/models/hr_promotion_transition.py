# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models


class HrPromotionTransition(models.Model):
    _name = "hr.promotion_transition"
    _inherit = ["hr.promotion_transition", "hr.career_transition"]
