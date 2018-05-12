# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _


class HrTrainingParticipantEvaluation(models.Model):
    _name = "hr.training_participant_evaluation"
    _description = "Employee Training Participant Evaluation"
    _order = "sequence, id"
    _inherit = ["mail.thread"]

    participant_id = fields.Many2one(
        string="Participant",
        comodel_name="hr.training_partisipant",
        required=True,
        ondelete="cascade",
    )
    training_id = fields.Many2one(
        string="Training",
        comodel_name="hr.training",
        related="participant_id.training_id",
        store=True,
    )
    pre_post_test = fields.Selection(
        string="Pre/Post Evaluation",
        selection=[
            ("pre", "Pre Evaluation"),
            ("post", "Post Evaluation"),
        ],
        required=False,
        related="training_evaluation_id.pre_post_test",
        store=True,
    )
    training_evaluation_id = fields.Many2one(
        string="Training Evaluation",
        comodel_name="hr.training_evaluation",
        required=True,
        ondelete="cascade",
    )
    survey_id = fields.Many2one(
        string="Survey",
        comodel_name="survey.survey",
        related="training_evaluation_id.survey_id",
        required=False,
    )
    respon_id = fields.Many2one(
        string="Respon",
        comodel_name="survey.user_input",
        ondelete="set null",
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=5,
    )
    note = fields.Text(
        string="Note",
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("waiting", "In Progress"),
            ("done", "Done"),
            ("cancel", "Cancel"),
        ],
        required=True,
        default="draft",
    )

    @api.multi
    def action_start(self):
        for evaluation in self:
            evaluation.write(self._prepare_start_data())
            evaluation.respon_id.action_survey_resent()

    @api.multi
    def action_done(self):
        for evaluation in self:
            evaluation.write(self._prepare_done_data())

    @api.multi
    def action_cancel(self):
        for evaluation in self:
            evaluation.write(self._prepare_cancel_data())

    @api.multi
    def action_restart(self):
        for evaluation in self:
            evaluation.write(self._prepare_restart_data())

    @api.multi
    def action_start_survey(self):
        self.ensure_one()
        context = {
            "survey_token": self.respon_id.token,
        }
        return self.survey_id.with_context(context).action_start_survey()

    @api.multi
    def _prepare_start_data(self):
        self.ensure_one()
        respon = self._create_survey_request()
        return {
            "state": "waiting",
            "respon_id": respon.id,
        }

    @api.multi
    def _prepare_done_data(self):
        self.ensure_one()
        return {
            "state": "done",
        }

    @api.multi
    def _prepare_cancel_data(self):
        self.ensure_one()
        return {
            "state": "cancel",
        }

    @api.multi
    def _prepare_restart_data(self):
        self.ensure_one()
        return {
            "state": "draft",
        }

    @api.multi
    def _create_survey_request(self):
        self.ensure_one()
        obj_request = self.env["survey.user_input"]
        return obj_request.create(self._prepare_survey_request())

    @api.multi
    def _prepare_survey_request(self):
        self.ensure_one()
        return {
            "survey_id": self.survey_id.id,
            "type": "link",
            "partner_id": self._get_partner().id,
        }

    @api.multi
    def _get_partner(self):
        self.ensure_one()
        employee = self.participant_id.partisipant_id
        user = employee.user_id
        if not user:
            warning_msg = _("Please link employee to user")
            raise UserError(warning_msg)
        return user.partner_id

    @api.constrains(
        "state",
        "respon_id")
    def _check_survey_respon_ok(self):
        if self.state == "done" and self.respon_id.state != "done":
            warning_msg = _("Evaluation is not finish!")
            raise UserError(warning_msg)
