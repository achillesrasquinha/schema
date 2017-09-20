# imports - module imports
from bot.util import get_uuid_str

class Config(object):
    JOBS                  = [
        {
                 'id': get_uuid_str(strip = True),
               'func': 'bot:run',
            'trigger': 'interval',
            'seconds': 10
        }
    ]

    SCHEDULER_API_ENABLED = True