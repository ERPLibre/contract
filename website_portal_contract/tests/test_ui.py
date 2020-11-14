# Copyright 2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import odoo.tests


@odoo.tests.tagged("post_install", "-at_install")
class TestUi(odoo.tests.HttpCase):
    def test_portal_contract_view_tour(self):
        self.phantom_js(
            "/my/home",
            "odoo.__DEBUG__.services['web_tour.tour'].run('test_contract_view')",
            "odoo.__DEBUG__.services['web_tour.tour'].tours.test_contract_view.ready",
            login="portal",
        )
