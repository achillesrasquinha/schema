# imports - standard imports
import sys, os
sys.path.insert(0, os.path.abspath('../..'))

# imports - module imports
from package import package

project        = package['name']
version        = package['version']
release        = package['release']

source_suffix  = ['.rst']

master_doc     = 'index'

html_theme     = 'alabaster'