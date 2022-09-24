import os

import tomlkit.items
import tomlkit

from settings import Settings


def _default_config() -> tomlkit.document():
    config = tomlkit.document()
    config['title'] = 'gamesLibrary Configuration'

    authentication = tomlkit.table()
    authentication['use_token'] = False
    authentication['token_path'] = '~/.config/gamesLibrary/lichessToken.txt'
    config['authentication'] = authentication

    lichess = tomlkit.table()
    lichess['username'] = 'gmwesleyso1993'
    config['lichess'] = lichess

    return config


def create_config():
    """Creates configuration file if it does not exist."""

    print('Checking for config set-up...')
    settings = Settings()
    config_path = settings.config_path

    def create_parents():
        print(str(config_path.parent) + """ does not exist. 
            Creating """ + str(config_path.parent) + ' ...')
        os.makedirs(config_path.parent)
        print(str(config_path.parent) + ' created.')

    def create_file():
        print(str(config_path) + """ does not exist. 
            Creating """ + config_path.name + ' ...')

        with open(config_path) as file:
            file.write(tomlkit.dumps(_default_config()))

        print(config_path.name + ' created at ' + str(config_path) + '.')

    if not config_path.parent.exists():
        create_parents()
    if not config_path.exists():
        create_file()
    else:
        print('Config already exists at ' + str(config_path) + '.')


if __name__ == "_main_":
    create_config()
