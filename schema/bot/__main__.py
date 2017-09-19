# imports - standard imports
import sys, os

# imports - module imports
import bot

if __name__ == '__main__':
    args = sys.argv[1:]
    code = bot.cli.main(args)

    sys.exit(code)