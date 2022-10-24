import json
from enum import Enum

from utils import paths


class Scen(Enum):
    # When today's candle does not break the high or the low (wick) of the previous day.
    # Also known as a consolidation.
    S_1 = "1"
    S_2d = "2d"
    S_2u = "2u"
    S_3 = "3"

    @staticmethod
    def methd(y, t):
        return True



def scenario_finder():
    # todo: find a way to iterate over a list an compare the two values
    path = paths.get_path("histories/BTCUSD-1Day-09012021-10012021.json")
    # path = paths.get_path(f"histories\\{filename}")

    with open(path) as candle_list:
        data = json.load(candle_list)
        for symb, candles in data.items():
            for yest, today in zip(candles, candles[1:]):
                which_scen(yest, today)


def scen_1_check(y, t):
    cond = []
    cond.append(y["high"] > t["high"])
    cond.append([y["low"] < t["low"]])
    return all(cond)



def scen_2_check(yestc, todac):
    pass


def which_scen(yestc, todac):
    if scen_1_check(yestc, todac):
        return Scen.S_1
    elif scen_2_check(yestc, todac):
        return Scen.methd(yestc, todac)

def scen_1_check(y, t):
    cond = [y["high"] > t["high"]]
    cond.append([y["low"] < t["low"]])


def test_a():
    scenario_finder()




