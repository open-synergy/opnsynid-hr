# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import _, api, fields, models
from openerp.addons import decimal_precision as dp
from openerp.exceptions import Warning as UserError
from openerp.tools.safe_eval import safe_eval as eval


class HrTrainingAllowance(models.Model):
    _name = "hr.training_allowance"
    _description = "Training Allowance"

    @api.model
    def _get_quantity(self):
        return 1.0

    @api.model
    def _default_qty_computation_method(self):
        return "fixed"

    training_id = fields.Many2one(
        string="Training",
        comodel_name="hr.training",
        ondelete="cascade",
    )
    participant_type_ids = fields.Many2many(
        string="Allowed Participant Types",
        comodel_name="hr.training_participant_type",
        relation="rel_allowance_2_participant_type",
        column1="allowance_id",
        column2="participant_type_id",
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
    qty_computation_method = fields.Selection(
        string="Qty. Computation Method",
        selection=[
            ("fixed", "Fixed"),
            ("code", "Python Code"),
        ],
        required=True,
        default=lambda self: self._default_qty_computation_method(),
    )

    quantity = fields.Float(
        string="Qty.",
        digits=dp.get_precision("Product Unit of Measure"),
        required=True,
        default=lambda self: self._get_quantity(),
    )
    python_code = fields.Text(
        string="Python Code",
    )
    uom_id = fields.Many2one(
        string="UoM",
        comodel_name="product.uom",
        required=True,
    )
    note = fields.Text(
        string="Note",
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
            prod_id=self.product_id.id, qty=self.quantity
        )[p_id]
        price_unit = obj_uom._compute_price(
            self.product_id.uom_id.id, price_unit, self.uom_id.id
        )
        data = {
            "participant_id": participant.id,
            "product_id": self.product_id.id,
            "uom_id": self.uom_id.id,
            "quantity": self._compute_qty(participant),
            "pricelist_id": participant.pricelist_id.id,
            "price_unit": price_unit,
        }
        return data

    @api.multi
    def _check_participant_type(self, participant):
        self.ensure_one()
        result = False

        if not self.participant_type_ids:
            result = True
        elif participant.type_id in self.participant_type_ids:
            result = True

        return result

    @api.multi
    def _compute_qty(self, participant):
        self.ensure_one()
        if self.qty_computation_method == "fixed":
            result = self.quantity
        else:
            localdict = {
                "env": self.env,
                "allowance": self,
                "participant": participant,
            }
            try:
                eval(self.python_code, localdict, mode="exec", nocopy=True)
                result = localdict["result"]
            except Exception:
                warning_msg = _("Error on allowance quantity formula")
                raise UserError(warning_msg)
        return result
