# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    department_id = fields.Many2one(
        string="Department",
        comodel_name="hr.department",
        related="current_contract_id.contract_department_id",
        store=True,
        readonly=True,
    )
    parent_id = fields.Many2one(
        string="Manager",
        comodel_name="hr.employee",
        related="current_contract_id.contract_department_id.manager_id",
        store=True,
        readonly=True,
    )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        related="contract_id.company_id",
        store=True,
        readonly=True,
    )
