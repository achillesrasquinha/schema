# imports - module imports
from bot.cli.parser import ArgumentParser
from bot            import SchemaBot

def main(args = None):
    parser  = ArgumentParser()
    args    = parser.parse(args)

    if not len(args):
        bot = SchemaBot()
        bot.run()