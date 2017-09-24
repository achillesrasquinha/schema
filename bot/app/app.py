# imports - third-party imports
from flask             import Flask
from flask_apscheduler import APScheduler

# imports - module imports
from bot.app.config import Config

config    = Config()

app       = Flask(__name__)
app.config.from_object(config)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()