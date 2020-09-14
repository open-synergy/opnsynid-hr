# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ResCompany(models.Model):
    _inherit = "res.company"

    start_overtime_buffer = fields.Float(
        string="Start Overtime Buffer",
        default=0.0,
        required=True,
    )
    end_overtime_buffer = fields.Float(
        string="End Overtime Buffer",
        default=0.0,
        required=True,
    )
    overtime_request_sequence_id = fields.Many2one(
        string="Overtime Request Sequence",
        comodel_name="ir.sequence",
    )
    overtime_request_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Overtime Request",
        comodel_name="res.groups",
        relation="rel_overtime_request_allowed_confirm_groups",
        column1="company_id",
        column2="group_id",
    )
    overtime_request_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel Overtime Request",
        comodel_name="res.groups",
        relation="rel_overtime_request_allowed_cancel_groups",
        column1="company_id",
        column2="group_id",
    )
    overtime_request_restart_grp_ids = fields.Many2many(
        string="Allowed To Restart Overtime Request",
        comodel_name="res.groups",
        relation="rel_overtime_request_allowed_restart_groups",
        column1="company_id",
        column2="group_id",
    )
    overtime_request_restart_validation_grp_ids = fields.Many2many(
        string="Allowed To Restart Validation Overtime Request",
        comodel_name="res.groups",
        relation="rel_overtime_request_allowed_restart_val_groups",
        column1="company_id",
        column2="group_id",
    )
