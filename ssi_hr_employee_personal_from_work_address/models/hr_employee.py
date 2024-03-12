# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    blood_type = fields.Selection(
        string="Blood Type (ABO)",
        related="address_home_id.blood_type",
        readonly=False,
    )
    blood_type_rhesus = fields.Selection(
        string="Blood Type (Rh)",
        related="address_home_id.blood_type_rhesus",
        readonly=False,
    )
    religion_id = fields.Many2one(
        string="Religion",
        comodel_name="res_partner_religion",
        related="address_home_id.religion_id",
        readonly=False,
    )
    ethnicity_id = fields.Many2one(
        string="Ethnicity",
        comodel_name="res_partner_ethnicity",
        related="address_home_id.ethnicity_id",
        readonly=False,
    )
    nationality_id = fields.Many2one(
        string="Nationality",
        comodel_name="res.country",
        related="address_home_id.nationality_id",
        readonly=False,
    )
    gender = fields.Selection(
        string="Gender",
        related="address_home_id.gender",
        readonly=False,
    )
    birthdate_date = fields.Date(
        string="Birthdate",
        related="address_home_id.birthdate_date",
        readonly=False,
    )
    birth_city = fields.Char(
        string="Birth city",
        related="address_home_id.birth_city",
        readonly=False,
    )
    birth_state_id = fields.Many2one(
        string="Birth state",
        comodel_name="res.country.state",
        related="address_home_id.birth_state_id",
        readonly=False,
    )
    birth_country_id = fields.Many2one(
        string="Birth country",
        comodel_name="res.country",
        related="address_home_id.birth_country_id",
        readonly=False,
    )
