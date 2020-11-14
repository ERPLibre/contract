# Copyright 2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ContractContract(models.Model):
    _name = "contract.contract"
    _inherit = ["contract.contract", "portal.mixin"]

    website_template_id = fields.Many2one(
        string="Website Template",
        comodel_name="contract.website.template",
        help="Website layout for contract",
    )

    def _compute_access_url(self):
        super(ContractContract, self)._compute_access_url()
        for contract in self:
            contract.access_url = "/my/contracts/%s" % contract.id

    @api.multi
    def _get_report_base_filename(self):
        self.ensure_one()
        return "Contract Report - %s" % self.name
