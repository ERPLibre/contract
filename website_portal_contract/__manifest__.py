# Copyright 2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Website Portal Contract",
    "summary": "Extends website portal with contracts.",
    "version": "12.0.1.0.0",
    "category": "Contract Management",
    "website": "https://laslabs.com",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    # 10.0 depends on "contract", "contract_show_invoice", "website_quote"
    "depends": [
        "contract",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/website_contract_template_data.xml",
        "views/contract.xml",
        "views/contract_template.xml",
        "views/contract_website_template.xml",
        "views/contract_portal_templates.xml",
        "views/assets.xml",
    ],
    "demo": [
        # Load order must be `contract => account => invoice line`
        "demo/contract_template_demo.xml",
        "demo/contract_demo.xml",
        "demo/account_invoice_line_demo.xml",
        "demo/assets_demo.xml",
    ],
}
