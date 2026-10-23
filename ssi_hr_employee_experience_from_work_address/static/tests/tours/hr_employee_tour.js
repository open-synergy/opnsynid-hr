odoo.define("ssi_hr_employee_experience_from_work_address.hr_employee_tour", function (
    require
) {
    "use strict";

    var tour = require("web_tour.tour");

    // ═══════════════════════════════════════════════════════════════
    // IK: docs/hr_employee/02-edit.md
    // Delta-only: navigation comes from the base work instruction of
    // ssi_hr (Flow steps 1-2); only the Experiences tab is asserted.
    // ═══════════════════════════════════════════════════════════════
    tour.register(
        "ssi_hr_employee_experience_from_work_address_hr_employee_edit",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Base Flow 1 — Open the Human Resource > Employees menu.
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Human Resource app",
                trigger: '.o_app[data-menu-xmlid="ssi_hr.menu_root_human_resource"]',
            },
            {
                content: "Open the Employees menu",
                trigger: '.o_menu_sections [data-menu-xmlid="ssi_hr.hr_employee_menu"]',
            },
            {
                // Gate: the target action's breadcrumb (the landing action of the
                // app is also a list/kanban view).
                content: "Employees kanban is displayed",
                trigger: ".o_control_panel .breadcrumb-item.active:contains(Employees)",
                extra_trigger: ".o_kanban_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            // ── Base Flow 2 — Open the employee record.
            {
                content: "Open the employee record",
                trigger: ".o_kanban_record:contains(TOUR-EXPERIENCE-EMPLOYEE-UI)",
            },
            // ── Additional Fields — the Experiences tab is displayed.
            {
                content: "Click the Experiences tab",
                trigger: ".o_notebook .nav-link:contains(Experiences)",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Academics list is displayed",
                trigger:
                    ".o_notebook .tab-pane.active .o_horizontal_separator:contains(Academics)",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Certifications list is displayed",
                trigger:
                    ".o_notebook .tab-pane.active .o_horizontal_separator:contains(Certifications)",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Professional Experiences list is displayed",
                trigger:
                    ".o_notebook .tab-pane.active .o_horizontal_separator:contains(Professional Experiences)",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );
});
