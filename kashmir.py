import json

import click
from alpaca.data import CryptoBarsRequest, TimeFrame

from alpaca.trading import TradingClient, MarketOrderRequest, OrderSide, TimeInForce
from alpaca.data.historical import CryptoHistoricalDataClient

from login.keys_to_the_kingdom import keys
from utils.custom_types import TIMEFRAME as timeframe

key_chain = keys()['paper']


@click.group()
def kash():
    pass


@kash.command()
def look_at_account():
    trading_client = TradingClient(key_chain["key"], key_chain["secret"], paper=True)
    account = trading_client.get_account()
    for property_name, value in account:
        click.echo(f"\"{property_name}\": {value}")


@kash.command()
def buy():
    trading_client = TradingClient(key_chain["key"], key_chain["secret"], paper=True)
    market_order_data = MarketOrderRequest(
        symbol="BTC/USD",
        qty=.0001,
        side=OrderSide.BUY,
        time_in_force=TimeInForce.GTC
    )

    market_order = trading_client.submit_order(market_order_data)
    order_obj = json.loads(market_order.json())
    for property_name, value in market_order:
        print(f"\"{property_name}\": {value}")


@kash.command()
def my_pos():
    trading_client = TradingClient(key_chain["key"], key_chain["secret"], paper=True)
    positions = trading_client.get_all_positions()
    for position in positions:
        for property_name, value in position:
            print(f"\"{property_name}\": {value}")





@kash.command()
@click.option('-symb', '--symbol', type=str, default='BTC/USD')
@click.option('-tf', '--time-frame', type=timeframe, default='Day')
def hist(symbol, time_frame):
    client = CryptoHistoricalDataClient()
    request_params = CryptoBarsRequest(
        symbol_or_symbols=[symbol],
        timeframe=time_frame,
        start="2022-09-01 00:00:00",
        end="2022-09-07 00:00:00"
    )
    btc_bars = client.get_crypto_bars(request_params)
    order_obj = json.loads(btc_bars.json())
    # Convert to dataframe
    print(btc_bars.df)





