# imports - standard imports
from collections         import MutableMapping

# imports - module imports
from schema.cache        import Cache
from schema.error        import raise_not_implemented_error
from schema.util.checker import check_str

class Schema(MutableMapping):
    def __init__(self, name, props = None, refresh = False, version = None):
        check_str(type_, raise_err = True)

        if props  != None:
            check_mapping(props, raise_err = True)

        self.cache = Cache(version = version)
        self.cache.create()

        self.store = self.cache.get(name, refresh = refresh)
        
    def __getitem__(self, key):
        raise_not_implemented_error()

    def __setitem__(self, key, value):
        raise_not_implemented_error()

    def __delitem__(self, key):
        raise_not_implemented_error()

    def __len__(self):
        raise_not_implemented_error()

    def __iter__(self):
        raise_not_implemented_error()

    def __repr__(self):
        raise_not_implemented_error()

    def __str__(self):
        raise_not_implemented_error()