# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrContract(models.Model):
    _inherit = "hr.contract"

    @api.model
    def _default_employee_id(self):
        if len(self.env.user.employee_ids) > 0:
            return self.env.user.employee_ids[0].id

    contract_department_id = fields.Many2one(
        string="Department",
        comodel_name="hr.department",
        readonly=False,
    )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
    )
    employee_id = fields.Many2one(
        default=lambda self: self._default_employee_id(),
    )

    @api.onchange("employee_id")
    def onchange_contract_department_id(self):
        self.contract_department_id = False
        if self.employee_id:
            self.contract_department_id = self.employee_id.department_id

    @api.onchange("employee_id")
    def onchange_company_id(self):
        self.company_id = False
        if self.employee_id:
            self.company_id = self.employee_id.company_id

    @api.onchange("employee_id")
    def onchange_job_id(self):
        self.job_id = False
        if self.employee_id:
            self.job_id = self.employee_id.job_id
