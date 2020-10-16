# Copyright 2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import HttpCase


class TestContract(HttpCase):
    def setUp(self):
        super(TestContract, self).setUp()
        self.account = self.env.ref(
            "website_portal_contract.contract_1"
        )
        self.contract = self.env.ref(
            "website_portal_contract.contract_template_1"
        )

    def test_website_template_id(self):
        """ Test website_template_id inherited from contract """
        self.assertEquals(
            self.account.website_template_id, self.contract.website_template_id
        )

    def test_search_contracts(self):
        """ Test returns correct contracts """
        self.account.partner_id = self.env.ref("base.partner_root")
        self.assertIn(
            self.account, self.env["contract.contract"]._search_contracts()
        )
