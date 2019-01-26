# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields
from openerp import tools


class HrPayslipAnalysis(models.Model):
    _name = "hr.payslip_analysis"
    _description = "Payslip Analysis"
    _auto = False

    payslip_id = fields.Many2one(
        string="Payslip",
        comodel_name="hr.payslip",
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
    rule_id = fields.Many2one(
        string="Salary Rule",
        comodel_name="hr.salary.rule",
    )
    structure_id = fields.Many2one(
        string="Salary Structure",
        comodel_name="hr.payroll.structure",
    )
    run_id = fields.Many2one(
        string="Payslip Run",
        comodel_name="hr.payslip.run",
    )
    payslip_state = fields.Selection(
        string="Payslip State",
        selection=[
            ("draft", "Draft"),
            ("verify", "Waiting"),
            ("done", "Done"),
            ("cancel", "Rejected"),
        ],
    )
    amount = fields.Float(
        string="Amount",
    )

    def _select(self):
        select_str = """
        SELECT
            a.id AS id,
            b.id AS payslip_id,
            c.id AS employee_id,
            c.department_id AS department_id,
            c.job_id AS job_id,
            a.salary_rule_id AS rule_id,
            b.state AS payslip_state,
            b.date_from AS date_start,
            b.date_to AS date_end,
            c.parent_id AS parent_id,
            b.struct_id AS structure_id,
            b.payslip_run_id AS run_id,
            SUM(a.rate) AS rate,
            SUM(a.amount) AS amount,
            SUM(a.quantity) AS quantity,
            SUM(a.total) AS total
        """
        return select_str

    def _from(self):
        from_str = """
        hr_payslip_line AS a
        """
        return from_str

    def _where(self):
        where_str = """
        WHERE 1 = 1
        """
        return where_str

    def _join(self):
        join_str = """
        JOIN hr_payslip AS b ON
            a.slip_id = b.id
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
            a.salary_rule_id,
            b.state,
            b.date_from,
            b.date_to,
            c.parent_id,
            b.struct_id,
            b.payslip_run_id
        """
        return group_str

    def init(self, cr):
        tools.drop_view_if_exists(cr, self._table)
        # pylint: disable=locally-disabled, sql-injection
        cr.execute("""CREATE or REPLACE VIEW %s as (
            %s
            FROM %s
            %s
            %s
            %s
        )""" % (
            self._table,
            self._select(),
            self._from(),
            self._join(),
            self._where(),
            self._group_by()
        ))
