.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===========================
Worked Days From Attendance
===========================

This module adds functionality to import attendance into payslip 
worked days computation

Installation
============

To install this module, you need to:

1.  Clone the branch 8.0 of the repository https://github.com/open-synergy/opnsynid-hr
2.  Add the path to this repository in your configuration (addons-path)
3.  Update the module list
4.  Go to menu *Setting -> Modules -> Local Modules*
5.  Search For *Worked Days From Attendance*
6.  Install the module

Configuration
=============

No configuration needed

Usage
=====

To import attendance into payslip you have to:

1. Go to *Human Resources -> Payroll -> Employee Payslip*
2. Open payslip data
3. Click *Import From Attendance* button

Odoo will import *one* worked days computation with *ATTN* code. That
computation is computed from *Timesheet By Period* thats match payslip
period

Known issues / Roadmap
======================


Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/open-synergy/opnsynid-hr/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed `feedback
<https://github.com/open-synergy/
opnsynid-hr/issues/new?body=module:%20
hr_worked_days_from_attendance%0Aversion:%20
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
