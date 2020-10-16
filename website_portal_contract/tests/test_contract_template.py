# Copyright 2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import HttpCase


class TestContractTemplate(HttpCase):
    def setUp(self):
        super(TestContractTemplate, self).setUp()
        self.contract_mod = self.env["contract.template"]
        self.template = self.env.ref(
            "website_portal_contract.website_contract_template_default"
        )

    def test_get_default_template(self):
        """ Test get_default_template returns correct template """
        self.assertEquals(self.contract_mod._get_default_template(), self.template)
