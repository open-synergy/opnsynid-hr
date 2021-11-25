# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging
from datetime import datetime

from dateutil.relativedelta import relativedelta
from openerp import api, fields, models

_logger = logging.getLogger(__name__)


class ManualGoalCreation(models.TransientModel):
    _name = "gamification.manual_goal_creation"
    _description = "Manual Goal Creation"

    @api.model
    def _default_challange_id(self):
        challange_id = self._context.get("active_id", False)
        return challange_id

    @api.model
    def _default_period(self):
        challange_id = self._default_challange_id()
        obj_challange = self.env["gamification.challenge"]
        challange = obj_challange.browse([challange_id])[0]
        return challange.period

    user_ids = fields.Many2many(
        string="Users",
        comodel_name="res.users",
        relation="rel_manual_goal_creation_2_user",
        column1="wizard_id",
        column2="user_id",
    )
    challange_id = fields.Many2one(
        string="Challange",
        comodel_name="gamification.challenge",
        required=True,
        default=lambda self: self._default_challange_id(),
    )
    period = fields.Selection(
        string="Periodicity",
        selection=[
            ("once", "Non recurring"),
            ("daily", "Daily"),
            ("weekly", "Weekly"),
            ("monthly", "Monthly"),
            ("yearly", "Yearly"),
        ],
        required=True,
        default=lambda self: self._default_period(),
    )
    date_start = fields.Date(
        string="Date Start",
        required=True,
    )
    date_end = fields.Date(
        string="Date End",
    )

    @api.multi
    def action_confirm(self):
        for wiz in self:
            wiz._confirm()

    @api.multi
    def _confirm(self):
        self.ensure_one()
        for line in self.challange_id.line_ids:
            for user in self.user_ids:
                self._batch_create_goal(user, line)

    @api.multi
    def _batch_create_goal(self, user, line):
        self.ensure_one()
        date_start = datetime.strptime(self.date_start, "%Y-%m-%d")
        date_end = False
        if self.date_end:
            date_end = datetime.strptime(self.date_end, "%Y-%m-%d")

        if not self.date_end:
            self._create_goal(user, line, self.date_start, False)
            return True

        if self.period == "daily":
            step = relativedelta(days=1)
        elif self.period == "weekly":
            step = relativedelta(weeks=1)
        elif self.period == "monthly":
            step = relativedelta(months=1)
        elif self.period == "yearly":
            step = relativedelta(years=1)

        while date_start <= date_end:
            date_stop = date_start + step + relativedelta(days=-1)
            str_date_start = date_start.strftime("%Y-%m-%d")
            str_date_end = date_stop.strftime("%Y-%m-%d")
            if self._check_goal(user, line, str_date_start, str_date_end):
                self._create_goal(user, line, str_date_start, str_date_end)
                _logger.info(str_date_start)

            date_start += step

    @api.multi
    def _create_goal(self, user, line, start_date, end_date):
        self.ensure_one()
        obj_goal = self.env["gamification.goal"]
        goal = obj_goal.create(self._prepare_goal(user, line, start_date, end_date))
        goal.update()

    @api.multi
    def _prepare_goal(self, user, line, start_date, end_date):
        challenge = self.challange_id
        return {
            "definition_id": line.definition_id.id,
            "line_id": line.id,
            "target_goal": line.target_goal,
            "state": "inprogress",
            "start_date": start_date,
            "end_date": end_date,
            "current": 0.0,
            "remind_update_delay": challenge.remind_update_delay,
            "user_id": user.id,
        }

    @api.multi
    def _prepare_check_goal_domain(self, user, line, start_date, end_date):
        self.ensure_one()
        domain = [
            ("user_id", "=", user.id),
            ("line_id", "=", line.id),
            "|",
            "&",
            ("start_date", ">=", start_date),
            ("end_date", "=", False),
            "&",
            ("start_date", ">=", start_date),
            ("start_date", "<=", end_date),
        ]
        return domain

    @api.multi
    def _check_goal(self, user, line, start_date, end_date):
        self.ensure_one()
        result = True
        domain = self._prepare_check_goal_domain(user, line, start_date, end_date)
        obj_goal = self.env["gamification.goal"]
        goal_count = obj_goal.search_count(domain)
        if goal_count > 0:
            result = False
        return result
