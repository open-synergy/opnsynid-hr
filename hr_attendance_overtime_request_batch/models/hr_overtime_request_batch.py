# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api, SUPERUSER_ID
from openerp.exceptions import Warning as UserError
from datetime import datetime
from openerp.tools.translate import _


class HrOvertimeRequestBatch(models.Model):
    _name = "hr.overtime_request_batch"
    _description = "Overtime Request Batches"

    name = fields.Char(
        string="# Batch",
        required=True,
        readonly=True,
        states={
            "draft": [("readonly", False)]
        },
        default="/",
    )
    user_id = fields.Many2one(
        string="User",
        comodel_name="res.users",
        readonly=True,
        states={
            "draft": [("readonly", False)]
        },
        default=lambda self: self.env.user
    )

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id.id

    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        default=lambda self: self._default_company_id(),
        readonly=False,
    )
    department_id = fields.Many2one(
        string="Department",
        comodel_name="hr.department",
        readonly=True,
        states={
            "draft": [("readonly", False)]
        },
    )
    manager_id = fields.Many2one(
        string="Manager",
        comodel_name="hr.employee",
        readonly=True,
        states={
            "draft": [("readonly", False)]
        },
    )
    date_start = fields.Datetime(
        string="Date Start",
        required=True,
        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        readonly=True,
        states={
            "draft": [("readonly", False)]
        },
    )
    date_end = fields.Datetime(
        string="Date End",
        required=True,
        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        readonly=True,
        states={
            "draft": [("readonly", False)]
        },
    )
    request_ids = fields.One2many(
        string="Overtime Request(s)",
        comodel_name="hr.overtime_request",
        inverse_name="request_batch_id",
        readonly=True,
    )

    @api.multi
    @api.depends(
        "state",
        "company_id",
    )
    def _compute_policy(self):
        for batch in self:
            if self.env.user.id == SUPERUSER_ID:
                batch.confirm_ok = batch.valid_ok = \
                    batch.cancel_ok = \
                    batch.settodraft_ok = \
                    batch.generate_ok = True
                continue

            if batch.company_id:
                company = batch.company_id
                for policy in company.\
                        _get_overtime_batch_button_policy_map():
                    setattr(
                        batch,
                        policy[0],
                        company.
                        _get_overtime_batch_button_policy(
                            policy[1]),
                    )

    confirm_ok = fields.Boolean(
        string="Can Confirm",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    valid_ok = fields.Boolean(
        string="Can Validate",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    cancel_ok = fields.Boolean(
        string="Can Cancel",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    restart_ok = fields.Boolean(
        string="Can Restart",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    generate_ok = fields.Boolean(
        string="Can Generate",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    confirmed_date = fields.Datetime(
        string="Confirmation Date",
        readonly=True,
        copy=False,
    )
    confirmed_user_id = fields.Many2one(
        string="Confirmation By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )
    validated_date = fields.Datetime(
        string="Validation Date",
        readonly=True,
        copy=False,
    )
    validated_user_id = fields.Many2one(
        string="Validation By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )
    cancelled_date = fields.Datetime(
        string="Cancellation Date",
        readonly=True,
        copy=False,
    )
    cancelled_user_id = fields.Many2one(
        string="Cancellation By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )
    state = fields.Selection(
        string="State",
        required=True,
        readonly=True,
        track_visibility="onchange",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("valid", "Valid"),
            ("cancel", "Cancel"),
        ],
        default="draft",
        copy=False,
    )

    @api.model
    def _prepare_create_data(self, values):
        name = values.get("name", False)
        company_id = values.get("company_id", False)
        if not name or name == "/":
            values["name"] = self._create_sequence(company_id)
        return values

    @api.model
    def _get_sequence(self, company_id):
        company = self.env["res.company"].browse([company_id])[0]

        if company.overtime_request_batch_sequence_id:
            result = company.overtime_request_batch_sequence_id
        else:
            result = self.env.ref(
                "hr_attendance_overtime_request_batch."
                "sequence_batch_overtime_request")
        return result

    @api.model
    def _create_sequence(self, company_id):
        name = self.env["ir.sequence"].\
            next_by_id(self._get_sequence(company_id).id) or "/"
        return name

    @api.model
    def create(self, values):
        new_values = self._prepare_create_data(values)
        return super(HrOvertimeRequestBatch, self).create(new_values)

    @api.multi
    def action_confirm(self):
        for overtime in self:
            overtime.write(overtime._prepare_confirm_data())
            overtime.request_ids.action_confirm()

    @api.multi
    def action_valid(self):
        for overtime in self:
            overtime.write(overtime._prepare_valid_data())
            overtime.request_ids.action_valid()

    @api.multi
    def action_cancel(self):
        for overtime in self:
            overtime.write(overtime._prepare_cancel_data())
            overtime.request_ids.action_cancel()

    @api.multi
    def action_restart(self):
        for overtime in self:
            overtime.write(overtime._prepare_restart())
            overtime.request_ids.action_restart()

    @api.multi
    def _prepare_confirm_data(self):
        self.ensure_one()
        result = {
            "state": "confirm",
            "confirmed_user_id": self.env.user.id,
            "confirmed_date": fields.Datetime.now(),
        }
        return result

    @api.multi
    def _prepare_valid_data(self):
        self.ensure_one()
        result = {
            "state": "valid",
            "validated_user_id": self.env.user.id,
            "validated_date": fields.Datetime.now(),
        }
        return result

    @api.multi
    def _prepare_cancel_data(self):
        self.ensure_one()
        result = {
            "state": "cancel",
            "cancelled_user_id": self.env.user.id,
            "cancelled_date": fields.Datetime.now(),
        }
        return result

    @api.multi
    def _prepare_restart(self):
        self.ensure_one()
        return {
            "state": "draft",
            "confirmed_user_id": False,
            "confirmed_date": False,
            "validated_user_id": False,
            "validated_date": False,
            "cancelled_user_id": False,
            "cancelled_date": False,
        }

    @api.constrains(
        "date_start", "date_end")
    def _check_date(self):
        strWarning = _(
            "Date start must be greater than date end")
        if self.date_start and self.date_end:
            if self.date_start > self.date_end:
                raise UserError(_("%s") % (strWarning))
