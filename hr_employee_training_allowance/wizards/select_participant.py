# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api


class SelectTrainingParticipant(models.TransientModel):
    _inherit = "hr.select_training_participant"

    @api.multi
    def _prepare_write_data(self):
        _super = super(SelectTrainingParticipant, self)
        result = _super._prepare_write_data()
        obj_employee = self.env["hr.employee"]
        training = self.training_id
        participant_type = training.participant_type_id
        if len(result["partisipant_ids"]) > 0:
            for seq, participant in enumerate(result["partisipant_ids"]):
                employee = obj_employee.browse(
                    [participant[2]["partisipant_id"]])[0]
                pricelist = participant_type._get_allowance_pricelist(
                    training,
                    employee)
                result["partisipant_ids"][seq - 1][2].update({
                    "pricelist_id": pricelist and pricelist.id or False,
                })
        return result
