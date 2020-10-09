# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openerp import SUPERUSER_ID


def set_double_validation_false(cr, registry):
    obj_hr_holidays_status = registry["hr.holidays.status"]
    criteria = [
        ("double_validation", "=", True)
    ]
    status_ids = \
        obj_hr_holidays_status.search(cr, SUPERUSER_ID, criteria)
    if holidays_status_ids:
        obj_hr_holidays_status.write(
            cr, SUPERUSER_ID, status_ids, {"double_validation": False})
