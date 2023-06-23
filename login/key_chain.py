import json

from utils import paths


def key_chain():
    f = open(paths.get_path('/login/chamber_keys.json'))
    keys = json.load(f)
    return keys
