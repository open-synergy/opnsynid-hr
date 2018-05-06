# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.addons import decimal_precision as dp


class HrTrainingAllowance(models.Model):
    _name = "hr.training_allowance"
    _description = "Training Allowance"

    @api.model
    def _get_quantity(self):
        return 1.0

    training_id = fields.Many2one(
        string="Training",
        comodel_name="hr.training",
        ondelete="cascade",
    )
    sequence = fields.Integer(
        string="Sequence",
        default=5,
        required=True,
    )
    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.product",
        required=True,
    )
    quantity = fields.Float(
        string="Qty.",
        digits=dp.get_precision("Product Unit of Measure"),
        required=True,
        default=lambda self: self._get_quantity(),
    )
    uom_id = fields.Many2one(
        string="UoM",
        comodel_name="product.uom",
        required=True,
    )

    @api.onchange(
        "product_id",
    )
    def onchange_uom_id(self):
        self.uom_id = False
        domain = {
            "uom_id": [
                ("id", "=", 0),
            ],
        }
        if self.product_id:
            self.uom_id = self.product_id.uom_id
            domain["uom_id"] = [
                ("category_id", "=", self.product_id.uom_id.category_id.id),
            ]
        return {
            "domain": domain,
        }

    @api.multi
    def _create_participant_allowance(self, participant):
        self.ensure_one()
        obj_allowance = self.env["hr.training_participant_allowance"]
        obj_allowance.create(self._prepare_participant_allowance(participant))

    @api.multi
    def _prepare_participant_allowance(self, participant):
        self.ensure_one()
        obj_uom = self.env["product.uom"]
        p_id = participant.pricelist_id.id
        price_unit = participant.pricelist_id.price_get(
            prod_id=self.product_id.id, qty=self.quantity)[p_id]
        price_unit = obj_uom._compute_price(
            self.product_id.uom_id.id, price_unit, self.uom_id.id)
        data = {
            "participant_id": participant.id,
            "product_id": self.product_id.id,
            "uom_id": self.uom_id.id,
            "quantity": self.quantity,
            "pricelist_id": participant.pricelist_id.id,
            "price_unit": price_unit,
        }
        return data
