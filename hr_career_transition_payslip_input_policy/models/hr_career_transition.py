# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrCareerTransition(models.Model):
    _inherit = "hr.career_transition"

    # New Data
    new_input_type_ids = fields.One2many(
        string="New Input Types",
        comodel_name="hr.career_transition_new_input_type",
        inverse_name="career_transition_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    previous_input_type_ids = fields.One2many(
        string="Previous Input Types",
        comodel_name="hr.career_transition_previous_input_type",
        inverse_name="career_transition_id",
    )
    change_input_type = fields.Boolean(
        string="Change Payslip Input?",
        related="type_id.change_input_type",
    )

    @api.multi
    def unpdate_input_type_ids(self):
        self.ensure_one()
        value = {
            "new_input_type_ids": [],
            "previous_input_type_ids": [],
        }
        self.new_input_type_ids.unlink()
        self.previous_input_type_ids.unlink()
        if self.previous_contract_id:
            contract = self.previous_contract_id
            for input_type in contract.input_type_ids:
                value["new_input_type_ids"].append((0, 0, {
                    "input_type_id": input_type.input_type_id.id,
                    "amount": input_type.amount,
                }))
                value["previous_input_type_ids"].append((0, 0, {
                    "input_type_id": input_type.input_type_id.id,
                    "amount": input_type.amount,
                }))
        self.write(value)

    @api.multi
    def _prepare_new_contract(self):
        _super = super(HrCareerTransition, self)
        result = _super._prepare_new_contract()
        input_types = []
        for input_type in self.new_input_type_ids:
            input_types.append((0, 0, {
                "input_type_id": input_type.input_type_id.id,
                "amount": input_type.amount,
            }))
        result.update({
            "input_type_ids": input_types,
        })
        return result

    @api.multi
    def _prepare_contract_update(self):
        _super = super(HrCareerTransition, self)
        result = _super._prepare_contract_update()
        self.previous_contract_id.input_type_ids.unlink()
        input_types = []
        for input_type in self.new_input_type_ids:
            input_types.append((0, 0, {
                "input_type_id": input_type.input_type_id.id,
                "amount": input_type.amount,
            }))
        result.update({
            "input_type_ids": input_types,
        })
        return result


class HrCareerTransitionPreviousInputType(models.Model):
    _name = "hr.career_transition_previous_input_type"
    _description = "Career Transition Previous Input Type Policy"

    career_transition_id = fields.Many2one(
        string="Career Transition",
        comodel_name="hr.career_transition",
        required=True,
        ondelete="cascade",
    )
    input_type_id = fields.Many2one(
        string="Input Type",
        comodel_name="hr.payslip.input_type",
        required=True,
        ondelete="restrict",
    )
    amount = fields.Float(
        string="Amount",
        require=True,
    )


class HrCareerTransitionNewInputType(models.Model):
    _name = "hr.career_transition_new_input_type"
    _description = "Career Transition New Input Type Policy"

    career_transition_id = fields.Many2one(
        string="Career Transition",
        comodel_name="hr.career_transition",
        required=True,
        ondelete="cascade",
    )
    input_type_id = fields.Many2one(
        string="Input Type",
        comodel_name="hr.payslip.input_type",
        required=True,
        ondelete="restrict",
    )
    amount = fields.Float(
        string="Amount",
        require=True,
    )
