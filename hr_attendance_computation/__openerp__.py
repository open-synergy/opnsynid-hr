# -*- coding: utf-8 -*-
# Copyright 2011 Domsense srl (<http://www.domsense.com>)
# Copyright 2011-15 Agile Business Group sagl (<http://www.agilebg.com>)
# Copyright 2017 OpenSynergy Indonesia (<https://opensynergy-indonesia.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Attendance Computation",
    "version": "8.0.1.0.0",
    "category": "Human Resources",
    "summary": "Dynamic reports based on employee's attendances and "
               "contract's calendar",
    "author": "Agile Business Group,"
              "OpenSynergy Indonesia,"
              "Odoo Community Association (OCA)",
    "website": "http://www.agilebg.com",
    "license": "AGPL-3",
    "depends": [
        "hr_attendance",
        "hr_contract",
        "hr_holidays",
    ],
    "data": [
        "views/res_company_views.xml",
        "views/hr_attendance_views.xml",
        "views/resource_calendar_views.xml",
    ],
    "demo": [
        "demo/hr_attendance_demo.xml",
    ],
    "installable": True
}
