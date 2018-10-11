# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api, SUPERUSER_ID
from openerp.exceptions import Warning as UserError
from datetime import datetime
from openerp.tools.translate import _


class HrHolidayBatchLeaveRequest(models.Model):
    _name = "hr.holiday_batch_leave_request"
    _inherit = "hr.holiday_batch_common"
    _description = "Leave Request Batches"

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
                    batch.refuse_ok = \
                    batch.generate_ok = \
                    batch.restart_ok = True
                continue

            if batch.company_id:
                company = batch.company_id
                for policy in company.\
                        _get_leave_batch_button_policy_map():
                    setattr(
                        batch,
                        policy[0],
                        company.
                        _get_holiday_batch_button_policy(
                            policy[1]),
                    )

    name = fields.Char(
        string="Name",
        required=True,
        readonly=True,
        states={
            'draft': [('readonly', False)]
        },
        default="/",
    )

    date_start = fields.Datetime(
        string="Date Start",
        required=True,
        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        states={
            'draft': [('readonly', False)]
        }
    )
    date_end = fields.Datetime(
        string="Date End",
        required=True,
        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        states={
            'draft': [('readonly', False)]
        }
    )
    request_ids = fields.One2many(
        string="Request(s)",
        comodel_name="hr.holidays",
        inverse_name="leave_batch_id",
        required=False,
        readonly=True,
        states={
            'draft': [('readonly', False)]
        }
    )

    @api.multi
    def action_confirm(self):
        res =\
            super(HrHolidayBatchLeaveRequest, self).\
            action_confirm()
        for holiday in self:
            holiday.request_ids.holidays_confirm()
        return res

    @api.multi
    def action_valid(self):
        res =\
            super(HrHolidayBatchLeaveRequest, self).\
            action_valid()
        for holiday in self:
            holiday.request_ids.holidays_validate()
        return res

    @api.multi
    def action_refuse(self):
        res =\
            super(HrHolidayBatchLeaveRequest, self).\
            action_refuse()
        for holiday in self:
            holiday.request_ids.holidays_refuse()
        return res

    @api.multi
    def action_cancel(self):
        res =\
            super(HrHolidayBatchLeaveRequest, self).\
            action_cancel()
        for holiday in self:
            holiday.request_ids.holidays_refuse()
        return res

    @api.multi
    def action_restart(self):
        res =\
            super(HrHolidayBatchLeaveRequest, self).\
            action_restart()
        for holiday in self:
            holiday.request_ids.holidays_reset()
        return res

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

        if company.leave_request_batch_sequence_id:
            result = company.leave_request_batch_sequence_id
        else:
            result = self.env.ref(
                "hr_holiday_batch.sequence_batch_leave_request")
        return result

    @api.model
    def _create_sequence(self, company_id):
        name = self.env["ir.sequence"].\
            next_by_id(self._get_sequence(company_id).id) or "/"
        return name

    @api.model
    def create(self, values):
        new_values = self._prepare_create_data(values)
        return super(HrHolidayBatchLeaveRequest, self).create(new_values)

    @api.constrains(
        "date_start", "date_end")
    def _check_date(self):
        strWarning = _(
            "Date start must be greater than date end")
        if self.date_start and self.date_end:
            if self.date_start > self.date_end:
                raise UserError(_("%s") % (strWarning))
