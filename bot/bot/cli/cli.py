# imports - compatibility imports
from __future__ import absolute_import

# imports - module imports
from bot.app import app, scheduler

def main(args = None):
    app.run()