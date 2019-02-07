# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api, _
from openerp.exceptions import Warning as UserError


class HrRecruitmentRequest(models.Model):
    _name = "hr.recruitment_request"
    _inherit = ["mail.thread", "base.sequence_document",
                "base.workflow_policy_object"]
    _description = "Recruitment Request"

    @api.multi
    @api.depends(
        "department_id",
        "company_id",
    )
    def _compute_policy(self):
        _super = super(HrRecruitmentRequest, self)
        _super._compute_policy()

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id

    @api.model
    def _default_user_id(self):
        return self.env.user.id

    name = fields.Char(
        string="# Document",
        required=True,
        default="/",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    ref = fields.Char(
        string="# Reference",
        required=True,
        default="/",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        default=lambda self: self._default_company_id(),
        ondelete="restrict",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    department_id = fields.Many2one(
        string="Department",
        comodel_name="hr.department",
        required=True,
        ondelete="restrict",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    user_id = fields.Many2one(
        string="Request By",
        comodel_name="res.users",
        required=True,
        ondelete="restrict",
        default=lambda self: self._default_user_id(),
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    job_id = fields.Many2one(
        string="Job Position",
        comodel_name="hr.job",
        required=True,
        ondelete="restrict",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    replacement_id = fields.Many2one(
        string="Replacement for",
        comodel_name="hr.employee",
        ondelete="restrict",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    num_of_request = fields.Integer(
        string="Num. of Requested Employee",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    effective_date = fields.Date(
        string="Effective Date",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    note = fields.Text(
        string="Note",
    )
    state = fields.Selection(
        string="State",
        required=True,
        readonly=True,
        track_visibility="onchange",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("open", "On Progress"),
            ("valid", "Done"),
            ("cancel", "Cancel"),
        ],
        default="draft",
        copy=False,
    )
    # Log Fields
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
    opened_date = fields.Datetime(
        string="Opened Date",
        readonly=True,
        copy=False,
    )
    opened_user_id = fields.Many2one(
        string="Open By",
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
    # Policy Fields
    confirm_ok = fields.Boolean(
        string="Can Confirm",
        compute="_compute_policy",
        store=False,
        readonly=True,
    )
    open_ok = fields.Boolean(
        string="Can Open",
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

    @api.multi
    def action_confirm(self):
        for rec_request in self:
            rec_request.write(rec_request._prepare_confirm_data())

    @api.multi
    def action_approve(self):
        for rec_request in self:
            rec_request.write(rec_request._prepare_approve_data())
            rec_request.job_id.write(rec_request._prepare_job_opening())

    @api.multi
    def action_valid(self):
        for rec_request in self:
            rec_request.write(rec_request._prepare_valid_data())
            rec_request._close_job_recruitment()

    @api.multi
    def action_cancel(self):
        for rec_request in self:
            rec_request.write(rec_request._prepare_cancel_data())

    @api.multi
    def action_restart(self):
        for rec_request in self:
            rec_request.write(rec_request._prepare_restart_data())

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
    def _prepare_approve_data(self):
        self.ensure_one()
        result = {
            "state": "open",
            "opened_user_id": self.env.user.id,
            "opened_date": fields.Datetime.now(),

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
    def _prepare_restart_data(self):
        self.ensure_one()
        result = {
            "state": "draft",
            "confirmed_user_id": False,
            "confirmed_date": False,
            "validated_user_id": False,
            "validated_date": False,
            "cancelled_user_id": False,
            "cancelled_date": False,
        }
        return result

    @api.multi
    def _prepare_job_opening(self):
        self.ensure_one()
        return {
            "state": "recruit",
        }

    @api.multi
    def _prepare_job_closing(self):
        self.ensure_one()
        return {
            "state": "open",
        }

    @api.multi
    def _close_job_recruitment(self):
        self.ensure_one()
        if self.job_id.num_active_recruitment_request == 0:
            self.job_id.write(self._prepare_job_closing())

    @api.model
    def create(self, values):
        _super = super(HrRecruitmentRequest, self)
        result = _super.create(values)
        result.write({
            "name": result._create_sequence(),
        })
        return result

    @api.multi
    def unlink(self):
        strWarning = _("You can only delete data on draft state")
        for rec_request in self:
            if rec_request.state != "draft":
                if not self.env.context.get("force_unlink", False):
                    raise UserError(strWarning)
        _super = super(HrRecruitmentRequest, self)
        _super.unlink()

    @api.onchange("job_id")
    def onchange_employee_id(self):
        self.replacement_id = False
