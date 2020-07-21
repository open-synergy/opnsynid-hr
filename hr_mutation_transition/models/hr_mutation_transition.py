# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api


class HrMutationTransition(models.Model):
    _name = "hr.mutation_transition"
    _inherit = ["hr.career_transition"]
    _description = "Career Transition - Mutation"
    _table = "hr_career_transition"

    @api.model
    def _default_type_id(self):
        return self.env.ref(
            "hr_mutation_transition."
            "career_transition_mutation").id

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        type_id = self.env.ref(
            "hr_mutation_transition."
            "career_transition_mutation", False) and self.env.ref(
                "hr_mutation_transition."
                "career_transition_mutation") or self.env["hr."
                                                          "career_transition_"
                                                          "type"]
        args.append(("type_id", "=", type_id.id))
        return super(HrMutationTransition, self).search(
            args=args, offset=offset, limit=limit,
            order=order, count=count)
