# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models, _
from openerp.exceptions import Warning as UserError


class HrHolidays(models.Model):
    _inherit = "hr.holidays"

    holiday_code = fields.Char(
        string="# Document",
        required=True,
        default="/"
    )

    @api.multi
    def _get_holidays_sequence_by_type(self, default_type):
        self.ensure_one()
        lvr_sequence_id = False
        alr_sequence_id = False

        status_id =\
            self.holiday_status_id
        if status_id:
            lvr_sequence_id =\
                status_id.leave_request_sequence_id
            alr_sequence_id =\
                status_id.allocation_request_sequence_id

        if lvr_sequence_id and default_type == "remove":
            result = self.env["ir.sequence"].\
                next_by_id(lvr_sequence_id.id)
        elif alr_sequence_id and default_type == "add":
            result = self.env["ir.sequence"].\
                next_by_id(alr_sequence_id.id)
        else:
            result = False
        return result

    @api.multi
    def _get_holidays_sequence_by_company(self, default_type):
        self.ensure_one()
        obj_res_company =\
            self.env["res.company"]

        company_id =\
            self.env.user.company_id.id

        lvr_sequence_id = False
        alr_sequence_id = False

        company = obj_res_company.browse([company_id])[0]
        if company:
            lvr_sequence_id =\
                company.leave_request_sequence_id
            alr_sequence_id =\
                company.allocation_request_sequence_id

        if lvr_sequence_id and default_type == "remove":
            result = self.env["ir.sequence"].\
                next_by_id(lvr_sequence_id.id)
        elif alr_sequence_id and default_type == "add":
            result = self.env["ir.sequence"].\
                next_by_id(alr_sequence_id.id)
        else:
            result = False
        return result

    @api.multi
    def _get_holidays_sequence_by_default(self, default_type):
        self.ensure_one()

        if default_type == "remove":
            result =\
                self.env["ir.sequence"].next_by_code("hr.holidays.lvr")
        elif default_type == "add":
            result =\
                self.env["ir.sequence"].next_by_code("hr.holidays.alr")
        else:
            result = False
        return result

    @api.multi
    def _get_holidays_sequence(self):
        self.ensure_one()
        context = self._context

        default_type =\
            context.get("default_type", False)

        if default_type:
            by_type =\
                self._get_holidays_sequence_by_type(default_type)
            by_default =\
                self._get_holidays_sequence_by_default(default_type)
            by_company =\
                self._get_holidays_sequence_by_company(default_type)
            if by_type:
                result = by_type
            elif by_company:
                result = by_company
            elif by_default:
                result = by_default
            else:
                result = False
        else:
            result = False
        return result

    @api.multi
    def _prepare_create_data(self):
        self.ensure_one()
        result = {}
        sequence =\
            self._get_holidays_sequence()
        if sequence:
            result.update({"holiday_code": sequence})
        else:
            raise UserError(_("Sequence Is Not Valid"))
        return result

    @api.model
    def create(self, values):
        _super = super(HrHolidays, self)
        result = _super.create(values)
        result.write(result._prepare_create_data())
        return result

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            result.append((record["id"], record.holiday_code))
        return result
