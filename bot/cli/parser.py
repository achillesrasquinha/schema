# imports - standard imports
import argparse

class ArgumentParser(argparse.ArgumentParser):
    def __init__(self, config = { }, *args, **kwargs):
        self.super  = super(ArgumentParser, self)
        self.config = config

        self.super.__init__(*args, **kwargs)

        if 'arguments' in self.config:
            for argument in self.config['arguments']:
                self.add_argument(
                    name = argument['name'],
                    help = argument['help']
                )

    def parse(self, argv = None):
        args = self.parse_args(argv)

        return args