import settings_fixtures
import settings


def test_default_settings():
    config = settings_fixtures.default_config
    settings.Settings()
