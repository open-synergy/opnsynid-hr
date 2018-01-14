# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrTraining(models.Model):
    _name = "hr.training"
    _description = "Employee Training"

    name = fields.Char(
        string="Training Name",
        required=True,
    )
    source_document = fields.Char(
        string="Source Document",
    )
    category_id = fields.Many2one(
        string="Category",
        comodel_name="hr.training_category",
        required=True,
        domain=[
            ("type", "=", "normal"),
        ],
    )
    method_ids = fields.Many2many(
        string="Training Method",
        comodel_name="hr.training_method",
        relation="rel_training_2_training_method",
        column1="training_id",
        column2="training_method_id",
    )
    vendor_ids = fields.Many2many(
        string="Vendor",
        comodel_name="res.partner",
        relation="rel_training_vendor",
        column1="training_id",
        column2="partner_id",
    )
    date_start = fields.Date(
        string="Date Start",
        required=True,
    )
    date_end = fields.Date(
        string="Date End",
        required=True,
    )
    is_public = fields.Boolean(
        string="Is Public",
    )
    training_purpose_ids = fields.Many2many(
        string="Training Purpose",
        comodel_name="hr.training_purpose",
        relation="rel_training_2_purpose",
        column1="training_id",
        column2="purpose_id",
    )
    training_syllabus_id = fields.Many2many(
        string="Training Syllabus",
        comodel_name="hr.training_syllabus",
        relation="rel_training_2_syllabus",
        column1="training_id",
        column2="syllabus_id",
    )
    request_by_id = fields.Many2one(
        string="Request By",
        comodel_name="hr.employee",
        required=True,
    )
    responsible_id = fields.Many2one(
        string="PIC",
        comodel_name="hr.employee",
        required=True,
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
    )
    observer_ids = fields.Many2many(
        string="Observer",
        comodel_name="res.partner",
        relation="rel_training_2_observer",
        column1="training_id",
        columns2="partner_id",
    )
    partisipant_ids = fields.One2many(
        string="Partisipants",
        comodel_name="hr.training_partisipant",
        inverse_name="training_id",
    )
    session_ids = fields.One2many(
        string="Sessions",
        comodel_name="hr.training_session",
        inverse_name="training_id",
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
