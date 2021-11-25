# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class HrDepartment(models.Model):
    _inherit = "hr.department"

    holiday_allocation_confirm_group_ids = fields.Many2many(
        string="Allowed to Confirm Holiday Allocation",
        comodel_name="res.groups",
        relation="rel_department_confirm_holiday_allocation",
        column1="department_id",
        column2="group_id",
    )

    holiday_allocation_approve_group_ids = fields.Many2many(
        string="Allowed to Approve Holiday Allocation",
        comodel_name="res.groups",
        relation="rel_department_approve_holiday_allocation",
        column1="department_id",
        column2="group_id",
    )

    holiday_allocation_refuse_group_ids = fields.Many2many(
        string="Allowed to Refuse Holiday Allocation",
        comodel_name="res.groups",
        relation="rel_department_refuse_holiday_allocation",
        column1="department_id",
        column2="group_id",
    )

    holiday_allocation_restart_group_ids = fields.Many2many(
        string="Allowed to Restart Holiday Allocation",
        comodel_name="res.groups",
        relation="rel_department_restart_holiday_allocation",
        column1="department_id",
        column2="group_id",
    )

    holiday_allocation_validate_group_ids = fields.Many2many(
        string="Allowed to Validate Holiday Allocation",
        comodel_name="res.groups",
        relation="rel_department_validate_holiday_allocation",
        column1="department_id",
        column2="group_id",
    )

    holiday_request_confirm_group_ids = fields.Many2many(
        string="Allowed to Confirm Holiday Request",
        comodel_name="res.groups",
        relation="rel_department_confirm_holiday_request",
        column1="department_id",
        column2="group_id",
    )

    holiday_request_approve_group_ids = fields.Many2many(
        string="Allowed to Approve Holiday Request",
        comodel_name="res.groups",
        relation="rel_department_confirm_holiday_request",
        column1="department_id",
        column2="group_id",
    )

    holiday_request_refuse_group_ids = fields.Many2many(
        string="Allowed to Refuse Holiday Request",
        comodel_name="res.groups",
        relation="rel_department_refuse_holiday_request",
        column1="department_id",
        column2="group_id",
    )

    holiday_request_restart_group_ids = fields.Many2many(
        string="Allowed to Restart Holiday Request",
        comodel_name="res.groups",
        relation="rel_department_restart_holiday_request",
        column1="department_id",
        column2="group_id",
    )

    holiday_request_validate_group_ids = fields.Many2many(
        string="Allowed to Validate Holiday Request",
        comodel_name="res.groups",
        relation="rel_department_validate_holiday_request",
        column1="department_id",
        column2="group_id",
    )

    @api.multi
    def _get_holiday_button_policy(self, policy_field):
        self.ensure_one()
        result = False
        button_group_ids = []
        user = self.env.user
        group_ids = user.groups_id.ids

        button_group_ids += getattr(self, policy_field).ids

        if not button_group_ids:
            result = True
        else:
            if set(button_group_ids) & set(group_ids):
                result = True
        return result

    @api.multi
    def _get_holiday_button_policy_map(self, holiday_type):
        self.ensure_one()
        if holiday_type == "add":
            result = [
                ("confirm_ok", "holiday_allocation_confirm_group_ids"),
                ("approve_ok", "holiday_allocation_approve_group_ids"),
                ("refuse_ok", "holiday_allocation_refuse_group_ids"),
                ("restart_ok", "holiday_allocation_restart_group_ids"),
                ("validate_ok", "holiday_allocation_validate_group_ids"),
            ]
        else:
            result = [
                ("confirm_ok", "holiday_request_confirm_group_ids"),
                ("approve_ok", "holiday_request_approve_group_ids"),
                ("refuse_ok", "holiday_request_refuse_group_ids"),
                ("restart_ok", "holiday_request_restart_group_ids"),
                ("validate_ok", "holiday_request_validate_group_ids"),
            ]
        return result
