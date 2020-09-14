# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ResConfig(models.TransientModel):
    _name = "hr.overtime_config_setting"
    _inherit = "res.config.settings"

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id.id

    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        required=True,
        default=lambda self: self._default_company_id(),
    )
    start_overtime_buffer = fields.Float(
        string="Start Overtime Buffer",
        related="company_id.start_overtime_buffer",
    )
    end_overtime_buffer = fields.Float(
        string="End Overtime Buffer",
        related="company_id.end_overtime_buffer",
    )
    overtime_request_sequence_id = fields.Many2one(
        string="Sequence Overtime Request",
        comodel_name="ir.sequence",
        related="company_id.overtime_request_sequence_id",
    )
    overtime_request_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Overtime Request",
        comodel_name="res.groups",
        related="company_id.overtime_request_confirm_grp_ids",
        store=False,
    )
    overtime_request_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel Overtime Request",
        comodel_name="res.groups",
        related="company_id.overtime_request_cancel_grp_ids",
        store=False,
    )
    overtime_request_restart_grp_ids = fields.Many2many(
        string="Allowed To Restart Overtime Request",
        comodel_name="res.groups",
        related="company_id.overtime_request_restart_grp_ids",
        store=False,
    )
    overtime_request_restart_validation_grp_ids = fields.Many2many(
        string="Allowed To Restart Validation Overtime Request",
        comodel_name="res.groups",
        related="company_id.overtime_request_restart_validation_grp_ids",
        store=False,
    )
