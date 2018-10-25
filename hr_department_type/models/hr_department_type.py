# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class HrDepartmentType(models.Model):
    _name = "hr.department.type"

    name = fields.Char(
        string="Name",
        required=True
    )
    description = fields.Text(
        string="Description"
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )
