import datetime
import json

import berserk

from config_parser import Settings


def get_client(settings=Settings()):
    """Creates lichess client, authenticated or not based on if they are configured"""
    if settings.use_Token:
        with open(settings.tokenPath) as f:
            token = f.read()
        session = berserk.TokenSession(token)
        client = berserk.Client(session)
    else:
        client = berserk.Client()

    return client


def get_games(username, client=berserk.Client(), prefs=None):
    """Returns list of games according to preference.
    If games that fulfill one of several preferences, prefs can be a list with
    elements of type berserk.enums.PrefType"""

    if isinstance(prefs, str):
        games_list = list(client.games.export_by_player(username, max=2,
                                                        rated=True, perf_type=prefs))
    elif isinstance(prefs, list):
        games_list = list()
        for p in prefs:
            games_list.extend(client.games.export_by_player(username, max=5,
                                                            rated=True, perf_type=p))
    else:
        raise TypeError
    return games_list


def encode(games_list):
    """Encodes a list of games into JSON."""

    def datetime_handler(dt):
        """Parses Python's datetime.datetime into ISO for JSON."""
        if isinstance(dt, datetime.datetime):
            return dt.isoformat()
        else:
            raise TypeError('Unknown ' + str(dt) + ' of type ' + str(type(dt)) + '.')
    encoder = json.JSONEncoder(default=datetime_handler, indent=4)
    games = encoder.encode(games_list)
    return games


def filter_by(games=None, filters=None):
    """Returns a list of games filtered
    All games returns must match all the filters"""
    filtered = []
    for game in games:
        for key, f in filters.items():
            if game[key] != f:
                break
        else:
            filtered.append(game)
    return filtered
