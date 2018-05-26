# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api


class HrSalaryRule(models.Model):
    _inherit = "hr.salary.rule"

    @api.multi
    def compute_rule(self, localdict):
        self.ensure_one()

        class BrowsableObject(object):

            def __init__(self, dict):
                self.dict = dict

            def __getattr__(self, attr):
                return attr in self.dict and self.dict.__getitem__(attr) or 0.0

        payslip = localdict["payslip"]
        if not isinstance(payslip, type(self.env["hr.payslip"])):
            payslip = payslip.dict
            payslip.refresh()
            localdict["payslip"] = payslip
        ts_computations = {}
        for ts_computation in payslip.timesheet_computation_ids:
            ts_computations[ts_computation.item_id.code] = ts_computation
        obj_ts_computation = BrowsableObject(ts_computations)
        localdict["ts_computations"] = obj_ts_computation

        return super(HrSalaryRule, self).compute_rule(self.id, localdict)
