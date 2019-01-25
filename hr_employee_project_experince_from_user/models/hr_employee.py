# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    project_experience_ids = fields.One2many(
        string="Project Experiences",
        comodel_name="hr.employee_project_experience_report",
        inverse_name="employee_id",
    )
