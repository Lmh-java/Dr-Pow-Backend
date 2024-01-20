import configparser


class Config:
    OPEN_AI_API_KEY = None
    UNSPLASH_API_KEY = None

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('./config.ini')
        self.OPEN_AI_API_KEY = config['open_ai_api_key']
        self.UNSPLASH_API_KEY = config['unsplash_api_key']


# this is a singleton class, you should not initialize it
singleton = None
if not singleton:
    singleton = Config()
