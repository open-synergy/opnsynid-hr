# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _


class HrTrainingParticipant(models.Model):
    _inherit = "hr.training_partisipant"

    allowance_ids = fields.One2many(
        string="Training Allowance",
        comodel_name="hr.training_participant_allowance",
        inverse_name="participant_id",
    )
    pricelist_id = fields.Many2one(
        string="Default Pricelist",
        comodel_name="product.pricelist",
    )

    @api.multi
    def _generate_allowance(self):
        self.ensure_one()
        training = self.training_id
        if not self.pricelist_id:
            str_warning = _("No pricelist defined")
            raise UserError(str_warning)
        for allowance in training.allowance_ids:
            if self._check_existing_product(
                allowance.product_id
            ) and allowance._check_participant_type(self):
                allowance._create_participant_allowance(self)

    @api.multi
    def _remove_allowance(self):
        self.ensure_one()
        criteria = [
            ("participant_id", "=", self.id),
            (
                "state",
                "=",
                "draft",
            ),
        ]
        self.env["hr.training_participant_allowance"].search(criteria).unlink()

    @api.multi
    def action_generate_allowance(self):
        self.ensure_one()
        for participant in self:
            participant._remove_allowance()
            participant._generate_allowance()

    @api.multi
    def _check_existing_product(self, product):
        self.ensure_one()
        result = True
        criteria = [
            ("participant_id", "=", self.id),
            ("product_id", "=", product.id),
        ]
        if self.env["hr.training_participant_allowance"].search_count(criteria) > 0:
            result = False
        return result
