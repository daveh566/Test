import os
from prettyconf import Configuration
from prettyconf.loaders import Environment, EnvFile

env_file = f"{os.getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config(object):
    """
    Configuratoins of `tgEasy`.
    """
    API_ID = config("API_ID")
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
