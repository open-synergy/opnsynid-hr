# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import datetime

from openerp import api, fields, models


class CreatePaymentOrderFromPayslipBatch(models.TransientModel):
    _name = "hr.create_payment_order_from_payslip_batch"
    _description = "Create Payment Order From Payslip Batch"

    @api.model
    def _default_payslip_batch_id(self):
        return self._context.get("active_id", False)

    @api.model
    def _default_date_prefered(self):
        return "fixed"

    @api.multi
    @api.depends(
        "payslip_batch_id",
    )
    def _compute_allowed_move_line_ids(self):
        obj_payslip = self.env["hr.payslip"]
        obj_line = self.env["account.move.line"]
        for wiz in self:
            result = []
            payslip_criteria = [
                ("payslip_run_id", "=", wiz.payslip_batch_id.id),
            ]
            payslips = obj_payslip.search(payslip_criteria)
            for payslip in payslips:
                if payslip.move_id:
                    line_criteria = [
                        ("move_id", "=", payslip.move_id.id),
                        ("reconcile_id", "=", False),
                        ("account_id.type", "=", "payable"),
                        ("credit", ">", 0.0),
                        ("account_id.reconcile", "=", True),
                    ]
                    lines = obj_line.search(line_criteria)
                    result += lines.ids

            wiz.allowed_move_line_ids = result

    payslip_batch_id = fields.Many2one(
        string="# Payslip Batch",
        comodel_name="hr.payslip.run",
        default=lambda self: self._default_payslip_batch_id(),
    )
    payment_mode_id = fields.Many2one(
        string="Payment Mode",
        comodel_name="payment.mode",
        required=True,
    )
    date_prefered = fields.Selection(
        string="Preferred Date",
        selection=[
            ("now", "Directly"),
            ("due", "Due date"),
            ("fixed", "Fixed date"),
        ],
        default=lambda self: self._default_date_prefered(),
    )
    date_scheduled = fields.Date(
        string="Scheduled Date",
    )
    account_move_line_ids = fields.Many2many(
        string="Account Move Lines",
        comodel_name="account.move.line",
        relation="rel_create_payment_from_batch_2_move",
        column1="wiz_id",
        column2="move_id",
    )
    allowed_move_line_ids = fields.Many2many(
        string="Allowed Move Lines",
        comodel_name="account.move.line",
        compute="_compute_allowed_move_line_ids",
        store=False,
    )

    @api.multi
    def action_confirm(self):
        self.ensure_one()
        self._create_payment_order()

    @api.multi
    def _create_payment_order(self):
        self.ensure_one()
        obj_order = self.env["payment.order"]
        obj_wiz = self.env["payment.order.create"]
        order = obj_order.create(self._prepare_payment_order())
        wiz = obj_wiz.create(self._prepare_create_payment_wizard())
        wiz.with_context(active_id=order.id).create_payment()

    @api.multi
    def _prepare_payment_order(self):
        self.ensure_one()
        return {
            "date_scheduled": self.date_scheduled,
            "mode": self.payment_mode_id.id,
            "user_id": self.env.user.id,
            "date_prefered": self.date_prefered,
        }

    @api.multi
    def _prepare_create_payment_wizard(self):
        self.ensure_one()
        return {
            "duedate": datetime.now().strftime("%Y-%m-%d"),
            "entries": [(6, 0, self.account_move_line_ids.ids)],
        }
