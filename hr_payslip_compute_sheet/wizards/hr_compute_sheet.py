# -*- coding: utf-8 -*-
# © 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api, _
from openerp.exceptions import Warning as UserError


class HrComputeSheet(models.TransientModel):
    _name = 'hr.compute_sheet'
    _description = 'HR Compute Sheet'

    reload_input = fields.Boolean(
        string="Reload Input",
        default=False
    )

    reload_workdays = fields.Boolean(
        string="Reload Workdays",
        default=False
    )

    def get_contract_ids(self, payslip):
        contract_ids = payslip.get_contract(
            employee=payslip.employee_id,
            date_from=payslip.date_from,
            date_to=payslip.date_to)
        return contract_ids

    def _reload_input(self, payslip):
        contract_ids = self.get_contract_ids(payslip)
        input_line_ids = payslip.get_inputs(
            contract_ids=contract_ids,
            date_from=payslip.date_from,
            date_to=payslip.date_to)
        if input_line_ids:
            for input_line in payslip.input_line_ids:
                reset = {
                    'input_line_ids': [(2, input_line.id)]
                    }
                payslip.write(reset)
            vals = {
                'input_line_ids': [(0, 0, input_line_ids[0])]
                }
            payslip.write(vals)

    def _reload_workdays(self, payslip):
        contract_ids = self.get_contract_ids(payslip)
        worked_days_line_ids = payslip.get_worked_day_lines(
            contract_ids=contract_ids,
            date_from=payslip.date_from,
            date_to=payslip.date_to)
        if worked_days_line_ids:
            for worked_days in payslip.worked_days_line_ids:
                reset = {
                    'worked_days_line_ids': [(2, worked_days.id)]
                    }
                payslip.write(reset)
            vals = {
                'worked_days_line_ids': [(
                    0, 0, worked_days_line_ids[0])]
                }
            payslip.write(vals)

    @api.multi
    def button_compute_sheet(self):
        self.ensure_one()
        obj_hr_payslip = self.env['hr.payslip']
        context = self._context
        record_ids = context['active_ids']

        for payslip in obj_hr_payslip.browse(record_ids):
            if payslip.state == 'draft':
                if self.reload_input:
                    self._reload_input(payslip)
                if self.reload_workdays:
                    self._reload_workdays(payslip)
            else:
                raise UserError(
                    _('Payslip No. %s '
                      'cannot be computed '
                      'because state is done.') % (payslip.number,))
            payslip.compute_sheet()

        return {'type': 'ir.actions.act_window_close'}
