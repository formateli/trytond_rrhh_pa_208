#This file is part of tryton-rrhh project. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.pyson import Eval, Equal, Not
from trytond.pool import Pool
from trytond.model import (
    ModelSingleton, ModelView, ModelSQL, fields)
from trytond.transaction import Transaction
from decimal import Decimal

__all__ = ['Configuration', 'Hora', 'Deduccion']


def _get_currency_digits():
    Company = Pool().get('company.company')
    company = Transaction().context.get('company')
    if company:
        company = Company(company)
        return company.currency.digits
    return 2


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
        return Decimal('208.0')

    @staticmethod
    def default_currency_digits():
        return _get_currency_digits()

    def get_currency_digits(self, name=None):
        return _get_currency_digits()


class Hora(ModelSQL, ModelView):
    'Hora'
    __name__ = 'rrhh.pa.208.hora'
    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripcion')
    tipo = fields.Selection(
        [
            ('normal', 'Normal'),
            ('sobretiempo', 'Sobretiempo'),
            ('descuento', 'Descuento'),
        ], 'Tipo', required=True)
    recargo = fields.Numeric('% Recargo',
        digits=(16, Eval('currency_digits', 2)),
        states={
            'invisible': Not(Equal(Eval('tipo'), 'sobretiempo')),
        },
        depends=['currency_digits', 'tipo'])
    currency_digits = fields.Function(fields.Integer('Currency Digits'),
        'get_currency_digits')
    orden = fields.Integer('Orden')
    active = fields.Boolean('Active')

    @staticmethod
    def default_active():
        return True

    @staticmethod
    def default_currency_digits():
        return _get_currency_digits()

    def get_currency_digits(self, name=None):
        return _get_currency_digits()


class Deduccion(ModelSQL, ModelView):
    'Deduccion'
    __name__ = 'rrhh.pa.208.deduccion'
    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripcion')
    tipo = fields.Selection([
        ('porcentaje', 'Porcentaje'),
        ('fijo', 'Monto Fijo'),
    ], 'Tipo', required=True)
    valor = fields.Numeric('Valor', required=True,
        digits=(16, Eval('currency_digits', 2)),
        depends=['currency_digits'])
    currency_digits = fields.Function(fields.Integer('Currency Digits'),
        'get_currency_digits')
    orden = fields.Integer('Orden')
    ley = fields.Boolean('De Ley')
    active = fields.Boolean('Active')

    @staticmethod
    def default_active():
        return True

    @staticmethod
    def default_currency_digits():
        return _get_currency_digits()

    def get_currency_digits(self, name=None):
        return _get_currency_digits()

