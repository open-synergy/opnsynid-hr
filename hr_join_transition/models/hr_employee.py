# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    join_transition_ids = fields.One2many(
        string="Join Transitions",
        comodel_name="hr.join_transition",
        inverse_name="employee_id",
    )
