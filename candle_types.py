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
    OX_1 = 1
    # 2 is change and a bigger drop, 2nd most OXish
    OX_2 = 2
    # 3 is a big change, small drop, small spike, normal OXish
    OX_3 = 3
    # 4 is a small change, big drop, small spike, neutral OXish
    OX_4 = 4
    # 5 is a small change, no drop, big spike, least OXish
    OX_5 = 5
    # 6 is all change, no spike, no drop, most bearish
    BEAR_6 = 6
    # 7 is change and a bigger spike, 2nd most bearish
    BEAR_7 = 7
    # 8 is big change, small drop, small spike, normal bearish
    BEAR_8 = 8
    # 9 is small change, big spike, big drop, neutral bearish
    BEAR_9 = 9
    # 10 is a small change, big drop, least bearish
    BEAR_10 = 10
    # 11 is near 0 change, near 50/50 drop/spike, neutral
    FLAT_11 = 11
    # 12 is near 0 change, near 100% spike, neutral
    FLAT_12 = 12
    # 13 is near 0 change, near 100%, neutral
    FLAT_13 = 13


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
        return Candle.FLAT_11
    elif change == 0 and spike == 0 < drop:
        return Candle.FLAT_12
    elif change == 0 < spike and drop == 0:
        return Candle.FLAT_13
    # Bulls
    if span == change > 0:
        return Candle.OX_1
    elif spike == 0 < drop and change > 0:
        return Candle.OX_2
    elif spike + drop <= change > 0:
        return Candle.OX_3
    elif spike + drop > change > 0:
        return Candle.OX_4
    elif drop == 0 and spike > 0 and change > 0:
        return Candle.OX_5
    # Bears
    elif span == change < 0:
        return Candle.BEAR_6
    elif drop == 0 < spike and change < 0:
        return Candle.BEAR_7
    elif spike + drop <= abs(change) and change < 0:
        return Candle.BEAR_8
    elif spike + drop > abs(change) and change < 0:
        return Candle.BEAR_9
    elif drop == 0 < spike and change < 0:
        return Candle.BEAR_10


def make_scen_seq(file):
    with open(file, 'r') as f:
        data = json.load(f)
    for symb, candles in data.items():
        for candle in candles:
            candle['type'] = get_candle_type(candle)
        with open(file, "w") as g:
            json.dump(data, g)



def make_candle_seq(data):
    f = json.load(open(data))
    for val, key in f.items():
        for b in key:
            print(get_candle_type(b))


def test_this():
    make_scen_seq("test_data.json")
