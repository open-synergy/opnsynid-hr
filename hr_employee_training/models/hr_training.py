# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _


class HrTraining(models.Model):
    _name = "hr.training"
    _description = "Employee Training"
    _order = "date_start desc, id"

    @api.multi
    @api.depends(
        "company_id",
    )
    def _compute_policy(self):
        user_group_ids = self.env.user.groups_id.ids
        for training in self:
            can_confirm = can_approve = can_start = \
                can_finish = can_cancel = \
                can_restart = True
            company = training.company_id

            confirm_group_ids = company.\
                employee_training_allowed_confirm_group_ids.ids
            if confirm_group_ids:
                if not (set(user_group_ids) & set(confirm_group_ids)):
                    can_confirm = False

            approve_group_ids = company.\
                employee_training_allowed_approve_group_ids.ids
            if approve_group_ids:
                if not (set(user_group_ids) & set(approve_group_ids)):
                    can_approve = False

            start_group_ids = company.\
                employee_training_allowed_start_group_ids.ids
            if start_group_ids:
                if not (set(user_group_ids) & set(start_group_ids)):
                    can_start = False

            finish_group_ids = company.\
                employee_training_allowed_finish_group_ids.ids
            if finish_group_ids:
                if not (set(user_group_ids) & set(finish_group_ids)):
                    can_finish = False

            cancel_group_ids = company.\
                employee_training_allowed_cancel_group_ids.ids
            if cancel_group_ids:
                if not (set(user_group_ids) & set(cancel_group_ids)):
                    can_cancel = False

            restart_group_ids = company.\
                employee_training_allowed_restart_group_ids.ids
            if restart_group_ids:
                if not (set(user_group_ids) & set(restart_group_ids)):
                    can_restart = False

            training.confirm_ok = can_confirm
            training.approve_ok = can_approve
            training.start_ok = can_start
            training.finish_ok = can_finish
            training.cancel_ok = can_cancel
            training.restart_ok = can_restart

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id

    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        required=True,
        default=lambda self: self._default_company_id(),
    )
    name = fields.Char(
        string="Training Name",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    source_document = fields.Char(
        string="Source Document",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    category_id = fields.Many2one(
        string="Category",
        comodel_name="hr.training_category",
        required=True,
        domain=[
            ("type", "=", "normal"),
        ],
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    method_ids = fields.Many2many(
        string="Training Method",
        comodel_name="hr.training_method",
        relation="rel_training_2_training_method",
        column1="training_id",
        column2="training_method_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    vendor_ids = fields.Many2many(
        string="Vendor",
        comodel_name="res.partner",
        relation="rel_training_vendor",
        column1="training_id",
        column2="partner_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    date_start = fields.Datetime(
        string="Date Start",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    date_end = fields.Datetime(
        string="Date End",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    is_public = fields.Boolean(
        string="Is Public",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    training_purpose_ids = fields.Many2many(
        string="Training Purpose",
        comodel_name="hr.training_purpose",
        relation="rel_training_2_purpose",
        column1="training_id",
        column2="purpose_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    training_syllabus_id = fields.Many2many(
        string="Training Syllabus",
        comodel_name="hr.training_syllabus",
        relation="rel_training_2_syllabus",
        column1="training_id",
        column2="syllabus_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    request_by_id = fields.Many2one(
        string="Request By",
        comodel_name="hr.employee",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    responsible_id = fields.Many2one(
        string="Primary PIC",
        comodel_name="hr.employee",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    secondary_responsible_id = fields.Many2one(
        string="Secondary PIC",
        comodel_name="hr.employee",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    participant_type_id = fields.Many2one(
        string="Default Participant Type",
        comodel_name="hr.training_participant_type",
        required=True,
        readonly=False,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("approve", "Approved"),
            ("start", "Started"),
            ("finish", "Finished"),
            ("cancel", "Cancelled"),
        ],
        required=True,
        default="draft",
    )
    cancel_reason_id = fields.Many2one(
        string="Cancel Reason",
        comodel_name="hr.training_cancel_reason",
    )
    note = fields.Text(
        string="Note",
    )
    trainer_ids = fields.Many2many(
        string="Trainer",
        comodel_name="res.partner",
        relation="rel_training_2_trainer",
        column1="training_id",
        columns2="partner_id",
        domain=[
            ("is_company", "=", False),
        ],
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    observer_ids = fields.Many2many(
        string="Observer",
        comodel_name="res.partner",
        relation="rel_training_2_observer",
        column1="training_id",
        columns2="partner_id",
        domain=[
            ("is_company", "=", False),
        ],
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    partisipant_ids = fields.One2many(
        string="Partisipants",
        comodel_name="hr.training_partisipant",
        inverse_name="training_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    session_ids = fields.One2many(
        string="Sessions",
        comodel_name="hr.training_session",
        inverse_name="training_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    confirm_ok = fields.Boolean(
        string="Can Confirm",
        compute="_compute_policy",
    )
    approve_ok = fields.Boolean(
        string="Can Approve",
        compute="_compute_policy",
    )
    start_ok = fields.Boolean(
        string="Can Start",
        compute="_compute_policy",
    )
    finish_ok = fields.Boolean(
        string="Can Finish",
        compute="_compute_policy",
    )
    cancel_ok = fields.Boolean(
        string="Can Cancel",
        compute="_compute_policy",
    )
    restart_ok = fields.Boolean(
        string="Can Restart",
        compute="_compute_policy",
    )

    @api.multi
    def button_confirm(self):
        for training in self:
            training.write(self._prepare_confirm_data())

    @api.multi
    def button_approve(self):
        for training in self:
            training.write(self._prepare_approve_data())

    @api.multi
    def button_start(self):
        for training in self:
            training.write(self._prepare_start_data())

    @api.multi
    def button_finish(self):
        for training in self:
            training.write(self._prepare_finish_data())

    @api.multi
    def button_cancel(self):
        for training in self:
            training.write(self._prepare_cancel_data())

    @api.multi
    def button_restart(self):
        for training in self:
            training.write(self._prepare_restart_data())

    @api.multi
    def button_generate_attendance(self):
        for training in self:
            training._generate_attendance()

    @api.model
    def _prepare_confirm_data(self):
        result = {
            "state": "confirm",
        }
        return result

    @api.model
    def _prepare_approve_data(self):
        result = {
            "state": "approve",
        }
        return result

    @api.model
    def _prepare_start_data(self):
        result = {
            "state": "start",
        }
        return result

    @api.model
    def _prepare_finish_data(self):
        result = {
            "state": "finish",
        }
        return result

    @api.model
    def _prepare_cancel_data(self):
        result = {
            "state": "cancel",
        }
        return result

    @api.model
    def _prepare_restart_data(self):
        result = {
            "state": "draft",
        }
        return result

    @api.multi
    def _generate_attendance(self):
        self.ensure_one()
        for session in self.session_ids:
            session.button_generate_attendance()

    @api.constrains("state")
    def _check_session_close(self):
        strWarning = _("There are unfinished session(s)")
        if self.state == "finish":
            for session in self.session_ids:
                if session.state not in ["finish", "cancel"]:
                    raise UserError(strWarning)

    @api.constrains("date_start", "date_end")
    def _check_duration(self):
        strWarning = _("Date end must be greater than date start")
        if self.date_start and self.date_end:
            if self.date_end < self.date_start:
                raise UserError(strWarning)
