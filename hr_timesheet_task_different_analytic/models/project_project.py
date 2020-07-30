# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProjectProject(models.Model):
    _name = "project.project"
    _inherit = "project.project"

    allowed_alternate_analytic_account_ids = fields.Many2many(
        string="Allowed Alternate Analytic Account",
        comodel_name="account.analytic.account",
        column1="project_id",
        column2="analytic_account_id",
        relation="rel_alternate_project_analytic_account",
        domain=[
            ("type", "in", ["normal", "contract"]),
            ("use_timesheets", "=", True),
        ],
    )
