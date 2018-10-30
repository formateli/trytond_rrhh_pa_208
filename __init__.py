#This file is part of tryton-rrhh project. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from .configuration import *
from .employee import *


def register():
    Pool.register(
        Configuration,
        Employee,
        module='rrhh_pa_208', type_='model')
