# Copyright 2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Contract Portal",
    "summary": "Extends portal with contracts",
    "version": "12.0.1.0.0",
    "category": "Contract Management",
    "website": "https://laslabs.com",
    "author": "LasLabs, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["contract", "contract_digitized_signature"],
    "data": [
        "security/ir.model.access.csv",
        "data/website_contract_template_data.xml",
        "views/contract.xml",
        "views/contract_template.xml",
        "views/contract_website_template.xml",
        "views/contract_portal_templates.xml",
        "views/assets.xml",
    ],
    "demo": ["demo/contract_demo.xml", "demo/assets_demo.xml"],
}
