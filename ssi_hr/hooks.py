# Copyright 2025 OpenSynergy Indonesia
# Copyright 20202523 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import re

from odoo import SUPERUSER_ID, api


def _generate_initials(name):
    if not name:
        return ""
    # Ambil hanya bagian sebelum koma
    main_part = name.split(",")[0]

    # Hilangkan gelar depan umum
    main_part = re.sub(
        r"\b(Dr|Ir|Prof|Hj|H|Mr|Mrs|Ms)\.?\s+", "", main_part, flags=re.IGNORECASE
    )

    # Ambil huruf pertama dari tiap kata
    words = main_part.split()
    return "".join([w[0].upper() for w in words if w and w[0].isalpha()])


def _populate_initials(env):
    employees = env["hr.employee"].with_context(active_test=False).search([])
    for emp in employees:
        if not emp.initials or not emp.initials_manual:
            emp.initials = _generate_initials(emp.name)
            emp.initials_manual = False


def post_init_hook(cr, registry):
    """Run after fresh install"""
    env = api.Environment(cr, SUPERUSER_ID, {})
    _populate_initials(env)
