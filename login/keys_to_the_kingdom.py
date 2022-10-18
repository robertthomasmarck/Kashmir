import json

from utils import paths


def keys():
    f = open(paths.get_path('/login/chamber_keys.json'))
    keys = json.load(f)
    return keys
