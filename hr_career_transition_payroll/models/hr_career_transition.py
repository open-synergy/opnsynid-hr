# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class HrCareerTransition(models.Model):
    _inherit = "hr.career_transition"

    # New Data
    new_salary_structure_id = fields.Many2one(
        string="New Salary Structure",
        comodel_name="hr.payroll.structure",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    previous_salary_structure_id = fields.Many2one(
        string="Previous Salery Structure",
        comodel_name="hr.payroll.structure",
    )
    change_salary_structure = fields.Boolean(
        string="Change Salary Structure?",
        related="type_id.change_salary_structure",
    )

    @api.onchange("previous_salary_structure_id")
    def onchange_new_salary_structure_id(self):
        self.new_salary_structure_id = self.previous_salary_structure_id

    @api.multi
    def _get_value_before_onchange_previous_contract(self):
        _super = super(HrCareerTransition, self)
        result = _super._get_value_before_onchange_previous_contract()
        result.update(
            {
                "previous_salary_structure_id": False,
            }
        )
        return result

    @api.multi
    def _get_value_after_onchange_previous_contract(self, previous_contract):
        _super = super(HrCareerTransition, self)
        result = _super._get_value_after_onchange_previous_contract(previous_contract)
        result.update(
            {
                "previous_salary_structure_id": previous_contract.struct_id,
            }
        )
        return result

    @api.multi
    def _prepare_new_contract(self):
        _super = super(HrCareerTransition, self)
        result = _super._prepare_new_contract()
        result.update(
            {
                "struct_id": self.new_salary_structure_id
                and self.new_salary_structure_id.id
                or False,
            }
        )
        return result

    @api.multi
    def _prepare_contract_update(self):
        _super = super(HrCareerTransition, self)
        result = _super._prepare_contract_update()
        result.update(
            {
                "struct_id": self.new_salary_structure_id
                and self.new_salary_structure_id.id
                or False,
            }
        )
        return result

    @api.multi
    def _prepare_contract_revert(self):
        _super = super(HrCareerTransition, self)
        result = _super._prepare_contract_revert()
        result.update(
            {
                "struct_id": self.previous_salary_structure_id
                and self.previous_salary_structure_id.id
                or False,
            }
        )
        return result
