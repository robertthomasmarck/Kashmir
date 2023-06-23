import json

from candle_types import Candle
from utils import paths


def write_scen_to_hist():
    path = paths.get_path("../histories/BTCUSD-1Day-09012021-10012021.json")
    # path = paths.get_path(f"histories\\{filename}")

    with open(path) as candle_list:
        data = json.load(candle_list)
        for symb, candles in data.items():
            for yest, today in zip(candles, candles[1:]):
                which_scen(yest, today)

def write_type_to_history(file):
    with open(file, 'r') as f:
        data = json.load(f)
    for symb, candles in data.items():
        for candle in candles:
            add_candle_type(candle)
        with open(file, "w") as g:
            json.dump(candles, g, indent=2)

def add_candle_type(candle):
    type = get_candle_type(candle)
    candle['type'] = type
    return candle

def make_candle_seq(data):
    f = json.load(open(data))
    for val, key in f.items():
        for c in key:
            print(Candle.get_candle_type(c))

test_candle = {
    "symbol": "BTC/USD",
    "timestamp": "2021-09-01T05:00:00+00:00",
    "open": 47128.0,
    "high": 49910.0,
    "low": 47124.0,
    "close": 49420.0,
    "volume": 970.77,
    "trade_count": 6375.0,
    "vwap": 48282.504172152
  }

def test_thing():
    add_candle_type(test_candle)