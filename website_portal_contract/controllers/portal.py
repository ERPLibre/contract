# Copyright 2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import http
from odoo.http import request
from odoo.exceptions import AccessError, MissingError
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
# from odoo.addons.portal.controllers.portal import pager as portal_pager
from odoo.http import request


class CustomerPortal(CustomerPortal):

    def _prepare_portal_layout_values(self):
        values = super(CustomerPortal, self)._prepare_portal_layout_values()

        Contract = request.env['contract.contract']
        contract_count = len(Contract._search_contracts())

        values.update({
            'contract_count': contract_count,
        })
        return values

    @http.route(
        ['/my/contracts', '/my/contracts/page/<int:page>'],
        type='http',
        auth="user",
        website=True,
    )
    def portal_my_contracts(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = self._prepare_portal_layout_values()
        Contract = request.env['contract.contract']
        
        # domain = []

        # TODO: searchbar_sortings

        # count for pager
        # contract_count = len(Contract._search_contracts())
        # pager
        # pager = portal_pager(
        #     url="/my/contracts",
        #     url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
        #     total=contract_count,
        #     page=page,
        #     step=self._items_per_page
        # )

        values.update({
            'user': request.env.user,
            'contracts': Contract._search_contracts(),
        })
        
        return request.render(
            'website_portal_contract.portal_my_contracts',
            values,
        )

    @http.route(
        ["/my/contracts/<int:contract_id>"],
        type='http',
        auth='user',
        website=True
    )
    def portal_my_contract(self, contract_id, report_type=None, access_token=None, message=False, download=False, **kw):
        try:
            contract_sudo = self._document_check_access('contract.contract', contract_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=contract_sudo, report_type=report_type, report_ref='contract.report_contract', download=download)

        # 1. Prepare value
        # contract = request.env["contract.contract"].browse(contract_id)
        values = {
            "contract": contract_sudo,
            'message': message,
            'token': access_token,
            'bootstrap_formatting': True,
            'user': request.env.user,
            'action': request.env.ref('contract.action_customer_contract').id,
        }

        history = request.session.get("my_contracts_history", [])
        values.update(get_records_pager(history, contract_sudo))

        # 2. Render view
        return request.render('website_portal_contract.portal_contract_page', values)


    # @http.route(
    #     ["/contract/template/"
    #      "<model('contract.template'):contract>"],
    #     type='http',
    #     auth='user',
    #     website=True,
    # )
    # def template_view(self, contract, **kwargs):
    #     values = {'template': contract}
    #     return request.render(
    #         'website_portal_contract.website_contract_template',
    #         values,
    #     )