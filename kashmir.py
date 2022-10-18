import json

import click
import requests
from requests.auth import HTTPBasicAuth

from utils import paths


# chamber_keys.json

@click.group()
def cli():
    pass


@cli.command()
def sheba():
    click.echo("I will rule the world!!!")
    pass

@cli.command()
def look_at_assets():
    key_chain = keys()['sandbox']
    hidden_key = HTTPBasicAuth(key_chain['key'], key_chain['secret'])
    response = requests.get(key_chain['endpoint'] + "/v1/assets", auth=hidden_key).json()
    pass


def keys():
    f = open(paths.get_path('login/chamber_keys.json'))
    keys = json.load(f)
    return keys
