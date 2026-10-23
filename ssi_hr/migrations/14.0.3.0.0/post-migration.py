# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
import re

from openupgradelib import openupgrade


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


@openupgrade.migrate()
def migrate(env, version):
    """Populate initials for existing employees.

    :param env: the Odoo environment provided by ``openupgrade``
    :param version: the installed version, empty on fresh install
    """
    if not version:
        return

    employees = env["hr.employee"].with_context(active_test=False).search([])
    for emp in employees:
        if not emp.initials or not emp.initials_manual:
            emp.initials = _generate_initials(emp.name)
            emp.initials_manual = False
