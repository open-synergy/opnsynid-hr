# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrJob(models.Model):
    _name = "hr.job"
    _inherit = ["hr.job"]

    @api.multi
    @api.depends(
        "recruitment_request_ids",
        "recruitment_request_ids.state",
    )
    def _compute_recruitment_request(self):
        for job in self:
            active_requests = job.recruitment_request_ids.filtered(
                lambda r: r.state == "open")
            num_rec = 0
            for active_request in active_requests:
                num_rec += active_request.num_of_request
            job.no_of_recruitment = num_rec
            job.num_active_recruitment_request = len(active_requests)

    recruitment_request_ids = fields.One2many(
        string="Recruitment Requests",
        comodel_name="hr.recruitment_request",
        inverse_name="job_id",
    )
    num_active_recruitment_request = fields.Integer(
        string="Num. of Active Recruitment Request",
        compute="_compute_recruitment_request",
        store=False,
    )
    no_of_recruitment = fields.Integer(
        compute="_compute_recruitment_request",
        store=True,
        readonly=True,
    )
