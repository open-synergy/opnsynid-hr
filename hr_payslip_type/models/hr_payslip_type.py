# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class HrPayslipType(models.Model):
    _name = "hr.payslip.type"
    _description = "Type of Payslip"

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
