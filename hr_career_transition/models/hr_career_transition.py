# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api, _
from openerp.exceptions import Warning as UserError


class HrCareerTransition(models.Model):
    _name = "hr.career_transition"
    _inherit = ["mail.thread", "base.sequence_document",
                "base.workflow_policy_object"]
    _description = "Career Transition"
    _order = "effective_date desc, id"

    @api.multi
    @api.depends(
        "type_id",
    )
    def _compute_policy(self):
        _super = super(HrCareerTransition, self)
        _super._compute_policy()

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id

    @api.model
    def _default_type_id(self):
        return False

    @api.model
    def _default_employee_id(self):
        employees = self.env.user.employee_ids
        if len(employees) > 0:
            employee = employees[0]
        return employee.id

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
    employee_id = fields.Many2one(
        string="Employee",
        comodel_name="hr.employee",
        default=lambda self: self._default_employee_id(),
        ondelete="restrict",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="hr.career_transition_type",
        default=lambda self: self._default_type_id(),
        ondelete="restrict",
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
    archieve = fields.Boolean(
        string="Archieve",
        default=False,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    require_reason = fields.Boolean(
        string="Require Reason",
        related="type_id.require_reason",
        store=False,
        readonly=True,
    )
    reason_id = fields.Many2one(
        string="Reason",
        comodel_name="hr.career_transition_type_reason",
        ondelete="restrict",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    # Contract
    previous_contract_id = fields.Many2one(
        string="Previous Contract",
        comodel_name="hr.contract",
        ondelete="restrict",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    new_contract_id = fields.Many2one(
        string="New Contract",
        comodel_name="hr.contract",
        ondelete="restrict",
        readonly=True,
    )
    create_new_contract = fields.Boolean(
        string="Create New Contract",
        related="type_id.create_new_contract",
        store=False,
        readonly=True,
    )
    need_previous_contract = fields.Boolean(
        string="Need Previous Contract",
        related="type_id.need_previous_contract",
        store=False,
        readonly=True,
    )
    contract_start_date = fields.Date(
        string="Contract Date Start",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    contract_end_date = fields.Date(
        string="Contract Date End",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    contract_type_id = fields.Many2one(
        string="Contract Type",
        comodel_name="hr.contract.type",
        ondelete="restrict",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    # New Data
    new_company_id = fields.Many2one(
        string="New Company",
        comodel_name="res.company",
        ondelete="restrict",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    new_department_id = fields.Many2one(
        string="New Department",
        comodel_name="hr.department",
        ondelete="restrict",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    new_job_id = fields.Many2one(
        string="New Job Title",
        comodel_name="hr.job",
        ondelete="restrict",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    new_working_hour_id = fields.Many2one(
        string="New Working Schedule",
        comodel_name="resource.calendar",
        ondelete="restrict",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    # Previous Data
    previous_company_id = fields.Many2one(
        string="Previous Company",
        comodel_name="res.company",
    )
    previous_department_id = fields.Many2one(
        string="Previous Department",
        comodel_name="hr.department",
    )
    previous_job_id = fields.Many2one(
        string="Previous Job Title",
        comodel_name="hr.job",
    )
    previous_working_hour_id = fields.Many2one(
        string="Previous Working Schedule",
        comodel_name="resource.calendar",
    )
    # Data Change Policy
    change_company = fields.Boolean(
        related="type_id.change_company",
        string="Change Company?",
        readonly=True,
    )
    change_job_title = fields.Boolean(
        related="type_id.change_job_title",
        string="Change Job Title",
        readonly=True,
    )
    change_department = fields.Boolean(
        related="type_id.change_department",
        string="Change Department",
        readonly=True,
    )
    change_working_schedule = fields.Boolean(
        related="type_id.change_working_schedule",
        string="Change Working Schedule",
        readonly=True,
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
            ("valid", "Valid"),
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
        for transition in self:
            transition.write(self._prepare_confirm_data())

    @api.multi
    def action_approve(self):
        for transition in self:
            transition.write(self._prepare_approve_data())

    @api.multi
    def action_valid(self):
        for transition in self:
            transition.write(self._prepare_valid_data())

    @api.multi
    def action_cancel(self):
        for transition in self:
            transition.write(self._prepare_cancel_data())

    @api.multi
    def action_restart(self):
        for transition in self:
            transition.write(self._prepare_restart_data())

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
        contract = self._create_update_contract()
        result = {
            "state": "valid",
            "validated_user_id": self.env.user.id,
            "validated_date": fields.Datetime.now(),
            "new_contract_id": contract and contract.id or False,
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

    @api.model
    def create(self, values):
        _super = super(HrCareerTransition, self)
        result = _super.create(values)
        result.write({
            "name": result._create_sequence(),
        })
        return result

    @api.onchange("previous_company_id")
    def onchange_new_company_id(self):
        self.new_company_id = self.previous_company_id

    @api.onchange("previous_department_id")
    def onchange_new_department_id(self):
        self.new_department_id = self.previous_department_id

    @api.onchange("previous_job_id")
    def onchange_new_job_id(self):
        self.new_job_id = self.previous_job_id

    @api.onchange("previous_working_hour_id")
    def onchange_new_working_hour_id(self):
        self.new_working_hour_id = self.previous_working_hour_id

    @api.onchange("previous_contract_id")
    def onchange_previous_working_hour_id(self):
        self.previous_working_hour_id = False
        if self.previous_contract_id:
            contract = self.previous_contract_id
            self.previous_working_hour_id = contract.working_hours

    @api.onchange("previous_contract_id")
    def onchange_previous_job_id(self):
        self.previous_job_id = False
        if self.previous_contract_id:
            contract = self.previous_contract_id
            self.previous_job_id = contract.job_id

    @api.onchange("previous_contract_id")
    def onchange_previous_department_id(self):
        self.previous_department_id = False
        if self.previous_contract_id:
            contract = self.previous_contract_id
            self.previous_department_id = contract.department_id

    @api.onchange("previous_contract_id")
    def onchange_previous_company_id(self):
        self.previous_company_id = False
        if self.previous_contract_id:
            contract = self.previous_contract_id
            self.previous_company_id = contract.company_id

    @api.onchange("employee_id")
    def onchange_previous_contract_id(self):
        self.previous_contract_id = False
        if self.employee_id and self.need_previous_contract:
            self.previous_contract_id = \
                self.employee_id.contract_id

    @api.onchange("type_id")
    def onchange_reason_id(self):
        self.reason_id = False

    @api.multi
    def _prepare_new_contract(self):
        self.ensure_one()
        return {
            # "name": "-",
            "employee_id": self.employee_id.id,
            "job_id": self.new_job_id and \
            self.new_job_id.id or \
            False,
            "type_id": self.contract_type_id.id,
            "date_start": self.contract_start_date,
            "date_end": self.contract_end_date,
            "working_hours": self.new_working_hour_id and \
            self.new_working_hour_id.id or \
            False,
            "wage": 0.0,
            "department_id": self.new_department_id and \
            self.new_department_id.id or \
            False,
            "company_id": self.new_company_id and \
            self.new_company_id.id or \
            False,
        }

    @api.multi
    def _prepare_contract_update(self):
        self.ensure_one()
        return {
            "job_id": self.new_job_id and
            self.new_job_id.id or
            False,
            "working_hours": self.new_working_hour_id and
            self.new_working_hour_id.id or
            False,
            "department_id": self.new_department_id and
            self.new_department_id.id or
            False,
            "company_id": self.new_company_id and
            self.new_company_id.id or
            False,
        }

    @api.multi
    def _create_update_contract(self):
        self.ensure_one()
        obj_contract = self.env["hr.contract"]
        result = False
        if self.create_new_contract and not self.archieve:
            result = obj_contract.create(self._prepare_new_contract())
        elif not self.create_new_contract and not self.archieve:
            self.previous_contract_id.write(self._prepare_contract_update())
            result = self.previous_contract_id
        return result

    @api.multi
    def _update_contract(self):
        self.ensure_one()
        self.previous_contract_id.write(self._prepare_contract_update())

    @api.multi
    def unlink(self):
        strWarning = _("You can only delete data on draft state")
        for transition in self:
            if transition.state != "draft":
                if not self.env.context.get("force_unlink", False):
                    raise UserError(strWarning)
        _super = super(HrCareerTransition, self)
        _super.unlink()
