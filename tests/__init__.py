# This file is part of Tryton. The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

try:
    from trytond.modules.rrhh_pa_208.tests.test_rrhh_pa_208 import suite
except ImportError:
    from .test_rrhh_pa_208 import suite


__all__ = ['suite']
