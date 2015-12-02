# -*- encoding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    This module copyright (C) 2015 Slobodni-programi d.o.o.#    #
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Epps Reseller Module',
    'version': '8.0.1.0.0',
    'author': 'Slobodni-programi d.o.o.',
    'maintainer': 'False',
    'website': 'False',
    'license': '',
    # any module necessary for this one to work correctly
    'depends': [
                'product',
                'epps_project',
    ],
    'external_dependencies': {
        'python': [],
    },

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml # noqa
    # for the full list
    'category': 'EPPS Modules',
    'summary': 'Epps common modules collection install via dependencies',
    'description': """
.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===========
Module name
===========

This module was written to extend the functionality of ... to support ...
and allow you to ...

Installation
============

To install this module, you need to:

 * do this ...

Configuration
=============

To configure this module, you need to:

 * go to ...

Usage
=====

To use this module, you need to:

 * go to ...

.
Known issues / Roadmap
======================

 * ...

Credits
=======

Contributors
------------

* Firstname Lastname <email.address@example.org>

Maintainer
----------


   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.


* Module exported by the Module Prototyper module for version 8.0.
* If you have any questions, please contact Savoir-faire Linux
(support@savoirfairelinux.com)
""",


    # always loaded
    'data': [
             'views/reseller_order_view.xml',
             'views/partner_view.xml',
             'data/reseller_order_sequence.xml',
             'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],

    # used for Javascript Web Client Testing with QUnit / PhantomJS
    # https://www.odoo.com/documentation/8.0/reference/javascript.html#testing-in-odoo-web-client  # noqa
    'js': [],
    'css': [],
    'qweb': [],

    'installable': True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    'auto_install': False,
    'application': False,
}
