# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models


class HrTerminationTransition(models.Model):
    _name = "hr.termination_transition"
    _inherit = ["hr.career_transition", "hr.termination_transition"]
