# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class HrTrainingParticipant(models.Model):
    _inherit = "hr.training_partisipant"

    organization_unit_id = fields.Many2one(
        string="Organization Unit",
        comodel_name="hr.department",
    )

    @api.onchange(
        "partisipant_id",
    )
    def onchange_organization_unit_id(self):
        self.organization_unit_id = False
        if self.partisipant_id:
            self.organization_unit_id = self.partisipant_id.organization_unit_id
