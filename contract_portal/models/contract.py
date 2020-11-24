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

    def _get_default_require_signature(self):
        return self.env.user.company_id.portal_confirmation_sign

    require_signature = fields.Boolean(
        "Online Signature",
        default=_get_default_require_signature,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="If checked, client can accept the contract by signing in the portal.",
    )

    state = fields.Selection(
        [("draft", "Draft"), ("done", "Locked"), ("cancel", "Cancelled")],
        default="draft",
        track_visibility="always",
    )

    def has_to_be_signed(self):
        # TODO consider expiration
        return (
            self.state == "draft"
            and self.require_signature
            and (not self.customer_signature)
            and self.active
        )

    def _compute_access_url(self):
        super(ContractContract, self)._compute_access_url()
        for contract in self:
            contract.access_url = "/my/contracts/%s" % contract.id

    @api.multi
    def _get_report_base_filename(self):
        self.ensure_one()
        return "Contract Report - %s" % self.name

    @api.multi
    def action_done(self):
        return self.write({"state": "done"})

    @api.multi
    def action_cancel(self):
        return self.write({"state": "cancel"})

    @api.multi
    def preview_contract(self):
        """Invoked when 'Preview' button in contract form view is clicked."""
        self.ensure_one()
        return {
            "type": "ir.actions.act_url",
            "target": "self",
            "url": self.get_portal_url(),
        }
