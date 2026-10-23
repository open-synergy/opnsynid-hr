# Copyright 2025 OpenSynergy Indonesia
# Copyright 20202523 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import re

from odoo import SUPERUSER_ID, api


def _generate_initials(name):
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
        r"\b(Dr|Ir|Prof|Hj|H|Mr|Mrs|Ms)\.?\s+", "", main_part, flags=re.IGNORECASE
    )

    # Take the first letter of each word
    words = main_part.split()
    return "".join([w[0].upper() for w in words if w and w[0].isalpha()])


def _populate_initials(env):
    """Fill the initials of employees lacking a manual value.

    Employees whose initials are empty or not manually set are
    regenerated from their name and flagged as automatic.

    :param env: the Odoo environment used to search employees
    """
    employees = env["hr.employee"].with_context(active_test=False).search([])
    for emp in employees:
        if not emp.initials or not emp.initials_manual:
            emp.initials = _generate_initials(emp.name)
            emp.initials_manual = False


def post_init_hook(cr, registry):
    """Run after fresh install"""
    env = api.Environment(cr, SUPERUSER_ID, {})
    _populate_initials(env)
