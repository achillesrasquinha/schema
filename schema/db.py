# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
from sqlalchemy import create_engine

# imports - module imports
from schema.util.checker import check_str, check_uint16

def build_url(dialect, database, host = '', port = None, username = '', password = ''):
    pass

class DB(object):
    def __init__(self, dialect, database, host = '', port = None, user = '', password = ''):
        check_str(dialect, database, host, user, password, raise_err = True)
        if port != None:
            check_uint16(port, raise_err = True)

        url          = build_url\
        (
            dialect  = dialect,
            database = database,
            host     = host,
            port     = port,
            username = user,
            password = password 
        )
        # self.engine  = create_engine(url)

    def insert(self):
        pass