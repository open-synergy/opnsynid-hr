# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    organization_unit_id = fields.Many2one(
        string="Organization Unit",
        comodel_name="hr.department"
    )

    @api.onchange("organization_unit_id")
    def _get_domain_department(self):
        domain = {}
        if self.organization_unit_id:
            self.department_id = False
            domain = {
                'department_id': [
                    ('id', 'child_of', [self.organization_unit_id.id])
                ]
            }
        return {'domain': domain}
