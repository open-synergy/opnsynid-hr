# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class HrCareerTransitionType(models.Model):
    _inherit = "hr.career_transition_type"

    change_job_grade = fields.Boolean(
        string="Change Job Grade?",
    )
