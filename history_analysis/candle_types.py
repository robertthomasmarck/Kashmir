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

    @staticmethod
    def change(candle):
        return candle["close"] - candle["open"]

    @staticmethod
    def spike(candle):
        return candle["high"] - max(candle["open"], candle["close"])

    @staticmethod
    def drop(candle):
        return  min(candle["open"], candle["close"]) - candle["low"]

    @staticmethod
    def span(candle):
        return candle["high"] - candle["low"]

    @staticmethod
    def flat_type(spike, drop):
        if  spike > 0 and drop > 0:
            return Candle.FLAT_11.value
        elif spike == 0 and drop > 0:
            return Candle.FLAT_12.value
        elif spike > 0 and drop == 0:
            return Candle.FLAT_13.value
        else:
            pass
            # Todo: add an error

    @staticmethod
    def ox_type(spike, drop, change):
        if  spike == 0 and drop == 0:
            return Candle.OX_1
        elif spike == 0 and drop > 0:
            return Candle.OX_2.value
        elif spike + drop <= change:
            return Candle.OX_3.value
        elif spike + drop > change:
            return Candle.OX_4.value
        elif drop == 0 and spike > 0:
            return Candle.OX_5.value
        else:
            pass
            # Todo: add an error


    @staticmethod
    def bear_type(spike, drop, change):
        if  spike == 0 and drop == 0:
            return Candle.BEAR_6.value
        elif spike > 0 and drop == 0:
            return Candle.BEAR_7.value
        elif spike + drop <= abs(change):
            return Candle.BEAR_8.value
        elif spike + drop > abs(change):
            return Candle.BEAR_9.value
        elif spike > 0 and drop == 0:
            return Candle.BEAR_10.value
        else:
            pass
            # Todo: add an error

    @staticmethod
    def get_candle_type(candle_data) -> Enum:
        animal = Animal.which_animal(candle_data)
        change = Candle.change(candle_data)
        spike = Candle.spike(candle_data)
        drop = Candle.drop(candle_data)
        # Neutrals
        if animal == "FLAT":
            return Candle.flat_type(spike, drop)
        # Oxes
        elif animal == "OX":
            return Candle.ox_type(spike, drop, change)
        # Bears
        elif animal == "BEAR":
            return Candle.bear_type(spike, drop, change)

class Animal(Enum):
    OX = "OX"
    BEAR = "BEAR"
    FLAT = "FLAT"

    @staticmethod
    def which_animal(candle_data):
        opn = candle_data["open"]
        cls = candle_data["close"]
        if opn == cls:
            return Animal.FLAT
        elif opn < cls:
            return Animal.OX
        elif opn > cls:
            return Animal.BEAR










