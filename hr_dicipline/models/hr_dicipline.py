# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api, _
from openerp.exceptions import Warning as UserError


class HrDicipline(models.Model):
    _name = "hr.dicipline"
    _description = "Employee Dicipline"
    _inherit = [
        "mail.thread",
        "base.sequence_document",
        "base.workflow_policy_object",
    ]

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id

    @api.model
    def _default_employee_id(self):
        employees = self.env.user.employee_ids
        if len(employees) > 0:
            employee = employees[0]
        return employee.id

    @api.multi
    @api.depends(
        "type_id",
    )
    def _compute_policy(self):
        _super = super(HrDicipline, self)
        _super._compute_policy()

    @api.multi
    @api.depends(
        "type_id",
    )
    def _compute_allowed_reason_ids(self):
        for document in self:
            document.allowed_reason_ids = document.type_id.reason_ids.ids

    name = fields.Char(
        string="# Document",
        required=True,
        default="/",
        copy=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="hr.dicipline_type",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    reason_id = fields.Many2one(
        string="Reason",
        comodel_name="hr.dicipline_reason",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    allowed_reason_ids = fields.Many2many(
        string="Allowed Reasons",
        comodel_name="hr.dicipline_reason",
        compute="_compute_allowed_reason_ids",
    )
    employee_id = fields.Many2one(
        string="Employee",
        comodel_name="hr.employee",
        default=lambda self: self._default_employee_id(),
        required=True,
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
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        required=True,
        default=lambda self: self._default_company_id(),
    )
    state = fields.Selection(
        string="State",
        copy=False,
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("approve", "Approved"),
            ("open", "On Progress"),
            ("done", "Valid"),
            ("cancel", "Cancelled"),
        ],
        required=True,
        readonly=True,
        default="draft",
    )
    note = fields.Text(
        string="Note",
    )

    # Log Fields
    confirm_date = fields.Datetime(
        string="Confirmation Date",
        readonly=True,
        copy=False,
    )
    confirm_user_id = fields.Many2one(
        string="Confirmation By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )
    approve_date = fields.Datetime(
        string="Approved Date",
        readonly=True,
        copy=False,
    )
    approve_user_id = fields.Many2one(
        string="Approved By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )
    open_date = fields.Datetime(
        string="Opened Date",
        readonly=True,
        copy=False,
    )
    open_user_id = fields.Many2one(
        string="Opened By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )
    done_date = fields.Datetime(
        string="Done Date",
        readonly=True,
        copy=False,
    )
    done_user_id = fields.Many2one(
        string="Done By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )
    cancel_date = fields.Datetime(
        string="Cancellation Date",
        readonly=True,
        copy=False,
    )
    cancel_user_id = fields.Many2one(
        string="Cancellation By",
        comodel_name="res.users",
        readonly=True,
        copy=False,
    )

    # Policy Fields
    confirm_ok = fields.Boolean(
        string="Can Confirm",
        compute="_compute_policy",
    )
    approve_ok = fields.Boolean(
        string="Can Approve",
        compute="_compute_policy",
    )
    open_ok = fields.Boolean(
        string="Can Open",
        compute="_compute_policy",
    )
    done_ok = fields.Boolean(
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

    @api.model
    def create(self, values):
        _super = super(HrDicipline, self)
        result = _super.create(values)
        sequence = result._create_sequence()
        result.write({
            "name": sequence,
        })
        return result

    @api.multi
    def unlink(self):
        strWarning = _("You can only delete data on draft state")
        for document in self:
            if document.state != "draft":
                if not self.env.context.get("force_unlink", False):
                    raise UserError(strWarning)
        _super = super(HrDicipline, self)
        _super.unlink()

    @api.multi
    def button_confirm(self):
        for document in self:
            document.write(document._prepare_confirm_data())

    @api.multi
    def button_approve(self):
        for document in self:
            document.write(document._prepare_approve_data())

    @api.multi
    def button_open(self):
        for document in self:
            document.write(document._prepare_open_data())

    @api.multi
    def button_done(self):
        for document in self:
            document.write(document._prepare_done_data())

    @api.multi
    def button_cancel(self):
        for document in self:
            document.write(document._prepare_cancel_data())

    @api.multi
    def button_restart(self):
        for document in self:
            document.write(document._prepare_restart_data())

    @api.multi
    def _prepare_confirm_data(self):
        self.ensure_one()
        result = {
            "state": "confirm",
            "confirm_date": fields.Datetime.now(),
            "confirm_user_id": self.env.user.id,
        }
        return result

    @api.multi
    def _prepare_approve_data(self):
        self.ensure_one()
        result = {
            "state": "approve",
            "approve_date": fields.Datetime.now(),
            "approve_user_id": self.env.user.id,
        }
        return result

    @api.multi
    def _prepare_open_data(self):
        self.ensure_one()
        result = {
            "state": "open",
            "open_date": fields.Datetime.now(),
            "open_user_id": self.env.user.id,
        }
        return result

    @api.multi
    def _prepare_cancel_data(self):
        self.ensure_one()
        result = {
            "state": "cancel",
            "cancel_date": fields.Datetime.now(),
            "cancel_user_id": self.env.user.id,
        }
        return result

    @api.multi
    def _prepare_done_data(self):
        self.ensure_one()
        result = {
            "state": "done",
            "done_date": fields.Datetime.now(),
            "done_user_id": self.env.user.id,
        }
        return result

    @api.multi
    def _prepare_restart_data(self):
        self.ensure_one()
        result = {
            "state": "draft",
            "confirm_date": False,
            "confirm_user_id": False,
            "approve_date": False,
            "approve_user_id": False,
            "open_date": False,
            "open_user_id": False,
            "done_date": False,
            "done_user_id": False,
            "cancel_date": False,
            "cancel_user_id": False,
        }
        return result

    @api.onchange("type_id")
    def _onchange_reason_id(self):
        self.reason_id = False

    @api.onchange("employee_id")
    def _onchange_department_id(self):
        self.department_id = False
        if self.employee_id:
            self.department_id = self.employee_id.department_id
