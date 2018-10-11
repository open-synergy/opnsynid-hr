# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class HrHolidayBatchCommon(models.AbstractModel):
    _name = "hr.holiday_batch_common"
    _description = "Abstract Class for Holiday Batch"

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
        comodel_name="hr.department"
    )
    holiday_status_id = fields.Many2one(
        string="Leave Type",
        comodel_name="hr.holidays.status",
        required=True,
        readonly=True,
        states={
            'draft': [('readonly', False)]
        }
    )
    holiday_type = fields.Selection(
        string="Mode",
        selection=[
            ('employee', 'By Employee'),
            ('category', 'By Employee Tag')
        ],
        required=True,
        readonly=True,
        states={
            'draft': [('readonly', False)]
        },
        default="employee"
    )
    type = fields.Selection(
        string="Type",
        selection=[
            ('remove', 'Leave Request'),
            ('add', 'Allocation Request')
        ]
    )

    @api.multi
    @api.depends(
        "state",
        "company_id",
    )
    def _compute_policy(self):
        pass

    confirm_ok = fields.Boolean(
        string="Can Confirm",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    valid_ok = fields.Boolean(
        string="Can Approve",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    refuse_ok = fields.Boolean(
        string="Can Refuse",
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
    refused_date = fields.Datetime(
        string="Refused Date",
        readonly=True,
        copy=False,
    )
    refused_user_id = fields.Many2one(
        string="Refused By",
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
            ('draft', 'To Submit'),
            ('cancel', 'Cancelled'),
            ('confirm', 'To Approve'),
            ('refuse', 'Refused'),
            ('validate', 'Approved')
        ],
        default="draft",
        copy=False,
    )

    @api.multi
    def action_confirm(self):
        for holiday in self:
            holiday.write(holiday._prepare_confirm_data())

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
    def action_valid(self):
        for holiday in self:
            holiday.write(holiday._prepare_valid_data())

    @api.multi
    def _prepare_valid_data(self):
        self.ensure_one()
        result = {
            "state": "validate",
            "validated_user_id": self.env.user.id,
            "validated_date": fields.Datetime.now(),
        }
        return result

    @api.multi
    def action_refuse(self):
        for holiday in self:
            holiday.write(holiday._prepare_refuse_data())

    @api.multi
    def _prepare_refuse_data(self):
        self.ensure_one()
        result = {
            "state": "refuse",
            "refused_user_id": self.env.user.id,
            "refused_date": fields.Datetime.now(),
        }
        return result

    @api.multi
    def action_cancel(self):
        for holiday in self:
            holiday.write(holiday._prepare_cancel_data())

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
    def action_restart(self):
        for holiday in self:
            holiday.write(holiday._prepare_set_to_draft())

    @api.multi
    def _prepare_set_to_draft(self):
        self.ensure_one()
        return {
            "state": "draft",
            "confirmed_user_id": False,
            "confirmed_date": False,
            "validated_user_id": False,
            "validated_date": False,
            "refused_user_id": False,
            "refused_date": False,
            "cancelled_user_id": False,
            "cancelled_date": False,
        }
