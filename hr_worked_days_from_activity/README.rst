.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===================================
Worked Days From Timesheet Activity
===================================

This module add capability on payslip to import worked days from
timesheet activities. This functionality will be useful for salary rule
that use man hour from timesheet activity as multiplier.

Installation
============

To install this module, you need to:

* clone the branch 8.0 of the repository https://github.com/open-synergy/opnsynid-hr
* add the path to this repository in your configuration (addons-path)
* update the module list
* search for "Worked Days From Timesheet Activity" in your addons
* install the module

Configuration
=============

To configure which timesheet activity that will be imported, you need to:

1. Go to *Human Resources -> Configuration -> Payroll -> Salary Rule*
2. Open a salary rule data
3. Select analytic account on *Timesheet Account* tab

Usage
=====

To import timesheet activity into payslip worked days, you need to:

1. Open payslip with draft status
2. Make sure you have properly configure which analytic account you would like to import
3. Click *Import From Timesheet Activity* button

Odoo will create one worked days per salary rule that has timesheet account(s). Number of hours
will be computed from sum of all timesheet activites that belong to that salary rule.

Known issues / Roadmap
======================

* No multi action

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/open-synergy/opnsynid-hr/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed `feedback
<https://github.com/open-synergy/
opnsynid-hr/issues/new?body=module:%20
hr_worked_days_from_activity%0Aversion:%20
8.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Credits
=======

Contributors
------------

* Andhitia Rama <andhitia.r@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id.com

This module is maintained by the PT. Simetri Sinergi Indonesia.
