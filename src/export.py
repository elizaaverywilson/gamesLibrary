# noinspection PyPackageRequirements
import berserk

import handler
from settings import Settings


def export():
    settings = Settings()
    settings.setup()
    client = handler.get_client(settings)

    prefs = [berserk.enums.PerfType.CLASSICAL, berserk.enums.PerfType.RAPID]
    games = handler.get_games(settings.lichess_username, client, prefs)
    filters = {'variant': 'standard', 'rated': True}
    filtered = handler.filter_by(games, filters)

    return handler.encode(filtered)

print(export())
