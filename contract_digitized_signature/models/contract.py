# Copyright 2017 Tecnativa - Vicent Cubells
# Copyright 2020 Technolibre - Carms Ng
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ContractContract(models.Model):
    _name = "contract.contract"
    _inherit = ["contract.contract", "mail.thread"]

    customer_signature = fields.Binary(
        string="Customer acceptance",
        attachment=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    signature_name = fields.Char(
        string="Signed by", readonly=True, states={"draft": [("readonly", False)]}
    )
    signature_time = fields.Datetime(string="Signed at", readonly=True)

    def _get_default_require_signature(self):
        return self.env.user.company_id.portal_confirmation_sign

    require_signature = fields.Boolean(
        "Online Signature",
        default=_get_default_require_signature,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="If checked, client can accept the contract by signing in the portal.",
    )

    @api.multi
    def action_draft(self):
        super(ContractContract, self).action_draft()
        # Clear Signature
        return self.write({"customer_signature": None, "signature_time": None})

    def has_to_be_signed(self):
        # TODO consider expiration
        return (
            self.state == "draft"
            and self.require_signature
            and (not self.customer_signature)
            and self.active
        )

    @api.model
    def create(self, values):
        contract = super(ContractContract, self).create(values)
        if contract.customer_signature:
            values = {"customer_signature": contract.customer_signature}
            contract._track_signature(values, "customer_signature")
            contract.action_done()
        return contract

    @api.multi
    def write(self, values):
        self._track_signature(values, "customer_signature")
        if values.get("customer_signature") and self.state == "draft":
            self.action_done()
        return super(ContractContract, self).write(values)

    def _track_signature(self, values, field):
        super(ContractContract, self)._track_signature(values, field)
        if field in values:
            if values.get(field):
                self.signature_time = fields.Datetime.now()
