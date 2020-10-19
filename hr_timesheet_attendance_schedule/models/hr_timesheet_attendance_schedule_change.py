# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api, _
from openerp.exceptions import Warning as UserError


class HrTimesheetAttendanceScheduleChange(models.Model):
    _name = "hr.timesheet_attendance_schedule_change"
    _description = "Attendance Schedule Change Request"
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
        return self.env.user.company_id

    @api.multi
    @api.depends(
        "company_id",
    )
    def _compute_policy(self):
        _super = super(HrTimesheetAttendanceScheduleChange, self)
        _super._compute_policy()

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
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        required=True,
        default=lambda self: self._default_company_id(),
        ondelete="restrict",
    )
    employee_id = fields.Many2one(
        string="Employee",
        comodel_name="hr.employee",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        ondelete="restrict",
    )
    sheet_id = fields.Many2one(
        string="Timesheet",
        comodel_name="hr_timesheet_sheet.sheet",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        ondelete="restrict",
    )
    schedule_id = fields.Many2one(
        string="Schedule",
        comodel_name="hr.timesheet_attendance_schedule",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
        ondelete="restrict",
    )
    old_date_start = fields.Datetime(
        string="Old Date Start",
        readonly=True,
    )
    old_date_end = fields.Datetime(
        string="Old Date End",
        readonly=True,
    )
    new_date_start = fields.Datetime(
        string="New Date Start",
        required=True,
    )
    new_date_end = fields.Datetime(
        string="New Date End",
        required=True,
    )
    state = fields.Selection(
        string="State",
        copy=False,
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("valid", "Valid"),
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
    valid_date = fields.Datetime(
        string="Validated Date",
        readonly=True,
        copy=False,
    )
    valid_user_id = fields.Many2one(
        string="Validated By",
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
    cancel_ok = fields.Boolean(
        string="Can Cancel",
        compute="_compute_policy",
    )
    restart_ok = fields.Boolean(
        string="Can Restart",
        compute="_compute_policy",
    )
    restart_approval_ok = fields.Boolean(
        string="Can Restart Approval",
        compute="_compute_policy",
        store=False,
    )

    @api.model
    def create(self, values):
        _super = super(HrTimesheetAttendanceScheduleChange, self)
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
        _super = super(HrTimesheetAttendanceScheduleChange, self)
        _super.unlink()

    @api.multi
    def validate_tier(self):
        _super = super(HrTimesheetAttendanceScheduleChange, self)
        _super.validate_tier()
        for document in self:
            if document.validated:
                document.button_approve()

    @api.multi
    def restart_validation(self):
        _super = super(HrTimesheetAttendanceScheduleChange, self)
        _super.restart_validation()
        for document in self:
            document.request_validation()

    @api.multi
    def button_confirm(self):
        for document in self:
            document.write(document._prepare_confirm_data())
            document.request_validation()

    @api.multi
    def button_approve(self):
        for document in self:
            document.write(document._prepare_approve_data())
            document.schedule_id.write(
                document._prepare_schedule_change()
            )

    @api.multi
    def button_cancel(self):
        for document in self:
            document.write(document._prepare_cancel_data())
            document.restart_validation()

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
            "state": "valid",
            "valid_date": fields.Datetime.now(),
            "valid_user_id": self.env.user.id,
        }
        return result

    @api.multi
    def _prepare_schedule_change(self):
        self.ensure_one()
        return {
            "date_start": self.new_date_start,
            "date_end": self.new_date_end,
        }

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
    def _prepare_restart_data(self):
        self.ensure_one()
        result = {
            "state": "draft",
            "confirm_date": False,
            "confirm_user_id": False,
            "approve_date": False,
            "approve_user_id": False,
            "valid_date": False,
            "valid_user_id": False,
        }
        return result

    @api.onchange("employee_id")
    def onchange_sheet_id(self):
        self.sheet_id = False

    @api.onchange("sheet_id")
    def onchange_schedule_id(self):
        self.schedule_id = False

    @api.onchange("schedule_id")
    def onchange_old_date_start(self):
        self.old_date_start = False
        if self.schedule_id:
            self.old_date_start = self.schedule_id.date_start

    @api.onchange("schedule_id")
    def onchange_old_date_end(self):
        self.old_date_end = False
        if self.schedule_id:
            self.old_date_end = self.schedule_id.date_end
