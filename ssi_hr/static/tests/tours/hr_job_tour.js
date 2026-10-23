/* Copyright 2026 OpenSynergy Indonesia
   Copyright 2026 PT. Simetri Sinergi Indonesia
   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("ssi_hr.hr_job_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/hr_job/01-create.md
    tour.register(
        "ssi_hr_hr_job_create",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Flow 1 — Open the Human Resource > Configuration > Organization >
            // Job Positions menu.
            // "Configuration" (level 2) is a section: its step only opens the
            // dropdown. "Organization" (level 3) is a header, so the leaf is
            // clicked directly.
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
                content: "Open the Job Positions menu",
                trigger: '.o_menu_sections [data-menu-xmlid="ssi_hr.hr_job_menu"]',
            },
            {
                content: "Job Positions list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Job Positions)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },
            // ── Flow 2 — Click the New button.
            {
                content: "Click Create",
                trigger: ".o_list_button_add",
                extra_trigger: ".o_list_view",
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
                content: "Enter the job position name",
                trigger: ".o_field_widget[name='name']",
                run: "text TOUR-JOB-CREATE",
            },
            // ── Flow 6 — Click Save.
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
            // ── Post-Condition — The new job position is in Recruitment in
            // Progress status.
            {
                content: "The new job position is shown",
                trigger: ".o_field_widget[name='name']:contains(TOUR-JOB-CREATE)",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "The status is Recruitment in Progress",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='recruit'].btn-primary",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
