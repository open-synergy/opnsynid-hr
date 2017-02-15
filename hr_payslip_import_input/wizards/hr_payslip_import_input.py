# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api
from openerp.exceptions import Warning as UserError
import base64
import csv
import cStringIO


class HrPayslipImportInput(models.TransientModel):
    _name = "hr.payslip_import_input"
    _description = "HR Payslip Import Input"

    data = fields.Binary('File', required=True)
    name = fields.Char('Filename')
    delimeter = fields.Char('Delimeter', default=',',
                            help='Default delimeter is ","')
    run_id = fields.Many2one(
        string="Payslip Run",
        comodel_name="hr.payslip.run"
    )

    @api.multi
    def _create_imported_line(self, payslip_run):
        obj_imported_line = self.env['hr.payslip_imported_line']
        criteria = [
            ('name', '=', self.name),
            ('run_id', '=', payslip_run.id)
        ]
        imported_line_ids = obj_imported_line.search(criteria)
        if imported_line_ids:
            raise UserError("Cannot import with the same file")
        else:
            val_imported = {
                'name': self.name,
                'run_id': payslip_run.id
            }
            obj_imported_line.create(val_imported)

    @api.multi
    def _create_process_line(self, data, keys, payslip_run):
        obj_employee = self.env['hr.employee']
        obj_payslip_input = self.env['hr.payslip.input']
        obj_payslip = self.env['hr.payslip']
        obj_process_line = self.env['hr.payslip_process_line']
        for i in range(len(data)):
            val_process = {}
            field = data[i]
            values = dict(zip(keys, field))

            employee = obj_employee.search(
                [('identification_id', '=', values['employee'])]
            )
            criteria_payslip = [
                ('employee_id', '=', employee.id),
                ('payslip_run_id', '=', payslip_run.id)
            ]

            payslip = obj_payslip.search(criteria_payslip)
            if payslip.input_line_ids:
                criteria_input = [
                    ('code', '=', values['code']),
                    ('payslip_id', '=', payslip.id)
                ]
                input_line = obj_payslip_input.search(criteria_input)
                input_line.amount = values['amount']
                val_process['input_id'] = input_line.id

            val_process['name'] = self.name
            val_process['employee_code'] = values['employee']
            val_process['input_code'] = values['code']
            val_process['amount'] = values['amount']
            val_process['run_id'] = payslip_run.id
            obj_process_line.create(val_process)

    @api.multi
    def import_data(self):
        # Variable Object
        obj_payslip_run = self.env['hr.payslip.run']

        # Get Payslip Run ID
        ctx = self.env.context
        if 'active_id' in ctx:
            payslip_run = obj_payslip_run.browse(ctx['active_id'])

        # Get Data CSV
        data = base64.b64decode(self.data)
        file_input = cStringIO.StringIO(data)
        file_input.seek(0)
        reader_info = []
        if self.delimeter:
            delimeter = str(self.delimeter)
        else:
            delimeter = ','
        reader = csv.reader(file_input, delimiter=delimeter,
                            lineterminator='\r\n')
        try:
            reader_info.extend(reader)
        except Exception:
            raise UserError("Not a valid file!")
        keys = reader_info[0]
        if not isinstance(keys, list) or ('employee' not in keys or
                                          'code' not in keys or
                                          'amount' not in keys):

            raise UserError(
                "Not 'employee' or 'code' or 'amount' keys found"
            )
        del reader_info[0]

        # Create Imported Line
        self._create_imported_line(payslip_run)

        # Create Process Line
        self._create_process_line(reader_info, keys, payslip_run)
