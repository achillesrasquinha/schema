# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
import sys

# imports - module imports
from bot import cli

if __name__ == '__main__':
    args = sys.argv[1:]
    code = cli.main(args)

    sys.exit(code)