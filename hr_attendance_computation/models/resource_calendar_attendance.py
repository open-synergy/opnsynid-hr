# -*- coding: utf-8 -*-
# Copyright 2011 Domsense srl (<http://www.domsense.com>)
# Copyright 2011-15 Agile Business Group sagl (<http://www.agilebg.com>)
# Copyright 2017 OpenSynergy Indonesia (<https://opensynergy-indonesia.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class ResourceCalendarAttendance(models.Model):
    _inherit = "resource.calendar.attendance"
    tolerance_from = fields.Float(
        'Tolerance from',
        size=8,
        help='Sign out done in the interval "Work to - Tolerance from" '
        'will be considered done at "Work to"',
    )
    tolerance_to = fields.Float(
        'Tolerance to',
        size=8,
        help='Sign in done in the interval "Work from + Tolerance to" '
        'will be considered done at "Work from"',
    )
