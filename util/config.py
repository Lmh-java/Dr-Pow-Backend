import configparser


# this is a singleton class, you should not initialize it
class Config:
    OPEN_AI_API_KEY = None
    UNSPLASH_API_KEY = None

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('./config.ini')
        Config.OPEN_AI_API_KEY = config['api_keys']['open_ai_api_key']
        Config.UNSPLASH_API_KEY = config['api_keys']['unsplash_api_key']


# this is a singleton class, you should not initialize it
singleton = None
if not singleton:
    singleton = Config()
