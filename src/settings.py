from pathlib import Path

import tomlkit
from tomlkit.items import String


class Settings:
    """Wrapper for the configuration
    Should call self.setup() if settings details are needed.
    Otherwise, referencing settings attributes besides self.config_path will raise an error."""

    def __init__(self, config_path=(Path.home() / '.config/gamesLibrary/config.toml')):
        self.config_path = config_path

        # Call self.setup() to prepare the attributes below.
        def _no_setting():
            raise UnboundLocalError

        self.token_path = _no_setting
        self.lichess_username = _no_setting
        self.use_token = _no_setting

    def setup(self):
        """Reads config and adds options to wrapper."""
        config = self._read_config()
        self.use_token = self._validate(config['authentication']['useToken'], bool)
        if self.use_token:
            token_path_str = self._validate(config['authentication']['tokenPath'], String)
            self.token_path = Path(token_path_str).expanduser()
        self.lichess_username = self._validate(config['lichess']['username'], String)

    def _read_config(self):
        """Reads configuration file and returns it as a TOMLDocument."""
        with open(self.config_path) as c:
            config_str = c.read()
        return tomlkit.parse(config_str)

    @staticmethod
    def _validate(setting, setting_type):
        """Confirms that the configuration file is of the expected type."""
        if type(setting) != setting_type:
            raise TypeError('Configuration setting ' + str(setting) + 'is of type'
                            + str(type(setting)) + ', not of expected type' + str(setting_type) + '.')
        else:
            return setting
