# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError


class HrAnalyticTimesheet(models.Model):
    _name = "hr.analytic.timesheet"
    _inherit = "hr.analytic.timesheet"

    accrue_income_journal_id = fields.Many2one(
        string="Accrue Income Journal",
        comodel_name="account.journal",
        domain=[
            ("type", "=", "general"),
        ],
    )
    accrue_income_account_id = fields.Many2one(
        string="Accrue Income Account",
        comodel_name="account.account",
        domain=[
            ("type", "=", "other"),
        ],
    )
    income_account_id = fields.Many2one(
        string="Income Account",
        comodel_name="account.account",
        domain=[
            ("type", "=", "other"),
        ],
    )
    accrue_income_ok = fields.Boolean(
        string="Can Create Accrue Income",
        default=False,
    )
    accrue_income_move_id = fields.Many2one(
        string="Accrue Income Move",
        comodel_name="account.move",
        readonly=True,
        ondelete="restrict",
    )

    @api.onchange(
        "user_id",
        "account_id",
    )
    def onchange_accrue_income_journal_id(self):
        journal = False
        if (
            self.user_id
            and len(self.user_id.employee_ids) > 0
            and self.user_id.employee_ids[0].accrue_income_journal_id
        ):
            journal = self.user_id.employee_ids[0].accrue_income_journal_id

        if not journal and self.account_id and self.account_id.accrue_income_journal_id:
            journal = self.account_id.accrue_income_journal_id

        self.accrue_income_journal_id = journal

    @api.onchange(
        "user_id",
        "account_id",
    )
    def onchange_accrue_income_account_id(self):
        account = False
        if (
            self.user_id
            and len(self.user_id.employee_ids) > 0
            and self.user_id.employee_ids[0].accrue_income_account_id
        ):
            account = self.user_id.employee_ids[0].accrue_income_account_id

        if not account and self.account_id and self.account_id.accrue_income_account_id:
            account = self.account_id.accrue_income_account_id

        self.accrue_income_account_id = account

    @api.onchange(
        "account_id",
        "product_id",
    )
    def onchange_income_account_id(self):
        account = False
        if not account and self.account_id and self.account_id.accrue_income_account_id:
            account = self.account_id.income_account_id

        if not account:
            account = self.product_id.property_account_income

        if not account:
            account = self.product_id.categ_id.property_account_income_categ

        self.income_account_id = account

    @api.onchange(
        "account_id",
    )
    def onchange_accrue_income_ok(self):
        result = False

        if self.account_id:
            result = self.account_id.accrue_income_ok

        self.accrue_income_ok = result

    @api.multi
    def action_create_accrue_income_move(self):
        for document in self:
            document._create_accrue_income_move()

    @api.multi
    def action_unlink_accrue_income_move(self):
        for document in self:
            document._unlink_accrue_income_move()

    @api.multi
    def _unlink_accrue_income_move(self):
        self.ensure_one()
        move = self.accrue_income_move_id
        self.write(
            {
                "accrue_income_move_id": False,
            }
        )
        move.unlink()

    @api.multi
    def _create_accrue_income_move(self):
        self.ensure_one()
        obj_move = self.env["account.move"]
        move = obj_move.create(self._prepare_accrue_income_move())
        self.write(
            {
                "accrue_income_move_id": move.id,
            }
        )

    @api.multi
    def _get_accrue_income_journal(self):
        self.ensure_one()
        if not self.accrue_income_journal_id:
            err_msg = _("No accrue income journal defined")
            raise UserError(err_msg)
        return self.accrue_income_journal_id

    @api.multi
    def _get_accrue_income_account(self):
        self.ensure_one()
        if not self.accrue_income_account_id:
            err_msg = _("No accrue income account defined")
            raise UserError(err_msg)
        return self.accrue_income_account_id

    @api.multi
    def _get_income_account(self):
        self.ensure_one()
        result = self.income_account_id
        if not result:
            err_msg = _("No income account defined")
            raise UserError(err_msg)
        return result

    @api.multi
    def _get_accrue_income_period(self):
        self.ensure_one()
        period = self.env["account.period"].find(self.date)
        return period

    @api.multi
    def _prepare_accrue_income_move(self):
        self.ensure_one()
        journal = self._get_accrue_income_journal()
        period = self._get_accrue_income_period()
        return {
            "journal_id": journal.id,
            "period_id": period.id,
            "date": self.date,
            "line_id": self._prepare_accrue_income_move_lines(),
        }

    @api.multi
    def _prepare_accrue_income_move_lines(self):
        self.ensure_one()
        result = []
        result.append(self._prepare_accrue_income_line())
        result.append(self._prepare_income_line())
        return result

    @api.multi
    def _get_accrue_income_partner(self):
        self.ensure_one()
        partner = self.account_id.partner_id
        if not partner:
            err_msg = _("No customer defined")
            raise UserError(err_msg)
        return partner

    @api.multi
    def _prepare_accrue_income_line(self):
        self.ensure_one()
        amount = self.unit_amount * self.account_id.prepaid_price_unit
        return (
            0,
            0,
            {
                "account_id": self._get_accrue_income_account().id,
                "analytic_account_id": self.account_id.id,
                "credit": 0.0,
                "debit": amount,
                "partner_id": self._get_accrue_income_partner().id,
                "name": self.name,
                "product_id": self.product_id.id,
                "product_uom_id": self.product_uom_id.id,
                "quantity": self.unit_amount,
            },
        )

    @api.multi
    def _prepare_income_line(self):
        self.ensure_one()
        amount = self.unit_amount * self.account_id.prepaid_price_unit
        return (
            0,
            0,
            {
                "account_id": self._get_income_account().id,
                "analytic_account_id": self.account_id.id,
                "debit": 0.0,
                "credit": amount,
                "partner_id": self._get_accrue_income_partner().id,
                "name": self.name,
                "product_id": self.product_id.id,
                "product_uom_id": self.product_uom_id.id,
                "quantity": self.unit_amount,
            },
        )
