# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrApplicant(models.Model):
    _name = "hr.applicant"
    _inherit = ["hr.applicant"]

    recruitment_request_id = fields.Many2one(
        string="# Recruitment Request",
        comodel_name="hr.recruitment_request",
    )
