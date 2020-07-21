# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api


class HrAssignmentTransition(models.Model):
    _name = "hr.assignment_transition"
    _inherit = ["hr.career_transition"]
    _description = "Career Transition - New Assignment"
    _table = "hr_career_transition"

    @api.model
    def _default_type_id(self):
        return self.env.ref(
            "hr_assignment_transition."
            "career_transition_assignment").id

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        ref_name = "hr_assignment_transition.career_transition_assignment"
        type_id = self.env.ref(ref_name, False) and \
            self.env.ref(ref_name) or \
            self.env["hr.career_transition_type"]
        args.append(("type_id", "=", type_id.id))
        return super(HrAssignmentTransition, self).search(
            args=args, offset=offset, limit=limit,
            order=order, count=count)
