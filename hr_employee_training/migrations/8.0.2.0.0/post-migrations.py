# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import SUPERUSER_ID, api
from openupgradelib import openupgrade


def map_training_participant(env):
    openupgrade.map_values(
        env.cr,
        "state",
        "state",
        [
            ("absence", "draft"),
        ],
        table="hr_training_partisipant",
        write="sql",
    )


@openupgrade.migrate()
def migrate(cr, version):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})

        map_training_participant(env)
