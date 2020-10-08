# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.multi
    @api.depends(
        "contract_ids",
        "contract_ids.date_start",
    )
    def _compute_current_contract(self):
        for employee in self:
            contract = False
            if employee.contract_ids:
                contracts = employee.contract_ids.sorted(
                    key=lambda r: r.date_start, reverse=True)
                if len(contracts) > 0:
                    contract = contracts[0]
            employee.current_contract_id = contract

    current_contract_id = fields.Many2one(
        string="Current Contract",
        comodel_name="hr.contract",
        compute="_compute_current_contract",
        store=True,
    )
    job_id = fields.Many2one(
        string="Job Title",
        comodel_name="hr.job",
        related="current_contract_id.job_id",
        readonly=True,
        store=True,
    )
    contract_type_id = fields.Many2one(
        string="Contract Type",
        comodel_name="hr.contract.type",
        related="current_contract_id.type_id",
        store=True,
        readonly=True,
    )
