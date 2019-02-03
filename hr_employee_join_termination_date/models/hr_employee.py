# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    date_join = fields.Date(
        string="Join Date",
    )
    date_termination = fields.Date(
        string="Termination Date",
    )
