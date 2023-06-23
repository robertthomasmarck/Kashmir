import attr
from alpaca.data import CryptoHistoricalDataClient


@attr.define
class CryptoHistoryClient:
    client = attr.ib(default=CryptoHistoricalDataClient())
    symb_list: list = attr.ib(default='BTC/USD')
    time_frame: str = attr.ib(default='Day')
    start_time: str = attr.ib(click.DateTime(formats=['%m-%d-%Y']))
    end_time: str = attr.ib(click.DateTime(formats=['%m-%d-%Y']))


    def get_bars(self):
        return self.client.get_crypto_bars()