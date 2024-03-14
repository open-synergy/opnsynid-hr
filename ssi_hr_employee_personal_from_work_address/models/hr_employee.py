# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    country_id = fields.Many2one(
        comodel_name="res.country",
        related="address_home_id.nationality_id",
        readonly=False,
        store=True,
    )
    gender = fields.Selection(
        related="address_home_id.gender",
        readonly=False,
        store=True,
    )
    birthday = fields.Date(
        related="address_home_id.birthdate_date",
        readonly=False,
        store=True,
    )
    place_of_birth = fields.Char(
        related="address_home_id.birth_city",
        readonly=False,
        store=True,
    )
    country_of_birth = fields.Many2one(
        comodel_name="res.country",
        related="address_home_id.birth_country_id",
        readonly=False,
        store=True,
    )
    birth_state_id = fields.Many2one(
        string="Birth state",
        comodel_name="res.country.state",
        related="address_home_id.birth_state_id",
        readonly=False,
        store=True,
    )
    blood_type = fields.Selection(
        string="Blood Type (ABO)",
        related="address_home_id.blood_type",
        readonly=False,
        store=True,
    )
    blood_type_rhesus = fields.Selection(
        string="Blood Type (Rh)",
        related="address_home_id.blood_type_rhesus",
        readonly=False,
        store=True,
    )
    religion_id = fields.Many2one(
        string="Religion",
        comodel_name="res_partner_religion",
        related="address_home_id.religion_id",
        readonly=False,
        store=True,
    )
    ethnicity_id = fields.Many2one(
        string="Ethnicity",
        comodel_name="res_partner_ethnicity",
        related="address_home_id.ethnicity_id",
        readonly=False,
        store=True,
    )
