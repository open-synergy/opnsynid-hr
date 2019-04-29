# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    @api.multi
    @api.depends(
        "employee_id", "date_from", "date_to")
    def _compute_goal_ids(self):
        obj_goal = self.env["gamification.goal"]
        for payslip in self:
            goal_ids = []
            if payslip.employee_id.user_id:
                criteria = [
                    "&",
                    ("user_id", "=", payslip.employee_id.user_id.id),
                    "|",
                    "&",
                    "&",
                    ("end_date", "!=", False),
                    ("start_date", ">=", payslip.date_from),
                    ("end_date", "<=", payslip.date_to),
                    "&",
                    "&",
                    ("end_date", "=", False),
                    ("start_date", ">=", payslip.date_from),
                    ("start_date", "<=", payslip.date_to),
                ]
                goal_ids = obj_goal.search(criteria).ids
            payslip.gamification_goal_ids = [(6, 0, goal_ids)]

    gamification_goal_ids = fields.Many2many(
        string="Gamification Goals",
        comodel_name="gamification.goal",
        compute="_compute_goal_ids",
        relation="rel_payslip_2_gamification_goal",
        column1="payslip_id",
        column2="goal_id",
    )
