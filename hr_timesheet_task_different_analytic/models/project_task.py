# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = "project.task"

    allowed_alternate_analytic_account_ids = fields.Many2many(
        string="Allowed Alternate Analytic Account",
        comodel_name="account.analytic.account",
        related="project_id.allowed_alternate_analytic_account_ids",
        store=False,
    )
