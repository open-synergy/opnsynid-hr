# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError


class HrDicipline(models.Model):
    _inherit = "hr.dicipline"

    fine = fields.Boolean(
        string="Fine",
    )
    journal_id = fields.Many2one(
        string="Journal",
        comodel_name="account.journal",
        domain=[
            ("type", "=", "general"),
        ],
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    receivable_account_id = fields.Many2one(
        string="Receivable Account",
        comodel_name="account.account",
        domain=[
            ("type", "in", ["other", "receivable", "payable"]),
            ("reconcile", "=", True),
        ],
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    income_account_id = fields.Many2one(
        string="Income Account",
        comodel_name="account.account",
        domain=[
            ("type", "in", ["other", "receivable", "payable"]),
        ],
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    currency_id = fields.Many2one(
        string="Currency",
        comodel_name="res.currency",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    fine_amount = fields.Float(
        string="Fine Amount",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    fine_move_id = fields.Many2one(
        string="Fine Accounting Entry",
        comodel_name="account.move",
        readonly=True,
    )

    @api.onchange("company_id")
    def onchange_currency_id(self):
        self.currency_id = False
        if self.company_id:
            self.currency_id = self.company_id.currency_id

    @api.multi
    def _get_fine_move_partner(self):
        self.ensure_one()
        result = self.employee_id.address_home_id
        if not result:
            msg = _("No partner defined for employee")
            raise UserError(msg)
        return result

    @api.multi
    def _get_fine_move_journal(self):
        self.ensure_one()
        result = self.journal_id

        if not result:
            result = self.type_id.journal_id

        if not result:
            msg = _("No fine journal defined")
            raise UserError(msg)
        return result

    @api.multi
    def _get_fine_move_income_account(self):
        self.ensure_one()
        result = self.income_account_id

        if not result:
            result = self.type_id.income_account_id

        if not result:
            msg = _("No fine income account defined")
            raise UserError(msg)
        return result

    @api.multi
    def _get_fine_move_receivable_account(self):
        self.ensure_one()
        result = self.receivable_account_id

        if not result:
            result = self.type_id.receivable_account_id

        if not result:
            msg = _("No fine receivable account defined")
            raise UserError(msg)
        return result

    @api.multi
    def _prepare_approve_data(self):
        self.ensure_one()
        _super = super(HrDicipline, self)
        result = _super._prepare_approve_data()
        result.update(
            {
                "fine_move_id": self._create_fine_move().id,
            }
        )
        return result

    @api.multi
    def _create_fine_move(self):
        self.ensure_one()
        obj_move = self.env["account.move"]
        return obj_move.create(self._prepare_fine_move())

    @api.multi
    def _prepare_fine_move(self):
        self.ensure_one()
        obj_period = self.env["account.period"]
        line = []
        line.append(self._prepare_fine_receivable_move_line())
        line.append(self._prepare_fine_income_move_line())
        res = {
            "name": "/",
            "journal_id": self._get_fine_move_journal().id,
            "date": self.effective_date,
            "ref": self.name,
            "period_id": obj_period.find(self.effective_date)[0].id,
            "line_id": line,
        }
        return res

    @api.multi
    def _prepare_fine_move_line(self, name, debit, credit, account_id, partner_id):
        self.ensure_one()
        res = {
            "name": name,
            "account_id": account_id,
            "debit": debit,
            "credit": credit,
            "partner_id": partner_id,
        }
        return (0, 0, res)

    @api.multi
    def _prepare_fine_receivable_move_line(self):
        self.ensure_one()
        name = _("Receivable for employee dicipline fine %s") % (self.name)
        return self._prepare_fine_move_line(
            name=name,
            account_id=self._get_fine_move_receivable_account().id,
            debit=self.fine_amount,
            credit=0.0,
            partner_id=self._get_fine_move_partner().id,
        )

    @api.multi
    def _prepare_fine_income_move_line(self):
        self.ensure_one()
        name = _("Income for employee dicipline fine %s") % (self.name)
        return self._prepare_fine_move_line(
            name=name,
            account_id=self._get_fine_move_income_account().id,
            debit=0.0,
            credit=self.fine_amount,
            partner_id=self._get_fine_move_partner().id,
        )
