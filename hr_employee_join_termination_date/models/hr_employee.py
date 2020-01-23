# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models, fields
import logging
_logger = logging.getLogger(__name__)

try:
    import pandas as pd
    import numpy as np
except (ImportError, IOError) as err:
    _logger.debug(err)


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.multi
    @api.depends(
        "date_join",
        "date_termination",
    )
    def _compute_work_longetivity(self):
        for document in self:
            year_work = month_work = 0
            if document.date_join and document.date_termination:
                dt_join =\
                    pd.to_datetime(document.date_join)
                dt_termination =\
                    pd.to_datetime(document.date_termination)

                dt_year_work = (dt_termination - dt_join)
                year_work =\
                    int(dt_year_work / np.timedelta64(1, "Y"))
                dt_temp_year = dt_join + pd.DateOffset(years=year_work)

                dt_month_work = (dt_termination - dt_temp_year)
                month_work =\
                    int(dt_month_work / np.timedelta64(1, "M"))

            document.year_work_longetivity = year_work
            document.month_work_longetivity = month_work

    date_join = fields.Date(
        string="Join Date",
    )
    date_termination = fields.Date(
        string="Termination Date",
    )
    year_work_longetivity = fields.Integer(
        string="Year Work Longetivity",
        compute="_compute_work_longetivity",
        store=True,
    )
    month_work_longetivity = fields.Integer(
        string="Month Work Longetivity",
        compute="_compute_work_longetivity",
        store=True,
    )
