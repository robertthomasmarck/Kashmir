import json

import click
from alpaca.data import CryptoBarsRequest

from alpaca.trading import TradingClient, MarketOrderRequest, OrderSide, TimeInForce
from alpaca.data.historical import CryptoHistoricalDataClient

from utils import paths
from utils.custom_types import TIMEFRAME as timeframe







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
@click.option('-w', '--write', is_flag=True, default=False, help='Do you want to store the history?')
@click.option('-symb', '--symbol', type=str, default='BTC/USD')
@click.option('-tf', '--time-frame', type=timeframe, default='Day')
@click.option('-s', '--start', type=click.DateTime(formats=['%m-%d-%Y']), required=True)
@click.option('-e', '--end', type=click.DateTime(formats=['%m-%d-%Y']), required=True)
def hist(write, symbol, time_frame, start, end):
    # Todo: Figure out the timezone thing
    client = CryptoHistoricalDataClient()
    request_params = CryptoBarsRequest(
        symbol_or_symbols=[symbol],
        timeframe=time_frame,
        start=f"{start}",
        end=f"{end}"
    )
    btc_bars = client.get_crypto_bars(request_params)
    order_obj = json.loads(btc_bars.json())['data']
    # Writing to sample.json
    if write:
        for candle in order_obj[symbol]:
            add_candle_type(candle)
        filename = f"{symbol.replace('/', '')}-{time_frame}-{start.strftime('%m%d%Y')}-{end.strftime('%m%d%Y')}.json"
        path = paths.get_path(f"histories\\{filename}")
        with open(path, "w") as outfile:
            write_obj = json.dumps(order_obj, indent=2)
            print(write_obj)
            click.echo(f"Writing file to histories: {filename}")
            outfile.write(write_obj)
            print(btc_bars.df)
    else:
        btc_bars.df

@kash.command()
@click.option('-f', '--file', type=str, required=True)
def add_type(file):
    write_type_to_history(file)

