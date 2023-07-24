# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    project_experience_ids = fields.One2many(
        string="Detail Summary",
        comodel_name="hr.employee_project_experience",
        inverse_name="employee_id",
        readonly=True,
    )
