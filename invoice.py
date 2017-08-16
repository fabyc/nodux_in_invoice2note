# -*- coding: utf-8 -*-

from trytond.pyson import Eval
from trytond.model import ModelSQL, Workflow, fields, ModelView
from trytond.report import Report
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta
from decimal import Decimal
import time

__all__ = ['Invoice']
__metaclass__ = PoolMeta

class Invoice():
    __name__ = 'account.invoice'

    sale_note = fields.Boolean('Nota de Venta', states={
            'invisible': Eval('type') != 'in_invoice',
            'readonly': Eval('state') != 'draft',
            })

    @classmethod
    def __setup__(cls):
        super(Invoice, cls).__setup__()

    @staticmethod
    def default_exclude_ats():
        return False
