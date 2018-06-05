# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api, SUPERUSER_ID
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _


class HrOvertimeRequest(models.Model):
    _name = "hr.overtime_request"
    _description = "Attendance Overtime Request"
    _inherit = ["mail.thread"]

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id.id

    @api.multi
    @api.depends(
        "date_start", "date_end")
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
        "state",
        "company_id",
    )
    def _compute_policy(self):
        for overtime in self:
            if self.env.user.id == SUPERUSER_ID:
                overtime.confirm_ok = overtime.valid_ok = \
                    overtime.cancel_ok = \
                    overtime.restart_ok = True
                continue

            if overtime.company_id:
                company = overtime.company_id
                for policy in company.\
                        _get_overtime_button_policy_map():
                    setattr(
                        overtime,
                        policy[0],
                        company.
                        _get_overtime_button_policy(
                            policy[1]),
                    )

    name = fields.Char(
        string="# Overtime Request",
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
        required=True,
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
    overtime_hour = fields.Float(
        string="Overtime Hour",
        compute="_compute_hour",
        store=True,
    )
    note = fields.Text(
        string="Note",
    )
    state = fields.Selection(
        string="State",
        required=True,
        readonly=True,
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
        for overtime in self:
            overtime.write(self._prepare_confirm_data())

    @api.multi
    def action_valid(self):
        for overtime in self:
            overtime.write(self._prepare_valid_data())

    @api.multi
    def action_cancel(self):
        for overtime in self:
            overtime.write(self._prepare_cancel_data())

    @api.multi
    def action_restart(self):
        for overtime in self:
            overtime.write(self._prepare_restart_data())

    @api.multi
    def _prepare_confirm_data(self):
        self.ensure_one()
        result = {
            "state": "confirm",
        }
        return result

    @api.multi
    def _prepare_valid_data(self):
        self.ensure_one()
        result = {
            "state": "valid",
        }
        return result

    @api.multi
    def _prepare_cancel_data(self):
        self.ensure_one()
        result = {
            "state": "cancel",
        }
        return result

    @api.multi
    def _prepare_restart_data(self):
        self.ensure_one()
        result = {
            "state": "draft",
        }
        return result

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

        if company.overtime_request_sequence_id:
            result = company.overtime_request_sequence_id
        else:
            result = self.env.ref(
                "hr_attendance_overtime_request.sequence_overtime_request")
        return result

    @api.model
    def _create_sequence(self, company_id):
        name = self.env["ir.sequence"].\
            next_by_id(self._get_sequence(company_id).id) or "/"
        return name

    @api.model
    def create(self, values):
        new_values = self._prepare_create_data(values)
        return super(HrOvertimeRequest, self).create(new_values)

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
