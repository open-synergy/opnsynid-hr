# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models, tools


class GamificationGoalAnalysis(models.Model):
    _name = "gamification.goal_analysis"
    _description = "Gamification Goal Analysis"
    _auto = False

    definition_id = fields.Many2one(
        string="Goal Definition",
        comodel_name="gamification.goal.definition",
    )
    user_id = fields.Many2one(
        string="User",
        comodel_name="res.users",
    )
    line_id = fields.Many2one(
        string="Challenge Line",
        comodel_name="gamification.challenge.line",
    )
    challenge_id = fields.Many2one(
        string="Challenge",
        comodel_name="gamification.challenge",
    )
    start_date = fields.Date(
        string="Start Date",
    )
    end_date = fields.Date(
        string="End Date",
    )
    target_goal = fields.Float(
        string="To Reach",
    )
    current = fields.Float(
        string="Current Value",
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("inprogress", "In progress"),
            ("reached", "Reached"),
            ("failed", "Failed"),
            ("canceled", "Canceled"),
        ],
    )

    def _select(self):
        select_str = """
        SELECT
            a.id AS id,
            a.definition_id AS definition_id,
            a.user_id AS user_id,
            a.line_id AS line_id,
            a.start_date AS start_date,
            a.end_date AS end_date,
            a.state AS state,
            a.challenge_id AS challenge_id,
            SUM(a.target_goal) AS target_goal,
            SUM(a.current) AS current
        """
        return select_str

    def _from(self):
        from_str = """
        gamification_goal AS a
        """
        return from_str

    def _where(self):
        where_str = """
        WHERE 1 = 1
        """
        return where_str

    def _join(self):
        join_str = """
        JOIN gamification_challenge_line AS b ON a.line_id = b.id
        """
        return join_str

    def _group_by(self):
        group_str = """
        GROUP BY
            a.id,
            a.definition_id,
            a.user_id,
            a.line_id,
            a.challenge_id,
            a.start_date,
            a.end_date,
            a.state
        """
        return group_str

    def init(self, cr):
        tools.drop_view_if_exists(cr, self._table)
        # pylint: disable=locally-disabled, sql-injection
        cr.execute(
            """CREATE or REPLACE VIEW %s as (
            %s
            FROM %s
            %s
            %s
            %s
        )"""
            % (
                self._table,
                self._select(),
                self._from(),
                self._join(),
                self._where(),
                self._group_by(),
            )
        )
