# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields
from openerp import tools


class HrCareerTransitionAnalysis(models.Model):
    _name = "hr.career_transition_analysis"
    _description = "Career Transition Analysis"
    _auto = False

    employee_id = fields.Many2one(
        string="Employee",
        comodel_name="hr.employee",
    )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="hr.career_transition_type",
    )
    effective_date = fields.Date(
        string="Effective Date",
    )
    reason_id = fields.Many2one(
        string="Reason",
        comodel_name="hr.career_transition_type_reason",
    )
    new_company_id = fields.Many2one(
        string="New Company",
        comodel_name="res.company",
    )
    new_department_id = fields.Many2one(
        string="New Department",
        comodel_name="hr.department",
    )
    new_job_id = fields.Many2one(
        string="New Job Title",
        comodel_name="hr.job",
    )
    new_working_hour_id = fields.Many2one(
        string="New Working Schedule",
        comodel_name="resource.calendar",
    )
    # Previous Data
    previous_company_id = fields.Many2one(
        string="Previous Company",
        comodel_name="res.company",
    )
    previous_department_id = fields.Many2one(
        string="Previous Department",
        comodel_name="hr.department",
    )
    previous_job_id = fields.Many2one(
        string="Previous Job Title",
        comodel_name="hr.job",
    )
    previous_working_hour_id = fields.Many2one(
        string="Previous Working Schedule",
        comodel_name="resource.calendar",
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("open", "On Progress"),
            ("valid", "Valid"),
            ("cancel", "Cancel"),
        ],
    )
    nbr = fields.Integer(
        string="Number of Career Transition",
    )

    def _select(self):
        select_str = """
        SELECT
            a.id AS id,
            a.company_id AS company_id,
            a.employee_id AS employee_id,
            a.type_id AS type_id,
            a.effective_date AS effective_date,
            a.reason_id AS reason_id,
            a.new_company_id AS new_company_id,
            a.new_department_id AS new_department_id,
            a.new_job_id AS new_job_id,
            a.new_working_hour_id AS new_working_hour_id,
            a.previous_company_id AS previous_company_id,
            a.previous_department_id AS previous_department_id,
            a.previous_job_id AS previous_job_id,
            a.previous_working_hour_id AS previous_working_hour_id,
            a.state AS state,
            COUNT(a.id) AS nbr
        """
        return select_str

    def _from(self):
        from_str = """
        hr_career_transition AS a
        """
        return from_str

    def _where(self):
        where_str = """
        WHERE 1 = 1
        """
        return where_str

    def _join(self):
        join_str = """
        """
        return join_str

    def _group_by(self):
        group_str = """
        GROUP BY
            a.id,
            a.company_id,
            a.employee_id,
            a.type_id,
            a.effective_date,
            a.reason_id,
            a.new_company_id,
            a.new_department_id,
            a.new_job_id,
            a.new_working_hour_id,
            a.previous_company_id,
            a.previous_department_id,
            a.previous_job_id,
            a.previous_working_hour_id,
            a.state
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
