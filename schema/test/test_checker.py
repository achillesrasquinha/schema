# imports - third-party imports
import pytest

# imports - module imports
from schema import Checker

def test_checker():
    checker = Checker()

def test_checker_check():
    checker = Checker()
    checker.check('Thing', dict(
        url = 'http://bit.ly/2fbwx4m'
    ))