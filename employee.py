#This file is part of tryton-rrhh project. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.model import fields
from trytond.transaction import Transaction
from trytond.pyson import Eval
from decimal import Decimal

__all__ = ['Employee']


class Employee:
    __metaclass__ = PoolMeta
    __name__ = 'company.employee'
  
    salario = fields.Numeric('Salario',
        digits=(16, Eval('currency_digits', 2)),
        depends=['currency_digits'])
    horas_base = fields.Function(fields.Numeric('Horas base',
        digits=(16, Eval('currency_digits', 2)),
        depends=['currency_digits']), 'get_horas_base')
    rata = fields.Function(fields.Numeric('Rata',
        digits=(16, Eval('currency_digits', 2)),
        depends=['currency_digits']), 'on_change_with_rata')
    currency_digits = fields.Function(fields.Integer('Currency Digits'),
        'get_currency_digits')

    @staticmethod
    def default_salario():
        return Decimal('0.0')

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

    @fields.depends('salario', 'horas_base')
    def on_change_with_rata(self, name=None):
        res = Decimal('0.0')
        if self.salario:
            exp = Decimal(str(10.0 ** -self.currency_digits))
            res = (self.salario / self.horas_base).quantize(exp)
        return res

    def get_horas_base(self, name=None):
        pool = Pool()
        Config = pool.get('rrhh.pa.208.configuration')
        config = Config(1)
        return config.horas_base
