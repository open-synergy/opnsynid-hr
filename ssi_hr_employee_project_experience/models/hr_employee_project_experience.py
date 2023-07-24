# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HrEmployeeProjectExprerience(models.Model):
    _name = "hr.employee_project_experience"
    _description = "Employee Project Experience"
    _auto = False

    employee_id = fields.Many2one(
        string="Employee",
        comodel_name="hr.employee",
        readonly=True,
    )
    date_start = fields.Date(
        string="Date Start",
        readonly=True,
    )
    date_end = fields.Date(
        string="Date End",
        readonly=True,
    )
    role_id = fields.Many2one(
        string="Role",
        comodel_name="project.role",
        readonly=True,
    )
    project_id = fields.Many2one(
        string="Project",
        comodel_name="project.project",
        readonly=True,
    )
    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        readonly=True,
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="project.type",
        readonly=True,
    )

    @property
    def _table_query(self):
        return "%s %s %s %s" % (
            self._select(),
            self._from(),
            self._join(),
            self._where(),
        )

    @api.model
    def _select(self):
        select_str = """
        SELECT
            row_number() OVER() as id,
            d.id AS employee_id,
            a.date_start AS date_start,
            a.date_end AS date_end,
            a.role_id AS role_id,
            b.id AS project_id,
            b.partner_id AS partner_id,
            b.type_id AS type_id
        """
        return select_str

    @api.model
    def _from(self):
        from_str = """
        FROM project_assignment AS a
        """
        return from_str

    @api.model
    def _join(self):
        join_str = """
        JOIN project_project AS b ON
            a.project_id=b.id
        JOIN resource_resource AS c ON
            a.asignee_id = c.user_id
        JOIN hr_employee AS d ON
            c.id = d.resource_id
        """
        return join_str

    @api.model
    def _where(self):
        where_str = """
        WHERE a.state NOT IN ('cancel', 'reject')
        """
        return where_str
