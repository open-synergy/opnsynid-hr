# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    termination_transition_ids = fields.One2many(
        string="Termination Transitions",
        comodel_name="hr.termination_transition",
        inverse_name="employee_id",
    )
