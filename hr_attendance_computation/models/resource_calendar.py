# -*- coding: utf-8 -*-
# Copyright 2011 Domsense srl (<http://www.domsense.com>)
# Copyright 2011-15 Agile Business Group sagl (<http://www.agilebg.com>)
# Copyright 2017 OpenSynergy Indonesia (<https://opensynergy-indonesia.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class ResourceCalendar(models.Model):
    _inherit = "resource.calendar"
    attendance_rounding = fields.Selection(
        selection=[
            ("60", "1"),
            ("30", "2"),
            ("20", "3"),
            ("12", "5"),
            ("10", "6"),
            ("7.5", "8"),
            ("6", "10"),
            ("5", "12"),
            ("4", "15"),
            ("3", "20"),
            ("2", "30"),
            ("1", "60"),
        ],
        string="Attendance rounding",
        help="For instance, using rounding = 15 minutes, every sign in "
        "will be rounded to the following quarter hour and every "
        "sign out to the previous quarter hour",
    )
    overtime_rounding = fields.Selection(
        selection=[
            ("60", "1"),
            ("30", "2"),
            ("20", "3"),
            ("12", "5"),
            ("10", "6"),
            ("7.5", "8"),
            ("6", "10"),
            ("5", "12"),
            ("4", "15"),
            ("3", "20"),
            ("2", "30"),
            ("1", "60"),
        ],
        string="Overtime rounding",
        help="Setting rounding = 30 minutes, an overtime of 29 minutes "
        "will be considered as 0 minutes, 31 minutes as 30 minutes, "
        "61 minutes as 1 hour and so on",
    )
    overtime_rounding_tolerance = fields.Float(
        string="Overtime rounding tolerance",
        size=8,
        help="Overtime can be rounded using a tolerance. Using tolerance "
        "= 3 minutes and rounding = 15 minutes, if employee does "
        "overtime of 12 minutes, it will be considered as 15 "
        "minutes.",
    )
    leave_rounding = fields.Selection(
        selection=[
            ("60", "1"),
            ("30", "2"),
            ("20", "3"),
            ("12", "5"),
            ("10", "6"),
            ("7.5", "8"),
            ("6", "10"),
            ("5", "12"),
            ("4", "15"),
            ("3", "20"),
            ("2", "30"),
            ("1", "60"),
        ],
        string="Leave rounding",
        help="On the contrary of overtime rounding, using rounding = 15 "
        "minutes, a leave of 1 minute will be considered as 15 "
        "minutes, 16 minutes as 30 minutes and so on",
    )
