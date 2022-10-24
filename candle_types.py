import json
from enum import Enum


class Candle(Enum):
    """What defines what the candle type?
    1. Direction - Primary indicator of how strong the type, BEAR or OX is.
    2. change v DROP - The drop is the second indicator of how strong the OX is, and how weak the BEAR is.
      This is counter-intuitive: the drop is POTENTIAL change that wasn't realized.
      The demand was strong enough to cancel out a temporary drop in price.
    3. change v SPIKE
    4. Drop v Spike
    """
    # 1 is all change, no spike, no drop, most OXish
    OX_1 = 1, "OX"
    # 2 is change and a bigger drop, 2nd most OXish
    OX_2 = 2, "OX"
    # 3 is a big change, small drop, small spike, normal OXish
    OX_3 = 3, "OX"
    # 4 is a small change, big drop, small spike, neutral OXish
    OX_4 = 4, "OX"
    # 5 is a small change, no drop, big spike, least OXish
    OX_5 = 5, "OX"
    # 6 is all change, no spike, no drop, most bearish
    BEAR_6 = 6, "BEAR"
    # 7 is change and a bigger spike, 2nd most bearish
    BEAR_7 = 7, "BEAR"
    # 8 is big change, small drop, small spike, normal bearish
    BEAR_8 = 8, "BEAR"
    # 9 is small change, big spike, big drop, neutral bearish
    BEAR_9 = 9, "BEAR"
    # 10 is a small change, big drop, least bearish
    BEAR_10 = 10, "BEAR"
    # 11 is near 0 change, near 50/50 drop/spike, neutral
    FLAT_11 = 11, "FLAT"
    # 12 is near 0 change, near 100% spike, neutral
    FLAT_12 = 12, "FLAT"
    # 13 is near 0 change, near 100%, neutral
    FLAT_13 = 13, "FLAT"


def get_candle_type(candle_dat) -> Candle:
    hi = candle_dat["high"]
    lo = candle_dat["low"]
    opn = candle_dat["open"]
    cls = candle_dat["close"]
    span = hi - lo
    change = cls - opn
    spike = hi - max(opn, cls)
    drop = min(opn, cls) - lo
    # Neutrals
    if change == 0 and spike > 0 and drop > 0:
        return Candle.FLAT_11.value
    elif change == 0 and spike == 0 < drop:
        return Candle.FLAT_12.value
    elif change == 0 < spike and drop == 0:
        return Candle.FLAT_13.value
    # Bulls
    if span == change > 0:
        return Candle.OX_1
    elif spike == 0 < drop and change > 0:
        return Candle.OX_2.value
    elif spike + drop <= change > 0:
        return Candle.OX_3.value
    elif spike + drop > change > 0:
        return Candle.OX_4.value
    elif drop == 0 and spike > 0 and change > 0:
        return Candle.OX_5.value
    # Bears
    elif span == change < 0:
        return Candle.BEAR_6.value
    elif drop == 0 < spike and change < 0:
        return Candle.BEAR_7.value
    elif spike + drop <= abs(change) and change < 0:
        return Candle.BEAR_8.value
    elif spike + drop > abs(change) and change < 0:
        return Candle.BEAR_9.value
    elif drop == 0 < spike and change < 0:
        return Candle.BEAR_10.value


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
            print(get_candle_type(c))


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



