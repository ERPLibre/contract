# Copyright 2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models
from odoo.tools.translate import html_translate


class ContractWebsiteTemplate(models.Model):
    _name = "contract.website.template"
    _description = "Contract Website Templates"

    name = fields.Char(help="Template name")
    website_description = fields.Html(
        string="Description", translate=html_translate, sanitize_attributes=False
    )
    contract_id = fields.Many2one(
        string="Contract",
        comodel_name="contract.contract",
        inverse_name="website_template_id",
    )
    contract_template_id = fields.One2many(
        string="Contract Template",
        comodel_name="contract.template",
        inverse_name="website_template_id",
    )
