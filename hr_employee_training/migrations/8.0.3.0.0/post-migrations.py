# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade
from openerp import api, SUPERUSER_ID, registry


def default_training_participant(env):
    pool = registry(env.cr.dbname)
    val = env.ref(
        "hr_employee_training.hr_training_participant_type_default")
    openupgrade.set_defaults(
        env.cr,
        pool,
        {
            "hr.training_partisipant": [
                ("type_id", val.id)
            ]
        },
    )


def default_training(env):
    pool = registry(env.cr.dbname)
    val = env.ref(
        "hr_employee_training.hr_training_participant_type_default")
    openupgrade.set_defaults(
        env.cr,
        pool,
        {
            "hr.training": [
                ("participant_type_id", val.id)
            ]
        },
    )


@openupgrade.migrate()
def migrate(cr, version):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})

        default_training(env)
        default_training_participant(env)
