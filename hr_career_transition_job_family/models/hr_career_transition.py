# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class HrCareerTransition(models.Model):
    _inherit = "hr.career_transition"

    @api.multi
    @api.depends("new_job_id")
    def _compute_job_grade(self):
        for transition in self:
            result = False
            if transition.new_job_id:
                result = transition.new_job_id.job_grade_ids.ids
            transition.allowed_job_grade_ids = result

    allowed_job_grade_ids = fields.Many2many(
        string="Job Grades",
        comodel_name="hr.job_grade",
        compute="_compute_job_grade",
        store=False,
    )

    # New Data
    new_job_grade_id = fields.Many2one(
        string="New Job Grade",
        comodel_name="hr.job_grade",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    previous_job_grade_id = fields.Many2one(
        string="Previous Job Grade",
        comodel_name="hr.job_grade",
    )
    change_job_grade = fields.Boolean(
        string="Change Job Grade?",
        related="type_id.change_job_grade",
    )

    @api.onchange("previous_job_grade_id", "new_job_id")
    def onchange_new_job_grade_id(self):
        self.new_job_grade_id = False

    @api.multi
    def _get_value_before_onchange_previous_contract(self):
        _super = super(HrCareerTransition, self)
        result = _super._get_value_before_onchange_previous_contract()
        result.update(
            {
                "previous_job_grade_id": False,
            }
        )
        return result

    @api.multi
    def _get_value_after_onchange_previous_contract(self, previous_contract):
        _super = super(HrCareerTransition, self)
        result = _super._get_value_after_onchange_previous_contract(previous_contract)
        result.update(
            {
                "previous_job_grade_id": previous_contract.job_grade_id,
            }
        )
        return result

    @api.multi
    def _prepare_new_contract(self):
        _super = super(HrCareerTransition, self)
        result = _super._prepare_new_contract()
        result.update(
            {
                "job_grade_id": self.new_job_grade_id
                and self.new_job_grade_id.id
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
                "job_grade_id": self.new_job_grade_id
                and self.new_job_grade_id.id
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
                "job_grade_id": self.previous_job_grade_id
                and self.previous_job_grade_id.id
                or False,
            }
        )
        return result
