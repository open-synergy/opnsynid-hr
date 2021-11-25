# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class HrTraining(models.Model):
    _inherit = "hr.training"

    organization_unit_id = fields.Many2one(
        string="Organization Unit",
        comodel_name="hr.department",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )

    @api.onchange(
        "request_by_id",
    )
    def onchange_organization_unit_id(self):
        self.organization_unit_id = False
        if self.request_by_id:
            self.organization_unit_id = self.request_by_id.organization_unit_id
