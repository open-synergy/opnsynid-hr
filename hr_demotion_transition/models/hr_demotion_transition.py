# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api


class HrDemotionTransition(models.Model):
    _name = "hr.demotion_transition"
    _inherit = ["hr.career_transition"]
    _description = "Career Transition - Demotion"
    _table = "hr_career_transition"

    @api.model
    def _default_type_id(self):
        return self.env.ref(
            "hr_demotion_transition."
            "career_transition_demotion").id

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        type_id = self.env.ref(
            "hr_demotion_transition."
            "career_transition_demotion", False) and self.env.ref(
                "hr_demotion_transition."
                "career_transition_demotion") or self.env["hr."
                                                          "career_transition_"
                                                          "type"]
        args.append(("type_id", "=", type_id.id))
        return super(HrDemotionTransition, self).search(
            args=args, offset=offset, limit=limit,
            order=order, count=count)
