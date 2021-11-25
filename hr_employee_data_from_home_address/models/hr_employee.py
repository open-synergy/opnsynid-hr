# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    title = fields.Many2one(
        string="Title",
        comodel_name="res.partner.title",
        related="address_home_id.title",
        store=True,
    )
    bank_ids = fields.One2many(
        string="Bank Accounts",
        comodel_name="res.partner.bank",
        related="address_home_id.bank_ids",
        store=False,
    )
    home_street = fields.Char(
        string="Street",
        related="address_home_id.street",
        store=True,
    )
    home_street2 = fields.Char(
        string="Street2",
        related="address_home_id.street2",
        store=True,
    )
    home_zip = fields.Char(
        string="ZIP",
        related="address_home_id.zip",
        store=True,
    )
    home_city = fields.Char(
        string="City",
        related="address_home_id.city",
        store=True,
    )
    home_state_id = fields.Many2one(
        string="State",
        comodel_name="res.country.state",
        related="address_home_id.state_id",
        store=True,
    )
    home_country_id = fields.Many2one(
        string="Country",
        comodel_name="res.country",
        related="address_home_id.country_id",
        store=True,
    )
    home_email = fields.Char(
        string="Email",
        related="address_home_id.email",
        store=True,
    )
    home_phone = fields.Char(
        string="Phone",
        related="address_home_id.phone",
        store=True,
    )
    home_mobile = fields.Char(
        string="Mobile",
        related="address_home_id.mobile",
        store=True,
    )
    home_fax = fields.Char(
        string="Fax",
        related="address_home_id.fax",
        store=True,
    )
