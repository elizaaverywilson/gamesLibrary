from pathlib import Path

import tomlkit
from tomlkit.items import String


class Settings:
    """Wrapper for the configuration"""
    config_dir: Path = Path.home() / '.config' / 'gamesLibrary'
    config_path: Path = config_dir / 'config.toml'
    default_config_path: Path = Path().absolute() / 'defaultConfig.toml'

    def __init__(self):
        """Reads config and adds options to wrapper."""

        def __read_config():
            """Returns config file as a TOMLDocument."""
            with open(self.config_path) as c:
                __config_str = c.read()
            return tomlkit.parse(__config_str)

        def __validate(setting, setting_type):
            """Checks that the setting is of correct type"""
            if type(setting) != setting_type:
                raise TypeError('Configuration setting ' + str(setting) + 'is of type'
                                + str(type(setting)) + ', not of expected type' + str(setting_type) + '.')
            else:
                return setting

        __config = __read_config()
       
        self.use_Token = __validate(__config['authentication']['useToken'], bool)
        if self.use_Token:
            __token_path_str = __validate(__config['authentication']['tokenPath'], String)
            self.tokenPath = Path(__token_path_str).expanduser()
        self.lichess_username =__validate(__config['lichess']['username'], String)
