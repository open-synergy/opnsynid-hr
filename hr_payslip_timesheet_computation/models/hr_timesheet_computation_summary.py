# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields
from openerp import tools


class HrTimesheetComputationSummary(models.Model):
    _name = "hr.timesheet_computation_summary"
    _description = "Timesheet Computation Summary"
    _auto = False

    payslip_id = fields.Many2one(
        string="# Payslip",
        comodel_name="hr.payslip",
    )
    item_id = fields.Many2one(
        string="Computation Item",
        comodel_name="hr.timesheet_computation_item",
        required=True,
    )
    amount = fields.Float(
        string="Computation Result",
        required=True,
    )

    def _select(self):
        select_str = """
            SELECT
                row_number() OVER() AS id,
                b.payslip_id AS payslip_id,
                c.item_id as item_id,
                SUM(c.amount) as amount
        """
        return select_str

    def _from(self):
        from_str = """
            FROM
                hr_payslip a
        """
        return from_str

    def _join(self):
        join_str = """
            JOIN
                rel_payslip_2_timesheet_computation AS b ON a.id=b.payslip_id
            JOIN
                hr_timesheet_computation AS c ON b.computation_id=c.id
        """
        return join_str

    def _group_by(self):
        group_by_str = """
            GROUP BY
                b.payslip_id,c.item_id
        """
        return group_by_str

    def _order_by(self):
        order_by_str = """
            ORDER BY
                b.payslip_id
        """
        return order_by_str

    def init(self, cr):
        tools.drop_view_if_exists(cr, self._table)
        cr.execute("""CREATE or REPLACE VIEW %s as (
            %s
            %s
            %s
            %s
            %s
            )""" % (
            self._table,
            self._select(),
            self._from(),
            self._join(),
            self._group_by(),
            self._order_by()))
