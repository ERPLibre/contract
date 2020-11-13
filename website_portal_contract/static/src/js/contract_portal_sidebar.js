odoo.define('website_portal_contract.ContractPortalSidebar.instance', function (require) {
    "use strict";

    require('web.dom_ready');
    var ContractPortalSidebar = require('website_portal_contract.ContractPortalSidebar');

    if (!$('.o_portal_contract_sidebar').length) {
        return $.Deferred().reject("DOM doesn't contain '.o_portal_contract_sidebar'");
    }

    var contract_portal_sidebar = new ContractPortalSidebar();
    return contract_portal_sidebar.attachTo($('.o_portal_contract_sidebar')).then(function () {
        return contract_portal_sidebar;
    });
});

//==============================================================================

odoo.define('website_portal_contract.ContractPortalSidebar', function (require) {
    "use strict";

    var PortalSidebar = require('portal.PortalSidebar');

    var ContractPortalSidebar = PortalSidebar.extend({
        events: {
            'click .o_portal_contract_print': '_onPrintContract',
        },
        /**
         * @override
         */
        start: function () {
            var self = this;
            this._super.apply(this, arguments);
            var $contractHtml = this.$el.find('iframe#contract_html');
            var updateIframeSize = self._updateIframeSize.bind(self, $contractHtml);
            $contractHtml.on('load', updateIframeSize);
            $(window).on('resize', updateIframeSize);
        },

        //--------------------------------------------------------------------------
        // Handlers
        //--------------------------------------------------------------------------

        /**
         * Called when the iframe is loaded or the window is resized on customer portal.
         * The goal is to expand the iframe height to display the full report without scrollbar.
         *
         * @private
         * @param {object} $el: the iframe
         */
        _updateIframeSize: function ($el) {
            var $wrapwrap = $el.contents().find('div#wrapwrap');
            // Set it to 0 first to handle the case where scrollHeight is too big for its content.
            $el.height(0);
            $el.height($wrapwrap[0].scrollHeight);
        },
        /**
         * @private
         * @param {MouseEvent} ev
         */
        _onPrintContract: function (ev) {
            ev.preventDefault();
            var href = $(ev.currentTarget).attr('href');
            this._printIframeContent(href);
        },
    });


    return ContractPortalSidebar;
});
