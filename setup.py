import os
import shutil

from config_parser import Settings


def create_config():
    """Creates configuration file if it does not exist."""

    print('Checking for config set-up...')

    config_dir = Settings.config_dir
    config_path = Settings.config_path

    if not config_dir.exists():
        print(str(config_dir) + """ does not exist. 
            Creating """ + str(config_dir) + ' ...')
        os.makedirs(config_dir)
        print(str(config_dir) + ' created.')

    if not config_path.exists():
        print(str(config_path) + """ does not exist. 
            Creating """ + config_path.name + ' ...')
        print(Settings.default_config_path)
        shutil.copy(Settings.default_config_path, config_path)
        print(config_path.name + ' created at ' + str(config_path) + '.')
    else:
        print('Config already exists at ' + str(config_path) + '.')


if __name__ == "__main__":
    create_config()
