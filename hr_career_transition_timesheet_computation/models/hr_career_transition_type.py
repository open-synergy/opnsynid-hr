# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class HrCareerTransitionType(models.Model):
    _inherit = "hr.career_transition_type"

    change_timesheet_computation = fields.Boolean(
        string="Change Timesheet Computation?",
    )
