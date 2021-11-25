# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models, tools


class HrEmployeeProjectExperienceReport(models.Model):
    _name = "hr.employee_project_experience_report"
    _description = "Employee Project Experience"
    _auto = False

    employee_id = fields.Many2one(
        string="Employee",
        comodel_name="hr.employee",
    )
    project_id = fields.Many2one(
        string="Project",
        comodel_name="project.project",
    )
    product_id = fields.Many2one(
        string="Function",
        comodel_name="product.product",
    )
    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
    )
    date_start = fields.Date(
        string="Date Start",
    )
    date_end = fields.Date(
        string="Date End",
    )

    def _select(self):
        select_str = """
        SELECT
            a.id AS id,
            e.id AS employee_id,
            c.id AS project_id,
            a.product_id AS product_id,
            b.partner_id AS partner_id,
            b.date_start AS date_start,
            b.date AS date_end
        """
        return select_str

    def _from(self):
        from_str = """
        analytic_user_funct_grid AS a
        """
        return from_str

    def _where(self):
        where_str = """
        WHERE 1 = 1
        """
        return where_str

    def _join(self):
        join_str = """
        JOIN account_analytic_account AS b ON
            a.account_id = b.id
        JOIN project_project AS c ON
            b.id = c.analytic_account_id
        JOIN resource_resource AS d ON
            a.user_id = d.user_id
        JOIN hr_employee AS e ON
            d.id = e.resource_id
        """
        return join_str

    def _group_by(self):
        group_str = """
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
