/* Copyright 2017 Laslabs Inc.
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define('contract_portal.tour_test_contract_portal', function (require) {
    'use strict';

    var base = require('web_editor.base');
    var _t = require('web.core')._t;
    var tour = require('web_tour.tour');

    var steps = [
        {
            content: _t('Click on Contracts'),
            trigger: "a:contains('Contracts')",
        },
        {
            content: _t('Click on Demo Contract'),
            trigger: "a:contains('Demo Contract')",
        },
        {
            content: _t('Click Communications'),
            trigger: "a:contains('Communications')",
        },
    ];

    var options = {
        test: true,
        url: '/my/home',
        name: 'Test website portal contract view',
        wait_for: base.ready(),
    };

    tour.register('test_contract_view', options, steps);

    // This element is detached from DOM
    return {};
});
