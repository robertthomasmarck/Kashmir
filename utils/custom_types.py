import click
from alpaca.data import TimeFrame


class TimeFrameParamType(click.ParamType):
    name = "timeframe"

    def convert(self, value, param, ctx):
        if isinstance(value, TimeFrame):
            return value
        try:
            if value == "Day":
                return TimeFrame.Day
            elif value == "Week":
                return TimeFrame.Week
            elif value == "Month":
                return TimeFrame.Month
            elif value == "Minute":
                return TimeFrame.Minute
            elif value == "Hour":
                return TimeFrame.Hour
            else:
                return TimeFrame.Day
        except ValueError:
            self.fail(f"{value!r} is not a valid time frame.", param, ctx)


TIMEFRAME = TimeFrameParamType()