odoo.define("ssi_hr_employee_personal_from_work_address.hr_employee_tour", function (
    require
) {
    "use strict";

    var tour = require("web_tour.tour");

    // ═══════════════════════════════════════════════════════════════
    // IK: docs/hr_employee/15-add-child.md
    // ═══════════════════════════════════════════════════════════════
    tour.register(
        "ssi_hr_employee_personal_from_work_address_hr_employee_add_child",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Flow 1 — Open the Human Resource > Employees menu.
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
            // ── Flow 2 — Open the employee record.
            {
                content: "Open the employee record",
                trigger: ".o_kanban_record:contains(TOUR-CHILD-EMPLOYEE-UI)",
            },
            // ── Flow 3 — Click the Private Information tab.
            {
                content: "Click the Private Information tab",
                trigger: ".o_notebook .nav-link:contains(Private Information)",
                extra_trigger: ".o_form_view",
            },
            // ── Flow 4 — Click the Add Child button.
            {
                content: "Click the Add Child button",
                trigger: ".o_form_view button[name='action_add_child']",
                extra_trigger: ".o_form_view",
            },
            // ── Flow 5 — Fill in the wizard.
            {
                content: "Fill in Name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".modal-footer button[name='action_add_child']",
                run: "text TOUR-CHILD-NAME-UI",
            },
            {
                content: "Fill in Place of Birth",
                trigger: ".o_field_widget[name='birth_city']",
                extra_trigger: ".modal-footer button[name='action_add_child']",
                run: "text Bandung",
            },
            // ── Flow 6 — Click Add Child in the wizard footer.
            {
                content: "Click Add Child in the wizard",
                trigger: ".modal-footer button[name='action_add_child']",
            },
            // ── Post-Condition — the child is listed on the Private
            // Information tab.
            {
                content: "The child is listed in the Children list",
                trigger:
                    ".o_field_widget[name='children_ids'] .o_data_row:contains(TOUR-CHILD-NAME-UI)",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );
});
