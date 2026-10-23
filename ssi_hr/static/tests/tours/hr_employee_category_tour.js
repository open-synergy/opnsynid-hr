/* Copyright 2026 OpenSynergy Indonesia
   Copyright 2026 PT. Simetri Sinergi Indonesia
   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_hr.hr_employee_category_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/hr_employee_category/01-create.md
    tour.register(
        "ssi_hr_hr_employee_category_create",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Flow 1 — Open the Human Resource > Configuration > Employee > Tags
            // menu.
            // "Configuration" (level 2) only opens the dropdown; the level 3
            // "Employee" header is skipped and the leaf is clicked directly.
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Human Resource app",
                trigger: '.o_app[data-menu-xmlid="ssi_hr.menu_root_human_resource"]',
            },
            {
                content: "Open the Configuration menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_hr.menu_human_resource_configuration"]',
            },
            {
                content: "Open the Tags menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_hr.hr_employee_catgeory_menu"]',
            },
            {
                content: "Tags list is displayed",
                trigger: ".o_control_panel .breadcrumb-item.active:contains(Tags)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },
            // ── Flow 2 — Click the New button.
            // The list is editable="bottom": Create adds an editable row.
            {
                content: "Click Create",
                trigger: ".o_list_button_add",
                extra_trigger: ".o_list_view",
            },
            {
                content: "An editable row is added to the list",
                trigger: ".o_list_view .o_selected_row",
                run: function () {
                    // Assertion only.
                },
            },
            // ── Flow 3 — Fill in the required field.
            {
                content: "Enter the tag name",
                trigger: ".o_selected_row .o_field_widget[name='name']",
                run: "text TOUR-TAG-CREATE",
            },
            // ── Flow 4 — Click Save.
            {
                content: "Save the row",
                trigger: ".o_list_button_save",
            },
            // ── Post-Condition — The new tag is listed.
            {
                content: "The new tag is listed",
                trigger:
                    ".o_list_view .o_data_row:not(.o_selected_row) .o_data_cell:contains(TOUR-TAG-CREATE)",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
