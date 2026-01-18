# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import re

from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    initials = fields.Char(
        string="Initials",
        compute="_compute_initials",
        inverse="_inverse_initials",
        store=True,
        compute_sudo=True,
        help="Automatically generated from name, unless manually overridden.",
    )

    initials_manual = fields.Boolean(
        string="Initials Manually Set",
        default=False,
        help="If checked, initials will not auto-update from name.",
    )

    def _generate_initials(self, name):
        if not name:
            return ""
        # Ambil hanya bagian sebelum koma
        main_part = name.split(",")[0]

        # Hilangkan gelar depan umum
        main_part = re.sub(
            r"\b(Dr|Ir|Prof|Hj|H|Mr|Mrs|Ms)\.?\s+",
            "",
            main_part,
            flags=re.IGNORECASE,
        )

        # Ambil huruf pertama dari tiap kata
        words = main_part.split()
        return "".join([w[0].upper() for w in words if w and w[0].isalpha()])

    @api.depends("name")
    def _compute_initials(self):
        for rec in self:
            # hanya generate kalau belum manual
            if not rec.initials_manual:
                rec.initials = rec._generate_initials(rec.name)

    def _inverse_initials(self):
        """Kalau user edit initials manual, tandai supaya tidak ditimpa lagi"""
        for rec in self:
            auto_value = rec._generate_initials(rec.name)
            if rec.initials and rec.initials != auto_value:
                rec.initials_manual = True
            elif not rec.initials:
                # kalau dikosongkan, balik ke auto mode
                rec.initials_manual = False
