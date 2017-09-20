MESSAGES = \
{
    'TypeError': 'Expected {expected} object, recieved {recieved} instead.'
}

class SchemaError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

def raise_not_implemented_error():
    raise NotImplementedError

def raise_type_error(expected, recieved):
    raise TypeError(MESSAGES['TypeError'].format(
        expected = expected,
        recieved = recieved
    ))
