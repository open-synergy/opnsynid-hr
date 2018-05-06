# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.addons import decimal_precision as dp


class HrTrainingParticipantAllowance(models.Model):
    _name = "hr.training_participant_allowance"
    _description = "Training Participant Allowance"

    @api.model
    def _get_quantity(self):
        return 1.0

    @api.multi
    @api.depends(
        "quantity",
        "price_unit",
    )
    def _compute_price(self):
        for allw in self:
            self.price_subtotal = self.price_unit * \
                self.quantity

    participant_id = fields.Many2one(
        string="Participant",
        comodel_name="hr.training_partisipant",
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
    pricelist_id = fields.Many2one(
        string="Product Pricelist",
        comodel_name="product.pricelist",
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
    price_unit = fields.Float(
        string="Unit Price",
        required=True,
        default=0.0,
    )
    price_subtotal = fields.Float(
        string="Price Subtotal",
        compute="_compute_price",
        store=True,
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("approve", "Approved"),
            ("reject", "Rejected"),
        ],
        required=True,
        default="draft",
    )

    @api.multi
    def button_confirm(self):
        for allw in self:
            allw.write(self._prepare_confirm_data())

    @api.multi
    def button_approve(self):
        for allw in self:
            allw.write(self._prepare_approve_data())

    @api.multi
    def button_reject(self):
        for allw in self:
            allw.write(self._prepare_reject_data())

    @api.multi
    def button_restart(self):
        for allw in self:
            allw.write(self._prepare_restart_data())

    @api.multi
    def _prepare_confirm_data(self):
        self.ensure_one()
        return {
            "state": "confirm",
        }

    @api.multi
    def _prepare_approve_data(self):
        self.ensure_one()
        return {
            "state": "approve",
        }

    @api.multi
    def _prepare_reject_data(self):
        self.ensure_one()
        return {
            "state": "reject",
        }

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

    @api.onchange(
        "product_id",
        "quantity",
        "pricelist_id",
        "uom_id",
    )
    def onchange_price_unit(self):
        self.price_unit = 0.0
        quantity = self.quantity
        obj_uom = self.env["product.uom"]
        if self.product_id and \
                self.quantity and self.pricelist_id and \
                self.uom_id:
            self.price_unit = self.pricelist_id.price_get(
                prod_id=self.product_id.id, qty=quantity)[self.pricelist_id.id]
            self.price_unit = obj_uom._compute_price(
                self.product_id.uom_id.id, self.price_unit, self.uom_id.id)
