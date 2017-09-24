# imports - third-party imports
import pytest

# imports - module imports
from schema import DB

def test_db():
    db = DB('sqlite', 'foo.db')