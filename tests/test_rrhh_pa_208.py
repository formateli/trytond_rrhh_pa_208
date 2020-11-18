# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from decimal import Decimal
from trytond.pool import Pool
from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.modules.company.tests import create_company, set_company
from trytond.exceptions import UserError
from trytond.modules.rrhh.tests import create_employee


class RRHHPa208TestCase(ModuleTestCase):
    'Test rrhh_pa_208 module'
    module = 'rrhh_pa_208'

    @with_transaction()
    def test_rrhh(self):
        pool = Pool()
        Configuration = pool.get('rrhh.pa.208.configuration')
        Hora = pool.get('rrhh.pa.208.hora')
        Deduccion = pool.get('rrhh.pa.208.deduccion')

        # Horas

        hora_normal = Hora(name='NORMAL',
                           tipo='normal')
        hora_normal.save()
        self.assertTrue(hora_normal.id)

        hora_domingo = Hora(name='DOMINGO',
                            tipo='sobretiempo',
                            recargo=50)
        hora_domingo.save()
        self.assertTrue(hora_domingo.id)

        falta_justificada = Hora(name='Falta Justificada',
                                 tipo='descuento')
        falta_justificada.save()
        self.assertTrue(falta_justificada.id)

        retraso = Hora(name='Retraso',
                       tipo='descuento')
        retraso.save()
        self.assertTrue(retraso.id)

        # Deducciones

        seguro_social = Deduccion(name='Seguro Social',
                                  tipo='porcentaje',
                                  valor=Decimal('9.75'),
                                  ley=True)
        seguro_social.save()
        self.assertTrue(seguro_social.id)

        vale_20 = Deduccion(name='Vale 20',
                            tipo='fijo',
                            valor=Decimal('20.0'))
        vale_20.save()
        self.assertTrue(vale_20.id)

        company = create_company()
        with set_company(company):
            employee = create_employee('Employee 1')
            employee.salario = Decimal('2080.0')
            employee.save()
            self.assertEqual(employee.horas_base, Decimal(208.00))
            self.assertEqual(employee.rata, Decimal('10.00'))


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        RRHHPa208TestCase))
    return suite
