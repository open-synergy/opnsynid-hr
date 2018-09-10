# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade
from openerp import api, SUPERUSER_ID


def reload_record_rule(env):
    openupgrade.load_data(
        env.cr,
        "hr_attendance_overtime_request",
        "security/ir_rule_data.xml",
        mode="update"
    )


@openupgrade.migrate()
def migrate(cr, version):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})

        reload_record_rule(env)
