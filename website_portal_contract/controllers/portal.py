# Copyright 2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import http, _
from odoo.http import request
from odoo.exceptions import AccessError, MissingError
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
# from odoo.addons.portal.controllers.portal import pager as portal_pager
from odoo.http import request


class CustomerPortal(CustomerPortal):

    def _prepare_portal_layout_values(self):
        values = super(CustomerPortal, self)._prepare_portal_layout_values()

        Contract = request.env['contract.contract']
        contract_count = Contract.search_count(self._prepare_contracts_domain())

        values.update({
            'contract_count': contract_count,
        })
        return values

    def _prepare_contracts_domain(self):
        partner = request.env.user.partner_id
        return [
            ("partner_id", "child_of", [partner.commercial_partner_id.id]),
        ]

    def _contract_get_page_view_values(self, contract, access_token, **kwargs):
        values = {
            'contract': contract,
            'invoices': contract._get_related_invoices(),
            'page_name': 'contract',
        }
        # if access_token:
        #     values['no_breadcrumbs'] = True
        #     values['access_token'] = access_token

        # if kwargs.get('error'):
        #     values['error'] = kwargs['error']
        # if kwargs.get('warning'):
        #     values['warning'] = kwargs['warning']
        # if kwargs.get('success'):
        #     values['success'] = kwargs['success']

        # history = request.session.get('my_contract_history', [])
        # values.update(get_records_pager(history, contract))

        return self._get_page_view_values(
            contract, access_token, values, 'my_contracts_history', False, **kwargs)

    @http.route(
        ['/my/contracts', '/my/contracts/page/<int:page>'],
        type='http', 
        auth="user",
        website=True,
    )
    def portal_my_contracts(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = self._prepare_portal_layout_values()
        Contract = request.env['contract.contract']
        
        domain = self._prepare_contracts_domain()

        searchbar_sortings = {
            'name': {'label': _('Contract Name'), 'order': 'name desc'},
            'active': {'label': _('Status'), 'order': 'active desc'},
            'invdate': {'label': _('Next Invoice Date'), 'order': 'recurring_next_date desc'},
        }
        # default sort by order
        if not sortby:
            sortby = 'invdate'
        order = searchbar_sortings[sortby]['order']

        archive_groups = self._get_archive_groups('contract.contract', domain)
        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]

        # count for pager
        contract_count = Contract.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/contracts",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
            total=contract_count,
            page=page,
            step=self._items_per_page
        )
        # content according to pager and archive selected
        contracts = Contract.search(
            domain, order=order, limit=self._items_per_page, offset=pager["offset"]
        )
        request.session['my_contracts_history'] = contracts.ids[:100]

        values.update({
            'user': request.env.user,
            'contracts': contracts,
            "pager": pager,
            "default_url": "/my/contracts",
            "page_name": "contract",
            "report_type": "html",
            'action': request.env.ref('contract.action_customer_contract').id,
            'archive_groups': archive_groups,
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })
        return request.render('website_portal_contract.portal_my_contracts', values)

    @http.route(
        ["/my/contracts/<int:contract_id>"],
        type='http',
        auth='user',
        website=True
    )
    def portal_my_contract_detail(self, contract_id, report_type=None, access_token=None, message=False, download=False, **kw):
        try:
            contract_sudo = self._document_check_access('contract.contract', contract_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=contract_sudo, report_type=report_type, report_ref='contract.report_contract', download=download)

        # Prepare value
        values = self._contract_get_page_view_values(contract_sudo, access_token, **kw)

        # Render view
        return request.render('website_portal_contract.portal_contract_page', values)

    def _get_contract_report_name(self):
        return ('contract.'
                'report_contract')

    @http.route(
        ['/my/contracts/pdf/<int:contract_id>'],
        type='http', 
        auth="public", 
        website=True
    )
    def portal_my_contract_report(self, contract_id, access_token=None, **kw):
        try:
            contract_sudo = self._document_check_access('contract.contract', contract_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        # print report as sudo
        pdf = request.env.ref(self._get_contract_report_name())\
            .sudo().render_qweb_pdf([contract_sudo.id])[0]
        pdfhttpheaders = [
            ('Content-Type', 'application/pdf'),
            ('Content-Length', len(pdf)),
        ]
        return request.make_response(pdf, headers=pdfhttpheaders)


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