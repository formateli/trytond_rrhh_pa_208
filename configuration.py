#This file is part of tryton-rrhh project. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.pyson import Eval
from trytond.pool import Pool
from trytond.model import (
    ModelSingleton, ModelView, ModelSQL, fields)
from trytond.transaction import Transaction
from decimal import Decimal

__all__ = ['Configuration']


class Configuration(ModelSingleton, ModelSQL, ModelView):
    "RRHH Panama 208 Configuration"
    __name__ = 'rrhh.pa.208.configuration'

    horas_base = fields.Numeric('Horas base',
        digits=(16, Eval('currency_digits', 2)),
        depends=['currency_digits'])
    currency_digits = fields.Function(fields.Integer('Currency Digits'),
        'get_currency_digits')

    @staticmethod
    def default_horas_base():
        return Decimal('208')

    @staticmethod
    def default_currency_digits():
        Company = Pool().get('company.company')
        company = Transaction().context.get('company')
        if company:
            company = Company(company)
            return company.currency.digits
        return 2

    def get_currency_digits(self, name=None):
        return self.default_currency_digits()
