# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError


class HrCareerTransition(models.Model):
    _name = "hr.career_transition"
    _description = "Career Transition"
    _inherit = [
        "mail.thread",
        "base.sequence_document",
        "base.workflow_policy_object",
        "tier.validation",
    ]
    _state_from = [
        "draft",
        "confirm",
    ]
    _state_to = [
        "open",
    ]
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
    new_manager_id = fields.Many2one(
        string="New Manager",
        comodel_name="hr.employee",
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
    new_wage = fields.Float(
        string="New Wage",
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
    previous_manager_id = fields.Many2one(
        string="Previous Department",
        comodel_name="hr.employee",
    )
    previous_job_id = fields.Many2one(
        string="Previous Job Title",
        comodel_name="hr.job",
    )
    previous_working_hour_id = fields.Many2one(
        string="Previous Working Schedule",
        comodel_name="resource.calendar",
    )
    previous_wage = fields.Float(
        string="Previous Wage",
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
    change_manager = fields.Boolean(
        related="type_id.change_manager",
        string="Change Manager",
        readonly=True,
    )
    change_working_schedule = fields.Boolean(
        related="type_id.change_working_schedule",
        string="Change Working Schedule",
        readonly=True,
    )
    change_wage = fields.Boolean(
        related="type_id.change_wage",
        string="Change Wage",
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
    restart_approval_ok = fields.Boolean(
        string="Can Restart Approval",
        compute="_compute_policy",
    )

    @api.multi
    def action_confirm(self):
        for transition in self:
            transition.write(transition._prepare_confirm_data())
            transition.request_validation()

    @api.multi
    def action_approve(self):
        for transition in self:
            transition.write(transition._prepare_approve_data())

    @api.multi
    def action_valid(self):
        for transition in self:
            transition.write(transition._prepare_valid_data())

    @api.multi
    def action_cancel(self):
        for transition in self:
            if not transition._check_cant_cancel_latest_transition():
                msg = _("You can only cancel valid latest transition")
                raise UserError(msg)
            new_contract = False
            if transition.new_contract_id:
                new_contract = transition.new_contract_id
            transition.write(transition._prepare_cancel_data())
            if new_contract:
                new_contract.unlink()
            else:
                transition._revert_contract()
            transition.restart_validation()

    @api.multi
    def action_restart(self):
        for transition in self:
            transition.write(transition._prepare_restart_data())

    @api.multi
    def validate_tier(self):
        _super = super(HrCareerTransition, self)
        _super.validate_tier()
        for document in self:
            if document.validated:
                document.action_approve()

    @api.multi
    def restart_validation(self):
        _super = super(HrCareerTransition, self)
        _super.restart_validation()
        for document in self:
            document.request_validation()

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
            "new_contract_id": False,
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
        result.write(
            {
                "name": result._create_sequence(),
            }
        )
        return result

    @api.onchange("previous_company_id")
    def onchange_new_company_id(self):
        self.new_company_id = self.previous_company_id

    @api.onchange("previous_department_id")
    def onchange_new_department_id(self):
        self.new_department_id = self.previous_department_id

    @api.onchange("previous_manager_id")
    def onchange_new_manager_id(self):
        self.new_manager_id = self.previous_manager_id

    @api.onchange("previous_job_id")
    def onchange_new_job_id(self):
        self.new_job_id = self.previous_job_id

    @api.onchange("previous_working_hour_id")
    def onchange_new_working_hour_id(self):
        self.new_working_hour_id = self.previous_working_hour_id

    @api.onchange("previous_wage")
    def onchange_new_wage(self):
        self.new_wage = self.previous_wage

    @api.multi
    def onchange_previous_contract(self, previous_contract_id):
        value = self._get_value_before_onchange_previous_contract()
        domain = self._get_domain_before_onchange_previous_contract()

        if previous_contract_id:
            obj_contract = self.env["hr.contract"]
            previous_contract = obj_contract.browse([previous_contract_id])[0]
            value = self._get_value_after_onchange_previous_contract(previous_contract)
            domain = self._get_domain_after_onchange_previous_contract(
                previous_contract
            )
        return {"value": value, "domain": domain}

    @api.multi
    def _get_value_before_onchange_previous_contract(self):
        return {
            "previous_working_hour_id": False,
            "previous_job_id": False,
            "previous_department_id": False,
            "previous_manager_id": False,
            "previous_company_id": False,
            "previous_wage": 0.0,
        }

    @api.multi
    def _get_domain_before_onchange_previous_contract(self):
        return {}

    @api.multi
    def _get_value_after_onchange_previous_contract(self, previous_contract):
        return {
            "previous_working_hour_id": previous_contract.working_hours,
            "previous_job_id": previous_contract.job_id,
            "previous_department_id": previous_contract.contract_department_id,
            "previous_manager_id": previous_contract.manager_id,
            "previous_company_id": previous_contract.company_id,
            "previous_wage": previous_contract.wage,
        }

    @api.multi
    def _get_domain_after_onchange_previous_contract(self, previous_contract):
        return {}

    @api.onchange("employee_id", "archieve")
    def onchange_previous_contract_id(self):
        self.previous_contract_id = False
        if self.employee_id and self.need_previous_contract and not self.archieve:
            self.previous_contract_id = self.employee_id.contract_id

    @api.onchange("type_id")
    def onchange_reason_id(self):
        self.reason_id = False

    @api.multi
    def _prepare_new_contract(self):
        self.ensure_one()
        return {
            "employee_id": self.employee_id.id,
            "job_id": self.new_job_id and self.new_job_id.id or False,
            "type_id": self.contract_type_id.id,
            "date_start": self.contract_start_date,
            "date_end": self.contract_end_date,
            "working_hours": (
                self.new_working_hour_id and self.new_working_hour_id.id or False
            ),
            "wage": self.new_wage,
            "contract_department_id": (
                self.new_department_id and self.new_department_id.id or False
            ),
            "parent_id": (self.new_manager_id and self.new_manager_id.id or False),
            "company_id": (self.new_company_id and self.new_company_id.id or False),
        }

    @api.multi
    def _prepare_contract_update(self):
        self.ensure_one()
        return {
            "job_id": self.new_job_id and self.new_job_id.id or False,
            "working_hours": self.new_working_hour_id
            and self.new_working_hour_id.id
            or False,
            "contract_department_id": self.new_department_id
            and self.new_department_id.id
            or False,
            "company_id": self.new_company_id and self.new_company_id.id or False,
            "parent_id": self.new_manager_id and self.new_manager_id.id or False,
            "wage": self.new_wage,
        }

    @api.multi
    def _prepare_contract_revert(self):
        self.ensure_one()
        return {
            "job_id": self.previous_job_id and self.previous_job_id.id or False,
            "working_hours": self.previous_working_hour_id
            and self.previous_working_hour_id.id
            or False,
            "contract_department_id": self.previous_department_id
            and self.previous_department_id.id
            or False,
            "company_id": self.previous_company_id
            and self.previous_company_id.id
            or False,
            "parent_id": self.previous_manager_id
            and self.previous_manager_id.id
            or False,
            "wage": self.previous_wage,
        }

    @api.multi
    def _revert_contract(self):
        self.ensure_one()
        if self._check_revert_contract():
            self.previous_contract_id.write(self._prepare_contract_revert())

    @api.multi
    def _check_revert_contract(self):
        self.ensure_one()
        result = False
        if (
            self.need_previous_contract
            and self.previous_contract_id
            and not self.create_new_contract
            and not self.archieve
        ):
            result = True
        return result

    @api.multi
    def _create_update_contract(self):
        self.ensure_one()
        obj_contract = self.env["hr.contract"]
        result = False
        if self.create_new_contract and not self.archieve:
            result = obj_contract.create(self._prepare_new_contract())
        elif not self.create_new_contract and not self.archieve:
            self.previous_contract_id.write(self._prepare_contract_update())
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

    @api.constrains(
        "effective_date",
        "state",
    )
    def _constrain_check_effective_date(self):
        if self.state == "valid" and not self.archieve:
            criteria = [
                ("id", "!=", self.id),
                ("state", "=", "valid"),
                ("employee_id", "=", self.employee_id.id),
            ]
            obj_transition = self.env["hr.career_transition"]
            transitions = obj_transition.search(criteria)
            if len(transitions) > 0:
                last_transition = transitions[0]
                if self.effective_date < last_transition.effective_date:
                    msg = _(
                        "Effective date have to be greater than "
                        "lastest career transition"
                    )
                    raise UserError(msg)

    @api.constrains(
        "state",
    )
    def _check_contract_start_date_no_equal_effective_date(self):
        if self.state == "valid" and self.create_new_contract and not self.archieve:
            if self.contract_start_date != self.effective_date:
                msg = _("Contract start date have to be " "equal to effective date")
                raise UserError(msg)

    @api.constrains(
        "state",
    )
    def _check_contract_end_date_equal_less_start_date(self):
        if (
            self.state == "valid"
            and self.create_new_contract
            and self.contract_end_date
        ):
            if self.contract_end_date <= self.contract_start_date:
                msg = _("Contract date end have to be greater than start date")
                raise UserError(msg)

    @api.constrains(
        "state",
    )
    def _check_transition_limit(self):
        transition_count = self.employee_id._get_transition_count(
            self.type_id,
            self.reason_id,
        )
        transition_limit = self.type_id._get_transition_limit(
            self.reason_id,
        )
        if (
            self.state == "valid"
            and transition_limit != 0
            and transition_count > transition_limit
        ):
            msg = _("Career transition limit exceed")
            raise UserError(msg)

    @api.multi
    def _check_cant_cancel_latest_transition(self):
        self.ensure_one()
        result = True
        if (
            self.id != self.employee_id.latest_career_transition_id.id
            and not self.archieve
            and self.state == "valid"
        ):
            result = False
        return result
