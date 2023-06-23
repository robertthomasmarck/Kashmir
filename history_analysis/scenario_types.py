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
    S_4 = "NOT DEFINED"

    @staticmethod
    def is_1(y, t) -> bool:
        return t["high"] < y["high"] and t["low"] > y["low"]

    @staticmethod
    def is_2d(y, t) -> bool:
        return t["low"] < y["low"]

    @staticmethod
    def is_2u(y, t) -> bool:
        return t["high"] > y["high"]

    @staticmethod
    def is_3(y, t):
        return t["high"] > y["high"] and t["low"] < y["low"]

    @staticmethod
    def which_scen(yestc, todac):
        if Scen.is_1(yestc, todac):
            return Scen.S_1
        elif Scen.is_2d(yestc, todac):
            return Scen.S_2d
        elif Scen.is_2u(yestc, todac):
            return Scen.S_2u
        elif Scen.is_3(yestc, todac):
            return Scen.S_3
        else:
            return Scen.S_4



def write_scen_to_hist():
    path = paths.get_path("../histories/BTCUSD-1Day-09012021-10012021.json")
    # path = paths.get_path(f"histories\\{filename}")

    with open(path) as candle_list:
        data = json.load(candle_list)
        for symb, candles in data.items():
            for yest, today in zip(candles, candles[1:]):
                which_scen(yest, today)






def test_a():
    scenario_finder()




