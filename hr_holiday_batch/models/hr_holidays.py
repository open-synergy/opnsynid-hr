# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrHolidays(models.Model):
    _inherit = "hr.holidays"

    leave_batch_id = fields.Many2one(
        string="Leave Request Batch",
        comodel_name="hr.holiday_batch_leave_request",
        readonly=True,
        states={
            'draft': [('readonly', False)]
        },
        copy=False,
        ondelete='restrict'
    )
    allocation_batch_id = fields.Many2one(
        string="Allocation Request Batch",
        comodel_name="hr.holiday_batch_allocation_request",
        readonly=True,
        states={
            'draft': [('readonly', False)]
        },
        copy=False,
        ondelete='restrict'
    )
