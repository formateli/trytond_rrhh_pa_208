# This file is part of tryton-corseg module. The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

import unittest
import trytond.tests.test_tryton
from trytond.pool import Pool
from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.modules.company.tests import create_company, set_company
from trytond.exceptions import UserError


class RRHHPa208TestCase(ModuleTestCase):
    'Test rrhh_pa_208 module'
    module = 'rrhh_pa_208'

    @with_transaction()
    def test_rrhh(self):
        pool = Pool()
        Employee = pool.get('company.employee')
        Configuration = pool.get('rrhh.pa.208.configuration')
        Hora = pool.get('rrhh.pa.208.hora')
        Deduccion = pool.get('rrhh.pa.208.deduccion')

        company = create_company()
        with set_company(company):
            pass


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        RRHHPa208TestCase))
    return suite
