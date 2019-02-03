# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class HrDepartment(models.Model):
    _inherit = "hr.department"

    department_type_id = fields.Many2one(
        string="Department Type",
        comodel_name="hr.department.type"
    )
