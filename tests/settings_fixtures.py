import pytest
import tomlkit

import create_config


class ExampleConfig:
    def __init__(self, doc):
        self.path = pytest.tmp_path / 'config.toml'
        self.doc = doc

@pytest.fixture
def default_config() -> ExampleConfig:
    # noinspection PyProtectedMember
    return example_config(create_config._default_config())

@pytest.fixture
def example_config(doc) -> ExampleConfig:
    config = ExampleConfig(doc)
    with open(config.path) as file:
        file.write(tomlkit.dumps(config.doc))
    return config
