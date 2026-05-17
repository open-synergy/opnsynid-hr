# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class ResCompany(models.Model):
    """
    Extends res.company as a base hook for ssi_hr company-level configuration.
    """

    _name = "res.company"
    _inherit = "res.company"
