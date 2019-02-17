# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class AccountJournal(models.Model):
    _inherit = "account.journal"

    expense_confirm_grp_ids = fields.Many2many(
        string="Allowed to Confirm",
        comodel_name="res.groups",
        relation="rel_journal_2_expense_confirm_groups",
        column1="journal_id",
        column2="group_id",
    )
    expense_validate_grp_ids = fields.Many2many(
        string="Allowed to Approve",
        comodel_name="res.groups",
        relation="rel_journal_2_expense_validate_groups",
        column1="journal_id",
        column2="group_id",
    )
    expense_refuse_grp_ids = fields.Many2many(
        string="Allowed to Refuse",
        comodel_name="res.groups",
        relation="rel_journal_2_expense_refuse_groups",
        column1="journal_id",
        column2="group_id",
    )
    expense_done_grp_ids = fields.Many2many(
        string="Allowed to Generate Accounting Entry",
        comodel_name="res.groups",
        relation="rel_journal_2_expense_accept_groups",
        column1="journal_id",
        column2="group_id",
    )
    expense_restart_grp_ids = fields.Many2many(
        string="Allowed to Restart",
        comodel_name="res.groups",
        relation="rel_journal_2_expense_restart_groups",
        column1="journal_id",
        column2="group_id",
    )
    expense_view_grp_ids = fields.Many2many(
        string="Allowed to View Accounting Entries",
        comodel_name="res.groups",
        relation="rel_journal_2_expense_view_groups",
        column1="journal_id",
        column2="group_id",
    )
