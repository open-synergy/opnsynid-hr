# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.exceptions import Warning as UserError
from openerp.tools.safe_eval import safe_eval as eval
from openerp.tools.translate import _


class HrTimesheetComputationItem(models.Model):
    _name = "hr.timesheet_computation_item"
    _description = "Timesheet Computation Item"

    code = fields.Char(
        string="Code",
        required=True,
    )
    name = fields.Char(
        string="Name",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    python_code = fields.Text(
        string="Python Code",
    )
    note = fields.Text(
        string="Note",
    )

    @api.multi
    def _get_localdict(self, sheet):
        self.ensure_one()
        return {
            "env": self.env,
            "sheet": sheet,
            "employee": sheet.employee_id,
            "attendances": sheet.attendances_ids,
            "activities": sheet.timesheet_ids,
        }

    @api.multi
    def _compute(self, sheet):
        self.ensure_one()
        result = 0.0
        localdict = self._get_localdict(sheet)
        try:
            eval(self.python_code,
                 localdict, mode="exec", nocopy=True)
            result = localdict["result"]
        except:
            raise UserError(_("Error in timesheet computation"))
        return result
