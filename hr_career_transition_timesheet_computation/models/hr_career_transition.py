# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrCareerTransition(models.Model):
    _inherit = "hr.career_transition"

    # New Data
    new_timesheet_computation_ids = fields.One2many(
        string="New Timesheet Computations",
        comodel_name="hr.career_transition_new_timesheet_computation",
        inverse_name="career_transition_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    previous_timesheet_computation_ids = fields.One2many(
        string="Previous Timesheet Computations",
        comodel_name="hr.career_transition_previous_timesheet_computation",
        inverse_name="career_transition_id",
    )
    change_timesheet_computation = fields.Boolean(
        string="Change Timesheet Computation?",
        related="type_id.change_timesheet_computation",
    )

    @api.multi
    def update_computation_ids(self):
        self.ensure_one()
        value = {
            "new_timesheet_computation_ids": [],
            "previous_timesheet_computation_ids": [],
        }
        self.new_timesheet_computation_ids.unlink()
        self.previous_timesheet_computation_ids.unlink()
        if self.previous_contract_id:
            contract = self.previous_contract_id
            for ts_computation in contract.computation_ids:
                value["new_timesheet_computation_ids"].append((0, 0, {
                    "item_id": ts_computation.item_id.id,
                }))
                value["previous_timesheet_computation_ids"].append((0, 0, {
                    "item_id": ts_computation.item_id.id,
                }))
        self.write(value)

    @api.multi
    def _prepare_new_contract(self):
        _super = super(HrCareerTransition, self)
        result = _super._prepare_new_contract()
        computations = []
        for computation in self.new_timesheet_computation_ids:
            computations.append((0, 0, {
                "item_id": computation.item_id.id,
            }))
        result.update({
            "computation_ids": computations,
        })
        return result

    @api.multi
    def _prepare_contract_update(self):
        _super = super(HrCareerTransition, self)
        result = _super._prepare_contract_update()
        self.previous_contract_id.computation_ids.unlink()
        computations = []
        for computation in self.new_timesheet_computation_ids:
            computations.append((0, 0, {
                "item_id": computation.item_id.id,
            }))
        result.update({
            "computation_ids": computations,
        })
        return result


class HrCareerTransitionNewTimesheetComputation(models.Model):
    _name = "hr.career_transition_new_timesheet_computation"
    _description = "Career Transition New Timesheet Computation"

    career_transition_id = fields.Many2one(
        string="Career Transition",
        comodel_name="hr.career_transition",
    )
    item_id = fields.Many2one(
        string="Computation Item",
        comodel_name="hr.timesheet_computation_item",
        required=True,
    )


class HrCareerTransitionPreviousTimesheetComputation(models.Model):
    _name = "hr.career_transition_previous_timesheet_computation"
    _description = "Career Transition Previous Timesheet Computation"

    career_transition_id = fields.Many2one(
        string="Career Transition",
        comodel_name="hr.career_transition",
    )
    item_id = fields.Many2one(
        string="Computation Item",
        comodel_name="hr.timesheet_computation_item",
        required=True,
    )
