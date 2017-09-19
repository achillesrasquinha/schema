# imports - module imports
from bot.cli.parser import ArgumentParser
from bot            import SchemaBot

def main(argv = None):
    parser  = ArgumentParser()
    args    = parser.parse(argv)

    if not argv:
        bot = SchemaBot()
        bot.run()