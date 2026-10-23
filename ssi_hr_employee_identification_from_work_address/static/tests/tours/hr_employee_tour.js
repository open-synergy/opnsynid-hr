odoo.define(
    "ssi_hr_employee_identification_from_work_address.hr_employee_tour",
    function (require) {
        "use strict";

        var tour = require("web_tour.tour");

        // ═══════════════════════════════════════════════════════════════
        // IK: docs/hr_employee/02-edit.md
        // Delta-only: navigation comes from the base work instruction of
        // ssi_hr (Flow steps 1-2); only the ID Numbers tab and the hidden
        // Identification No / Passport No fields are asserted.
        // ═══════════════════════════════════════════════════════════════
        tour.register(
            "ssi_hr_employee_identification_from_work_address_hr_employee_edit",
            {
                test: true,
                url: "/web",
            },
            [
                // ── Base Flow 1 — Open the Human Resource > Employees menu.
                tour.stepUtils.showAppsMenuItem(),
                {
                    content: "Open the Human Resource app",
                    trigger:
                        '.o_app[data-menu-xmlid="ssi_hr.menu_root_human_resource"]',
                },
                {
                    content: "Open the Employees menu",
                    trigger:
                        '.o_menu_sections [data-menu-xmlid="ssi_hr.hr_employee_menu"]',
                },
                {
                    // Gate: the target action's breadcrumb (the landing action of
                    // the app is also a list/kanban view).
                    content: "Employees kanban is displayed",
                    trigger:
                        ".o_control_panel .breadcrumb-item.active:contains(Employees)",
                    extra_trigger: ".o_kanban_view",
                    run: function () {
                        // Assertion only; do not trigger the default click action.
                    },
                },
                // ── Base Flow 2 — Open the employee record.
                {
                    content: "Open the employee record",
                    trigger:
                        ".o_kanban_record:contains(TOUR-IDENTIFICATION-EMPLOYEE-UI)",
                },
                // ── Additional Fields — the ID Numbers tab is displayed.
                {
                    content: "Click the ID Numbers tab",
                    trigger: ".o_notebook .nav-link:contains(ID Numbers)",
                    extra_trigger: ".o_form_view",
                },
                {
                    content: "ID Numbers tab is displayed",
                    trigger: ".o_notebook .tab-pane.active .o_field_one2many",
                    run: function () {
                        // Assertion only; do not trigger the default click action.
                    },
                },
                // ── Removed / Relaxed — Identification No and Passport No are hidden.
                {
                    content: "Click the Private Information tab",
                    trigger: ".o_notebook .nav-link:contains(Private Information)",
                },
                {
                    content: "Identification No and Passport No are not displayed",
                    trigger:
                        ".o_notebook .tab-pane.active .o_horizontal_separator:contains(Citizenship)",
                    run: function () {
                        // Assertion only: the visible fields of this tab must not
                        // include the hidden core fields.
                        var $hidden = $(
                            ".o_notebook .tab-pane.active " +
                                ".o_field_widget[name='identification_id']:visible," +
                                ".o_notebook .tab-pane.active " +
                                ".o_field_widget[name='passport_id']:visible"
                        );
                        if ($hidden.length) {
                            throw new Error(
                                "Identification No / Passport No must be hidden"
                            );
                        }
                    },
                },
            ]
        );
    }
);
