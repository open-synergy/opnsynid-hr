# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrCareerTransition(models.Model):
    _inherit = "hr.career_transition"

    # New Data
    new_analytic_account_id = fields.Many2one(
        string="New Analytic Account",
        comodel_name="account.analytic.account",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    previous_analytic_account_id = fields.Many2one(
        string="Previous Analytic Account",
        comodel_name="account.analytic.account",
    )
    change_analytic_account = fields.Boolean(
        string="Change Analytic Account?",
        related="type_id.change_analytic_account",
    )

    @api.onchange("previous_salary_structure_id")
    def onchange_new_analytic_account_id(self):
        self.new_analytic_account_id = self.previous_analytic_account_id

    @api.onchange("previous_contract_id")
    def onchange_previous_analytic_account_id(self):
        self.previous_analytic_account_id = False
        if self.previous_contract_id:
            contract = self.previous_contract_id
            self.previous_analytic_account_id = contract.analytic_account_id

    @api.multi
    def _prepare_new_contract(self):
        _super = super(HrCareerTransition, self)
        result = _super._prepare_new_contract()
        result.update({
            "analytic_account_id": self.new_analytic_account_id and
            self.new_analytic_account_id.id or
            False,
        })
        return result

    @api.multi
    def _prepare_contract_update(self):
        _super = super(HrCareerTransition, self)
        result = _super._prepare_contract_update()
        result.update({
            "analytic_account_id": self.new_analytic_account_id and
            self.new_analytic_account_id.id or
            False,
        })
        return result
