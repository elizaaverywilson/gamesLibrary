import pytest
# noinspection PyPackageRequirements
from berserk.session import Requestor


@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(Requestor, "get", lambda *args, **kwargs: stunted_get())
