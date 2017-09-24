# imports - compatibility imports
from __future__          import absolute_import

# imports - third-party imports
from sqlalchemy          import create_engine

# imports - module imports
from schema.util.util    import assign_if_none, get_uuid_str
from schema.util.checker import check_str, check_uint16, check_type
from schema.schema       import Schema

def build_url(dialect, database, host = '', port = None, username = '', password = ''):
    pass

class DB(object):
    SQLITE = 'sqlite'

    def __init__(self, dialect = None, name = None, host = '', port = None, user = '', password = ''):
        dialect = assign_if_none(dialect, DB.SQLITE)
        name    = assign_if_none(name,    '{name}.db'.format(name = get_uuid_str()))
        
        check_str(dialect, name, host, user, password, raise_err = True)

        if port != None:
            check_uint16(port, raise_err = True)

        url          = build_url\
        (
            dialect  = dialect,
            database = name,
            host     = host,
            port     = port,
            username = user,
            password = password 
        )

    def insert(self, schema, name = None):
        if name   != None:
            schema = Schema(name, schema)

        check_type(schema, Schema, raise_err = True)