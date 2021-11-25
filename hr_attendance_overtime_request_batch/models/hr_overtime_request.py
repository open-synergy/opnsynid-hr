# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class HrOvertimeRequest(models.Model):
    _inherit = "hr.overtime_request"

    request_batch_id = fields.Many2one(
        string="Request Batch",
        comodel_name="hr.overtime_request_batch",
        readonly=True,
        states={"draft": [("readonly", False)]},
        copy=False,
        ondelete="restrict",
    )
