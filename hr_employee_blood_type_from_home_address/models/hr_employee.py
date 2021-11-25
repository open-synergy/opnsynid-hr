# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    blood_type_aob = fields.Selection(
        string="Blood Type (ABO)",
        selection=[
            ("a", "A"),
            ("b", "B"),
            ("ab", "AB"),
            ("o", "O"),
        ],
        related="address_home_id.blood_type_aob",
        store=True,
    )
    blood_type_rh = fields.Selection(
        string="Blood Type (Rh)",
        selection=[
            ("+", "+"),
            ("-", "-"),
        ],
        related="address_home_id.blood_type_rh",
        store=True,
    )
