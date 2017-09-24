# module  - schema
# imports - compatibility imports
from __future__       import absolute_import

# imports - module imports
from schema.error   import SchemaError, SchemaValidationError
from schema.log     import Logger
from schema.cache   import Cache
from schema.checker import Checker
from schema.schema  import Schema
from schema.db      import DB

def check(name, props, raise_err = False, verbose = False):
    checker = Checker()
    result  = checker.check(name, props, raise_err = raise_err, verbose = verbose)

    return result