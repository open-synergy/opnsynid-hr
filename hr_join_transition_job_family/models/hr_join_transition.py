# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models


class HrJoinTransition(models.Model):
    _name = "hr.join_transition"
    _inherit = ["hr.career_transition", "hr.join_transition"]
