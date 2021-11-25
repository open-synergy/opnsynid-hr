# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _


class HrCertification(models.Model):
    _inherit = "hr.certification"

    training_category_id = fields.Many2one(
        string="Training Category",
        comodel_name="hr.training_category",
        domain=[
            ("type", "=", "normal"),
        ],
        ondelete="cascade",
    )
    participant_id = fields.Many2one(
        string="Participant",
        comodel_name="hr.training_partisipant",
    )
    training_id = fields.Many2one(
        string="Training",
        comodel_name="hr.training",
        related="participant_id.training_id",
        store=True,
    )

    @api.multi
    def unlink(self):
        _super = super(HrCertification, self)
        for certification in self:
            if certification.participant_id:
                str_warning = _(
                    "You can not delete certification that "
                    "link into training participant"
                )
                raise UserError(str_warning)
        return _super.unlink()
