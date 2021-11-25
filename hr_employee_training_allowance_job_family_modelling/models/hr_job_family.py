# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class HrJobFamily(models.Model):
    _inherit = "hr.job_family"

    training_allowance_pricelist_ids = fields.One2many(
        string="Training Allowance Pricelist",
        comodel_name="hr.job_family_training_allowance_pricelist",
        inverse_name="job_family_id",
    )

    @api.multi
    def _get_training_allowance_pricelist(self, participant_type):
        self.ensure_one()
        obj_pricelist = self.env["hr.job_family_training_allowance_pricelist"]
        criteria = [
            ("job_family_id", "=", self.id),
            ("participant_type_id", "=", participant_type.id),
        ]
        pricelists = obj_pricelist.search(criteria)
        return pricelists[0].pricelist_id if len(pricelists) > 0 else False


class HrJobFamilyTrainingAllowancePricelist(models.Model):
    _name = "hr.job_family_training_allowance_pricelist"
    _description = "Job Family Training Allowance Pricelist"

    job_family_id = fields.Many2one(
        string="Job Family",
        comodel_name="hr.job_family",
        required=True,
        ondelete="cascade",
    )
    participant_type_id = fields.Many2one(
        string="Participant Type",
        comodel_name="hr.training_participant_type",
        required=True,
        ondelete="restrict",
    )
    pricelist_id = fields.Many2one(
        string="Pricelist",
        comodel_name="product.pricelist",
        required=True,
        ondelete="restrict",
    )
