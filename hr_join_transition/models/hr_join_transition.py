# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api


class HrJoinTransition(models.Model):
    _name = "hr.join_transition"
    _inherit = ["hr.career_transition"]
    _description = "Career Transition - Join"
    _table = "hr_career_transition"

    @api.model
    def _default_type_id(self):
        return self.env.ref(
            "hr_join_transition."
            "career_transition_join").id

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        type_id = self.env.ref(
            "hr_join_transition."
            "career_transition_join", False) and self.env.ref(
                "hr_join_transition."
                "career_transition_join") or self.env["hr."
                                                      "career_transition_"
                                                      "type"]
        args.append(("type_id", "=", type_id.id))
        return super(HrJoinTransition, self).search(
            args=args, offset=offset, limit=limit,
            order=order, count=count)
