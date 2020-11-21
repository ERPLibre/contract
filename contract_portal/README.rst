===============
Contract Portal
===============

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fcontract-lightgray.png?logo=github
    :target: https://github.com/OCA/contract/tree/12.0/contract
    :alt: OCA/contract
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/contract-12-0/contract-12-0-contract
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runbot-Try%20me-875A7B.png
    :target: https://runbot.odoo-community.org/runbot/110/12.0
    :alt: Try me on Runbot

|badge1| |badge2| |badge3| |badge4| |badge5| 

This module is an extension of contract and portal that allows contracts to
be shown in the client portal. Each contract now has a website template tied to it.

Usage
=====

`v10.0 Usage Video <https://youtu.be/PSulRVdh4C4>`_

To edit the website template, go to:

* `Invoicing` in the top navigation.
* `Contracts` => `Website Templates`.
* When viewing a template in form view, click `View Template`.
  This will direct you to an edit page of the template in website if
  your user has edit permissions.

To view the live template in `My Account` in website, assign the template
to a contract and go to:

* `Website`
* Click on your username then select `My Account` in the dropdown.
* Click `Contracts`, then the relevant contract. Your template will show under
  the `Contract` section header, which is also shown in the edit template view for reference.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/110/10.0

Known Issues / Roadmap
======================

* Add token access to controller - Done
* Add functionality to print contracts in website portal - Done
* Add functionality to accept and sign
* integrate with mail template

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/contract/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/OCA/contract/issues/new?body=module:%20contract%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.


Credits
=======

Authors
~~~~~~~

* LasLabs

Contributors
~~~~~~~~~~~~

* Brett Wood <bwood@laslabs.com>
* Carms Ng <carms.ng@technolibre.ca>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/contract <https://github.com/OCA/contract/tree/12.0/contract>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
