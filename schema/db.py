# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
from sqlalchemy import create_engine

# imports - module imports
from schema.util.checker import check_str

class DB(object):
    def __init__(self, dialect, database, user = '', password = ''):
        check_str(dialect, database, user, password)