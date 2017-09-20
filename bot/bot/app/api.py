# imports - module imports
from bot.app.app import app

@app.route('/')
def index():
    return 'This is a development server for <a href="https://github.com/achillesrasquinha/schema">schema</a>.'