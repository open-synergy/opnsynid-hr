# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
import datetime

from babel.dates import format_date


class Parser:
    def __init__(self, env, document):
        self.env = env
        self.document = document
        self.current_date = datetime.datetime.now()

    def ttd(self, locale, record=None):
        if record:
            city = record.company_id and record.company_id.city or ""
        else:
            city = self.document.company_id and self.document.company_id.city or ""
        tanggal = format_date(self.current_date, format="d MMMM y", locale=locale)
        return city + ", " + tanggal
