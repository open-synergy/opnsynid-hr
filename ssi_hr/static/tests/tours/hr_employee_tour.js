/* Copyright 2026 OpenSynergy Indonesia
   Copyright 2026 PT. Simetri Sinergi Indonesia
   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_hr.hr_employee_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/hr_employee/01-create.md
    tour.register(
        "ssi_hr_hr_employee_create",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Flow 1 — Open the Human Resource > Employees menu.
            // Employees is the landing menu of the Human Resource app, so the
            // click reloads the same action: the control panel is marked first
            // and the gate waits for the unmarked (re-mounted) one.
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Human Resource app",
                trigger: '.o_app[data-menu-xmlid="ssi_hr.menu_root_human_resource"]',
            },
            {
                content: "Open the Employees menu",
                trigger: '.o_menu_sections [data-menu-xmlid="ssi_hr.hr_employee_menu"]',
                run: function (actions) {
                    // Instrumentation marker, destroyed with the old controller.
                    $(".o_control_panel").addClass("oe_tour_stale");
                    actions.click();
                },
            },
            {
                content: "Employees kanban is displayed",
                trigger: ".o_control_panel:not(.oe_tour_stale)",
                extra_trigger: ".o_kanban_view",
                run: function () {
                    // Assertion only.
                },
            },
            // ── Flow 2 — Click the New button.
            // Employees lands on kanban, so the Create button is the kanban
            // controller's own ".o-kanban-button-new" (note the HYPHEN).
            {
                content: "Click Create",
                trigger: ".o-kanban-button-new",
                extra_trigger: ".o_kanban_view",
            },
            {
                content: "Form is open in edit mode",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only.
                },
            },
            // ── Flow 3 — Fill in the required field.
            {
                content: "Enter the employee name",
                trigger: ".o_field_widget[name='name']",
                run: "text Tour Employee Create",
            },
            // ── Flow 5 — Click Save.
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only.
                },
            },
            // ── Post-Condition — The employee exists and Initials is shown.
            {
                content: "The new employee is shown",
                trigger: ".o_field_widget[name='name']:contains(Tour Employee Create)",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "The Initials field is shown",
                trigger: ".o_field_widget[name='initials']",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
