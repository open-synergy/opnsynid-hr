# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=C8101
{
    "name": "Human Resource",
    "version": "14.0.3.3.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "auto_install": False,
    "depends": [
        "configuration_helper",
        "ssi_py3o",
        "ssi_hr_employee_language_from_work_address",
        "ssi_hr_employee_experience_from_work_address",
        "ssi_hr_employee_identification_from_work_address",
        "ssi_hr_employee_personal_from_work_address",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "menu.xml",
        "reports/report.xml",
        "views/res_config_settings_views.xml",
        "views/hr_employee_views.xml",
    ],
    "post_init_hook": "post_init_hook",
    "demo": [],
}
