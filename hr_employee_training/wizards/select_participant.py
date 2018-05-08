# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api, fields


class SelectTrainingParticipant(models.TransientModel):
    _name = "hr.select_training_participant"
    _description = "Select Training Participant"

    @api.model
    def _default_training_id(self):
        return self.env.context.get("active_id", False)

    @api.model
    def _default_participant_type_id(self):
        training_id = self._default_training_id()
        if not training_id:
            return False

        obj_training = self.env["hr.training"]
        return obj_training.browse([training_id])[0].\
            participant_type_id.id

    training_id = fields.Many2one(
        string="Training",
        comodel_name="hr.training",
        required=True,
        default=lambda self: self._default_training_id(),
    )
    employee_ids = fields.Many2many(
        string="Employee",
        comodel_name="hr.employee",
        relation="rel_select_participant_2_employee",
        column1="wizard_id",
        column2="employee_id",
        required=True,
    )
    participant_type_id = fields.Many2one(
        string="Participant Type",
        comodel_name="hr.training_participant_type",
        required=True,
        default=lambda self: self._default_participant_type_id(),
    )

    @api.onchange("training_id")
    def onchange_employee_ids(self):
        result = {
            "domain": {},
        }
        if self.training_id:
            existing_employee_ids = []
            for participant in self.training_id.partisipant_ids:
                existing_employee_ids.append(participant.partisipant_id.id)
            result["domain"].update({
                "employee_ids": [
                    ("id", "not in", existing_employee_ids),
                ]
            })
        return result

    @api.multi
    def action_select_participant(self):
        for wiz in self:
            wiz._select_participant()

    @api.multi
    def _select_participant(self):
        self.ensure_one()
        obj_training = self.env["hr.training"]
        training_id = self.env.context.get("active_id", False)
        training = obj_training.browse([training_id])[0]
        training.write(self._prepare_write_data())
        training.session_ids.button_generate_attendance()

    @api.multi
    def _prepare_write_data(self):
        self.ensure_one()
        list_participant = []
        for employee in self.employee_ids:
            criteria = [
                ("training_id", "=", self.training_id.id),
                ("partisipant_id", "=", employee.id),
            ]
            if self.env["hr.training_partisipant"].search_count(criteria) > 0:
                continue

            data = {
                "partisipant_id": employee.id,
                "job_id": employee.job_id and employee.job_id.id or False,
                "type_id": self.participant_type_id.id,
            }
            if self.training_id.state in ["start"]:
                data.update({"additional": True})
            list_participant.append((0, 0, data))
        result = {
            "partisipant_ids": list_participant,
        }
        return result
