# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    observer_ok = fields.Boolean(
        string="Avalaible as Observer",
    )
    trainer_ok = fields.Boolean(
        string="Available as Trainer",
    )

    @api.onchange("is_company")
    def onchange_observer_ok(self):
        if self.is_company:
            self.observer_ok = False

    @api.onchange("is_company")
    def onchange_trainer_ok(self):
        if self.is_company:
            self.trainer_ok = False
