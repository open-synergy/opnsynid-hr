# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError


class HrAnalyticTimesheet(models.Model):
    _name = "hr.analytic.timesheet"
    _inherit = "hr.analytic.timesheet"

    accrue_expense_journal_id = fields.Many2one(
        string="Accrue Expense Journal",
        comodel_name="account.journal",
        domain=[
            ("type", "=", "general"),
        ],
    )
    accrue_expense_account_id = fields.Many2one(
        string="Accrue Expense Account",
        comodel_name="account.account",
        domain=[
            ("type", "=", "other"),
        ],
    )
    accrue_expense_ok = fields.Boolean(
        string="Can Create Accrue Expense",
        default=False,
    )
    accrue_expense_move_id = fields.Many2one(
        string="Accrue Expense Move",
        comodel_name="account.move",
        readonly=True,
        ondelete="restrict",
    )

    @api.onchange(
        "user_id",
        "account_id",
    )
    def onchange_accrue_expense_journal_id(self):
        journal = False
        if (
            self.user_id
            and len(self.user_id.employee_ids) > 0
            and self.user_id.employee_ids[0].accrue_expense_journal_id
        ):
            journal = self.user_id.employee_ids[0].accrue_expense_journal_id

        if (
            not journal
            and self.account_id
            and self.account_id.accrue_expense_journal_id
        ):
            journal = self.account_id.accrue_expense_journal_id

        self.accrue_expense_journal_id = journal

    @api.onchange(
        "user_id",
        "account_id",
    )
    def onchange_accrue_expense_account_id(self):
        account = False
        if (
            self.user_id
            and len(self.user_id.employee_ids) > 0
            and self.user_id.employee_ids[0].accrue_expense_account_id
        ):
            account = self.user_id.employee_ids[0].accrue_expense_account_id

        if (
            not account
            and self.account_id
            and self.account_id.accrue_expense_account_id
        ):
            account = self.account_id.accrue_expense_account_id

        self.accrue_expense_account_id = account

    @api.onchange(
        "account_id",
    )
    def onchange_accrue_expense_ok(self):
        result = False

        if self.account_id:
            result = self.account_id.accrue_expense_ok

        self.accrue_expense_ok = result

    @api.multi
    def action_create_accrue_expense_move(self):
        for document in self:
            document._create_accrue_expense_move()

    @api.multi
    def action_unlink_accrue_expense_move(self):
        for document in self:
            document._unlink_accrue_expense_move()

    @api.multi
    def _unlink_accrue_expense_move(self):
        self.ensure_one()
        move = self.accrue_expense_move_id
        self.write(
            {
                "accrue_expense_move_id": False,
            }
        )
        move.unlink()

    @api.multi
    def _create_accrue_expense_move(self):
        self.ensure_one()
        obj_move = self.env["account.move"]
        move = obj_move.create(self._prepare_accrue_expense_move())
        self.write(
            {
                "accrue_expense_move_id": move.id,
            }
        )

    @api.multi
    def _get_accrue_expense_journal(self):
        self.ensure_one()
        if not self.accrue_expense_journal_id:
            err_msg = _("No accrue expense journal defined")
            raise UserError(err_msg)
        return self.accrue_expense_journal_id

    @api.multi
    def _get_accrue_expense_account(self):
        self.ensure_one()
        if not self.accrue_expense_account_id:
            err_msg = _("No accrue expense account defined")
            raise UserError(err_msg)
        return self.accrue_expense_account_id

    @api.multi
    def _get_expense_account(self):
        self.ensure_one()
        return self.general_account_id

    @api.multi
    def _get_accrue_expense_period(self):
        self.ensure_one()
        period = self.env["account.period"].find(self.date)
        return period

    @api.multi
    def _prepare_accrue_expense_move(self):
        self.ensure_one()
        journal = self._get_accrue_expense_journal()
        period = self._get_accrue_expense_period()
        return {
            "journal_id": journal.id,
            "period_id": period.id,
            "date": self.date,
            "line_id": self._prepare_accrue_expense_move_lines(),
        }

    @api.multi
    def _prepare_accrue_expense_move_lines(self):
        self.ensure_one()
        result = []
        result.append(self._prepare_accrue_expense_line())
        result.append(self._prepare_expense_line())
        return result

    @api.multi
    def _get_accrue_expense_partner(self):
        self.ensure_one()
        partner = self.user_id.employee_ids[0].address_home_id
        if not partner:
            err_msg = _("No home address defined")
            raise UserError(err_msg)
        return partner

    @api.multi
    def _prepare_accrue_expense_line(self):
        self.ensure_one()
        return (
            0,
            0,
            {
                "account_id": self._get_accrue_expense_account().id,
                "credit": abs(self.amount),
                "debit": 0.0,
                "analytic_account_id": self.account_id.id,
                "partner_id": self._get_accrue_expense_partner().id,
                "name": self.name,
                "product_id": self.product_id.id,
                "product_uom_id": self.product_uom_id.id,
                "quantity": self.unit_amount,
            },
        )

    @api.multi
    def _prepare_expense_line(self):
        self.ensure_one()
        return (
            0,
            0,
            {
                "account_id": self._get_expense_account().id,
                "analytic_account_id": self.account_id.id,
                "debit": abs(self.amount),
                "credit": 0.0,
                "partner_id": self._get_accrue_expense_partner().id,
                "name": self.name,
                "product_id": self.product_id.id,
                "product_uom_id": self.product_uom_id.id,
                "quantity": self.unit_amount,
            },
        )
