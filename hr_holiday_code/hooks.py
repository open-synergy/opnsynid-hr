# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import SUPERUSER_ID


def create_code_equal_to_id(cr):
    """
    With this pre-init-hook we want to avoid error when creating the UNIQUE
    code constraint when the module is installed and before the post-init-hook
    is launched.
    """
    cr.execute("ALTER TABLE hr_holidays " "ADD COLUMN holiday_code character varying;")
    cr.execute("UPDATE hr_holidays " "SET holiday_code = id;")


def assign_old_sequences(cr, registry):
    """
    This post-init-hook will update all existing issue assigning them the
    corresponding sequence code.
    """
    hr_holidays_obj = registry["hr.holidays"]
    sequence_obj = registry["ir.sequence"]

    criteria_lvr = [("type", "=", "remove")]

    lvr_ids = hr_holidays_obj.search(cr, SUPERUSER_ID, criteria_lvr, order="id")

    for lvr in lvr_ids:
        # pylint: disable=locally-disabled, sql-injection
        cr.execute(
            "UPDATE hr_holidays "
            "SET holiday_code = '%s' "
            "WHERE id = %d;"
            % (sequence_obj.get(cr, SUPERUSER_ID, "hr.holidays.lvr"), lvr)
        )

    criteria_alr = [("type", "=", "add")]

    alr_ids = hr_holidays_obj.search(cr, SUPERUSER_ID, criteria_alr, order="id")

    for alr in alr_ids:
        # pylint: disable=locally-disabled, sql-injection
        cr.execute(
            "UPDATE hr_holidays "
            "SET holiday_code = '%s' "
            "WHERE id = %d;"
            % (sequence_obj.get(cr, SUPERUSER_ID, "hr.holidays.alr"), alr)
        )
