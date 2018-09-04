# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class HrOvertimeRequest(models.Model):
    _name = "hr.overtime_request"
    _inherit = ["hr.overtime_request", "tier.validation"]
    _state_from = ["confirm"]
    _state_to = ["valid"]
