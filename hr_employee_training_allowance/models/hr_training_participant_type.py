# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import _, api, fields, models
from openerp.exceptions import Warning as UserError
from openerp.tools.safe_eval import safe_eval as eval


class HrTrainingParticipantType(models.Model):
    _inherit = "hr.training_participant_type"

    pricelist_allowance_policy_ids = fields.One2many(
        string="Allowance Pricelist Policy",
        comodel_name="hr.training_allowance_pricelist_policy",
        inverse_name="type_id",
    )

    @api.multi
    def _get_allowance_pricelist(self, training, employee):
        self.ensure_one()
        result = False
        localdict = {
            "env": self.env,
            "participant_type": self,
            "training": training,
            "employee": employee,
        }
        for policy in self.pricelist_allowance_policy_ids:
            try:
                eval(
                    policy.policy_field_id.python_code,
                    localdict,
                    mode="exec",
                    nocopy=True,
                )
                result = localdict["result"]
                if result:
                    break
            except Exception:
                warning_msg = _("Error on pricelist allowance formula")
                raise UserError(warning_msg)
        return result
