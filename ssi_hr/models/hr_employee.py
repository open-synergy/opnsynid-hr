# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import re

from odoo import api, fields, models


class HrEmployee(models.Model):
    # Extends the standard hr.employee model with initials support.
    #
    # Automatically computes employee initials from the employee name,
    # stripping common titles and taking the first letter of each word.
    # Users can manually override initials, at which point
    # auto-generation is disabled.

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
        """Build the initials of a person name.

        Only the part before the first comma is used. Common titles
        (Dr, Ir, Prof, Hj, H, Mr, Mrs, Ms) are removed, then the first
        letter of each alphabetic word is taken and uppercased.

        :param name: the employee name
        :return: the generated initials, empty when ``name`` is empty
        """
        if not name:
            return ""
        # Take only the part before the comma
        main_part = name.split(",")[0]

        # Remove common leading titles
        main_part = re.sub(
            r"\b(Dr|Ir|Prof|Hj|H|Mr|Mrs|Ms)\.?\s+",
            "",
            main_part,
            flags=re.IGNORECASE,
        )

        # Take the first letter of each word
        words = main_part.split()
        return "".join([w[0].upper() for w in words if w and w[0].isalpha()])

    @api.depends("name")
    def _compute_initials(self):
        """Compute ``initials`` from the employee name.

        Records flagged ``initials_manual`` keep their value.
        """
        for rec in self:
            # only generate when not manually set
            if not rec.initials_manual:
                rec.initials = rec._generate_initials(rec.name)

    def _inverse_initials(self):
        """Flag initials as manual when the user edits them.

        Clearing the value switches the record back to automatic mode.
        """
        for rec in self:
            auto_value = rec._generate_initials(rec.name)
            if rec.initials and rec.initials != auto_value:
                rec.initials_manual = True
            elif not rec.initials:
                # when cleared, go back to auto mode
                rec.initials_manual = False
