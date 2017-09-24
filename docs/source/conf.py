# imports - standard imports
import sys, os
sys.path.insert(0, os.path.abspath('../..'))

# imports - third-party imports
from recommonmark.parser import CommonMarkParser

# imports - module imports
from package import package

project        = package['name']
version        = package['version']
release        = package['release']

source_parsers = \
{
    '.md': CommonMarkParser
}

source_suffix  = ['.md']