import berserk

import handler
from config_parser import Settings

settings = Settings()
client = handler.get_client(settings)

prefs = [berserk.enums.PerfType.CLASSICAL, berserk.enums.PerfType.RAPID]
games = handler.get_games(settings.lichess_username, client, prefs)
filters = {'variant': 'standard', 'rated': True}
filtered = handler.filter_by(games, filters)

print(handler.encode(filtered))
