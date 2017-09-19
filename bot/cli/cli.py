# imports - module imports
from bot.cli.parser import ArgumentParser
from bot            import SchemaBot

CONFIG = \
{
    'arguments':
    [
        {
               'name': ['-d', '--dest'],
               'type': str,
            'default': '.',
               'help': 'directory path to save'
        },
        {
               'name': ['-i', '--indent'],
               'type': int,
            'default': 4,
               'help': 'indentation for JSON files'
        }
    ]
}

def main(argv = None):
    parser  = ArgumentParser(CONFIG)
    args    = parser.parse(argv)

    bot     = SchemaBot()
    bot.run(
        savedir = args.dest,
        indent  = args.indent
    )