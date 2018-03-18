# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api, fields


class ChangeTrainingAttendanceStatus(models.TransientModel):
    _name = "hr.change_training_attendance_status"
    _description = "Change Training Attendance Status"

    @api.model
    def _default_state(self):
        return self.env.context.get("state", "absence")

    @api.model
    def _default_attendance_ids(self):
        obj_att = self.env["hr.training_attendance"]
        state = self._default_state()
        attendance_ids = self.env.context.get("active_ids", [])
        criteria = [
            ("id", "in", attendance_ids),
            ("state", "!=", state),
        ]
        attendances = obj_att.search(criteria)
        return [(6, 0, attendances.ids)]

    state = fields.Selection(
        string="State",
        selection=[
            ("absence", "Absence"),
            ("present", "Present"),
        ],
        required=True,
        default=lambda self: self._default_state(),
    )

    attendance_ids = fields.Many2many(
        string="Attendances",
        comodel_name="hr.training_attendance",
        relation="rel_change_training_attendance_wiz_2_attendance",
        column1="wizard_id",
        column2="attendance_id",
        default=lambda self: self._default_attendance_ids(),
    )

    @api.multi
    def action_confirm(self):
        for wiz in self:
            wiz._change_attendance_status()

    @api.multi
    def _change_attendance_status(self):
        self.ensure_one()
        if self.state == "absence":
            self.attendance_ids.button_absence()
        else:
            self.attendance_ids.button_present()
