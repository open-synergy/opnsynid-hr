# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models, tools


class HrTimesheetComputationAnalysis(models.Model):
    _name = "hr.timesheet_computation_analysis"
    _description = "Timesheet Computation Analysis"
    _auto = False

    timesheet_id = fields.Many2one(
        string="Timesheet",
        comodel_name="hr_timesheet_sheet.sheet",
    )
    employee_id = fields.Many2one(
        string="Employee",
        comodel_name="hr.employee",
    )
    department_id = fields.Many2one(
        string="Department",
        comodel_name="hr.department",
    )
    parent_id = fields.Many2one(
        string="Manager",
        comodel_name="hr.employee",
    )
    job_id = fields.Many2one(
        string="Job Title",
        comodel_name="hr.job",
    )
    date_start = fields.Date(
        string="Date Start",
    )
    date_end = fields.Date(
        string="Date End",
    )
    item_id = fields.Many2one(
        string="Computation Item",
        comodel_name="hr.timesheet_computation_item",
    )
    timesheet_state = fields.Selection(
        string="Timesheet State",
        selection=[
            ("new", "New"),
            ("draft", "Open"),
            ("confirm", "Waiting Approval"),
            ("done", "Approved"),
        ],
    )
    amount = fields.Float(
        string="Amount",
    )

    def _select(self):
        select_str = """
        SELECT
            a.id AS id,
            b.id AS timesheet_id,
            c.id AS employee_id,
            c.department_id AS department_id,
            c.job_id AS job_id,
            a.item_id AS item_id,
            b.state AS timesheet_state,
            b.date_from AS date_start,
            b.date_to AS date_end,
            c.parent_id AS parent_id,
            SUM(a.amount) AS amount
        """
        return select_str

    def _from(self):
        from_str = """
        hr_timesheet_computation AS a
        """
        return from_str

    def _where(self):
        where_str = """
        WHERE 1 = 1
        """
        return where_str

    def _join(self):
        join_str = """
        JOIN hr_timesheet_sheet_sheet AS b ON
            a.sheet_id = b.id
        JOIN hr_employee AS c ON
            b.employee_id = c.id
        """
        return join_str

    def _group_by(self):
        group_str = """
        GROUP BY
            a.id,
            b.id,
            c.id,
            c.department_id,
            c.job_id,
            a.item_id,
            b.state,
            b.date_from,
            b.date_to,
            c.parent_id
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
