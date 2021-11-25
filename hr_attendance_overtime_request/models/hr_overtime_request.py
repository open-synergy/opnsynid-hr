# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import api, fields, models
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _


class HrOvertimeRequest(models.Model):
    _name = "hr.overtime_request"
    _description = "Attendance Overtime Request"
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
        "valid",
    ]

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id.id

    @api.model
    def _default_employee_id(self):
        employees = self.env.user.employee_ids
        if len(employees) > 0:
            employee = employees[0]
        return employee.id

    @api.multi
    @api.depends("attendance_ids")
    def _compute_attendance(self):
        for overtime in self:
            attendances = overtime.attendance_ids.filtered(
                lambda r: r.action == "sign_in"
            ).sorted(key=lambda r: r.name)
            overtime.start_attendance_id = (
                attendances[0].id if len(attendances) > 0 else False
            )

            attendances = overtime.attendance_ids.filtered(
                lambda r: r.action == "sign_out"
            ).sorted(key=lambda r: r.name, reverse=True)
            overtime.end_attendance_id = (
                attendances[0].id if len(attendances) > 0 else False
            )

    @api.multi
    @api.depends("start_attendance_id", "date_start")
    def _compute_real_start(self):
        for overtime in self:
            overtime.real_date_start = False
            if not overtime.start_attendance_id or not overtime.date_start:
                continue

            if overtime.start_attendance_id.name <= overtime.date_start:
                overtime.real_date_start = overtime.date_start
            else:
                overtime.real_date_start = overtime.start_attendance_id.name

    @api.multi
    @api.depends("end_attendance_id", "date_end")
    def _compute_real_end(self):
        for overtime in self:
            overtime.real_date_end = False
            if not overtime.end_attendance_id or not overtime.date_end:
                continue

            if overtime.end_attendance_id.name <= overtime.date_end:
                overtime.real_date_end = overtime.end_attendance_id.name
            else:
                overtime.real_date_end = overtime.date_end

    @api.multi
    @api.depends("real_date_start", "real_date_end")
    def _compute_real(self):
        for overtime in self:
            overtime.real_overtime_hour = 0.0
            if overtime.real_date_start and overtime.real_date_end:
                dt_start = fields.Datetime.from_string(overtime.real_date_start)
                dt_end = fields.Datetime.from_string(overtime.real_date_end)
                overtime.real_overtime_hour = (
                    dt_end - dt_start
                ).total_seconds() / 3600.00

    @api.multi
    @api.depends("date_start", "date_end")
    def _compute_hour(self):
        for ovt in self:
            ovt_hour = 0.0
            dt_start = dt_end = False
            if ovt.date_start:
                dt_start = fields.Datetime.from_string(ovt.date_start)
            if ovt.date_end:
                dt_end = fields.Datetime.from_string(ovt.date_end)
            if dt_start and dt_end:
                ovt_hour = (dt_end - dt_start).total_seconds() / 3600.00
            ovt.overtime_hour = ovt_hour

    @api.multi
    @api.depends(
        "company_id",
    )
    def _compute_policy(self):
        _super = super(HrOvertimeRequest, self)
        _super._compute_policy()

    name = fields.Char(
        string="# Overtime Request",
        required=True,
        default="/",
        readonly=True,
        copy=False,
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
        readonly=False,
    )
    employee_id = fields.Many2one(
        string="Employee",
        comodel_name="hr.employee",
        required=True,
        readonly=True,
        default=_default_employee_id,
        track_visibility="onchange",
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    department_id = fields.Many2one(
        string="Department",
        comodel_name="hr.department",
        readonly=False,
        copy=False,
        track_visibility="onchange",
    )
    manager_id = fields.Many2one(
        string="Manager",
        comodel_name="hr.employee",
        readonly=False,
        copy=False,
        track_visibility="onchange",
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
        track_visibility="onchange",
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
        track_visibility="onchange",
    )
    real_date_start = fields.Datetime(
        string="Real Date Start",
        readonly=True,
        compute="_compute_real_start",
        store=True,
    )
    real_date_end = fields.Datetime(
        string="Real Date End",
        readonly=True,
        compute="_compute_real_end",
        store=True,
    )
    overtime_hour = fields.Float(
        string="Overtime Hour",
        compute="_compute_hour",
        store=True,
    )
    real_overtime_hour = fields.Float(
        string="Real Overtime Hour",
        compute="_compute_real",
        store=True,
    )
    note = fields.Text(
        string="Note",
    )
    attendance_ids = fields.One2many(
        string="Attendances",
        comodel_name="hr.attendance",
        inverse_name="overtime_id",
        readonly=True,
    )
    start_attendance_id = fields.Many2one(
        string="Start Attendance",
        comodel_name="hr.attendance",
        compute="_compute_attendance",
        store=True,
        readonly=True,
    )
    end_attendance_id = fields.Many2one(
        string="End Attendance",
        comodel_name="hr.attendance",
        compute="_compute_attendance",
        store=True,
        readonly=True,
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
    confirm_ok = fields.Boolean(
        string="Can Confirm",
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
    restart_validation_ok = fields.Boolean(
        string="Can Restart Validation",
        compute="_compute_policy",
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

    @api.multi
    def validate_tier(self):
        _super = super(HrOvertimeRequest, self)
        _super.validate_tier()
        for document in self:
            if document.validated:
                document.action_valid()

    @api.multi
    def restart_validation(self):
        _super = super(HrOvertimeRequest, self)
        _super.restart_validation()
        for document in self:
            document.request_validation()

    @api.multi
    def action_confirm(self):
        for overtime in self:
            overtime.write(overtime._prepare_confirm_data())
            overtime.request_validation()

    @api.multi
    def action_valid(self):
        for overtime in self:
            overtime.write(overtime._prepare_valid_data())

    @api.multi
    def action_cancel(self):
        for overtime in self:
            overtime.write(overtime._prepare_cancel_data())
            overtime.restart_validation()

    @api.multi
    def action_restart(self):
        for overtime in self:
            overtime.write(overtime._prepare_restart_data())

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
            "definition_id": False,
            "reviewer_partner_ids": False,
            "review_ids": False,
        }
        return result

    @api.model
    def create(self, values):
        _super = super(HrOvertimeRequest, self)
        result = _super.create(values)
        sequence = result._create_sequence()
        result.write(
            {
                "name": sequence,
            }
        )
        return result

    @api.multi
    def copy(self, default):
        self.ensure_one()
        _super = super(HrOvertimeRequest, self)
        default.update(
            {
                "department_id": self._get_department_id().id,
                "manager_id": self._get_manager_id().id,
            }
        )
        return _super.copy(default)

    @api.multi
    def unlink(self):
        _super = super(HrOvertimeRequest, self)
        force_unlink = self._context.get("force_unlink", False)
        for report in self:
            if report.state != "draft" and not force_unlink:
                raise UserError(_("You can only delete data with draft state"))
        _super.unlink()

    @api.constrains("date_start", "date_end")
    def _check_duration(self):
        strWarning = _("Date end must be greater than date start")
        if self.date_start and self.date_end:
            if self.date_end < self.date_start:
                raise UserError(strWarning)

    @api.constrains("employee_id", "state", "date_start", "date_end")
    def _check_availability(self):
        obj_overtime = self.env[self._name]
        if self.state in ["confirm", "valid"]:
            criteria = [
                ("employee_id", "=", self.employee_id.id),
                ("id", "<>", self.id),
                ("state", "=", "valid"),
                ("date_start", "<=", self.date_end),
                ("date_end", ">=", self.date_start),
            ]
            if obj_overtime.search_count(criteria) > 0:
                raise UserError(_("Employe already has an overtime request"))

    @api.multi
    def _get_department_id(self):
        self.ensure_one()
        department_id = False
        if self.employee_id:
            department_id = self.employee_id.department_id
        return department_id

    @api.multi
    def _get_manager_id(self):
        self.ensure_one()
        manager_id = False
        if self.employee_id:
            manager_id = self.employee_id.parent_id
        return manager_id

    @api.onchange("employee_id")
    def onchange_department_id(self):
        self.department_id = self._get_department_id()

    @api.onchange("employee_id")
    def onchange_manager_id(self):
        self.manager_id = self._get_manager_id()
