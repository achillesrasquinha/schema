# module  - schema.dtype
# imports - compatibility imports
from __future__      import absolute_import

# imports - standard imports
import datetime

# imports - module imports
from schema.dtype.url import URL

DTYPES = \
{
     'Boolean': bool,
      'Number': (int, float),
        'Text': str, 
           URL: URL,
        'Date': datetime.date,
    'DateTime': datetime.datetime,
        'Time': datetime.time
}