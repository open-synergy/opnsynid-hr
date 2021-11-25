# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime

from openerp import api, models


class HrTrainingParticipant(models.Model):
    _inherit = "hr.training_partisipant"

    @api.multi
    def button_accomplish(self):
        _super = super(HrTrainingParticipant, self)
        _super.button_accomplish()

        for participant in self:
            participant._create_certification()

    @api.multi
    def _create_certification(self):
        self.ensure_one()
        obj_certification = self.env["hr.certification"]
        obj_certification.create(self._prepare_create_certification())

    @api.multi
    def button_reset(self):
        _super = super(HrTrainingParticipant, self)
        _super.button_reset()
        for participant in self:
            participant._delete_certification()

    @api.multi
    def _prepare_create_certification(self):
        self.ensure_one()
        training = self.training_id
        date_start = datetime.strptime(
            self.training_id.date_start, "%Y-%m-%d %H:%M:%S"
        ).strftime("%Y-%m-%d")
        date_end = datetime.strptime(
            self.training_id.date_end, "%Y-%m-%d %H:%M:%S"
        ).strftime("%Y-%m-%d")
        return {
            "name": training.name,
            "employee_id": self.partisipant_id.id,
            "start_date": date_start,
            "end_date": date_end,
            "expire": False,
            "training_category_id": training.category_id.id,
            "participant_id": self.id,
        }

    @api.multi
    def _delete_certification(self):
        self.ensure_one()
        domain = self._prepare_certification_domain()
        obj_certification = self.env["hr.certification"]
        certifications = obj_certification.search(domain)
        certifications.write({"participant_id": False})
        certifications.unlink()

    @api.multi
    def _prepare_certification_domain(self):
        self.ensure_one()
        return [
            ("participant_id", "=", self.id),
        ]
