# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:34:15 2019

@author: drago
"""

import binance.client
from binance.client import Client

api_key = 'dg43rhsu46Mgo8OqNEzRtEElBPMVaHUhXS43sQ3EYphHTpDZImMOhk9ic0TJcvnD'
api_secret = '8vjeqpojJOULtkqUcklmq3cbLxNeQfWz3cztd0fkRrUiEsvXi9hqypmPzHyVk5Mo'

stash = ['BNBBTC', 'XRPBTC', 'ETHBTC', 'LTCBTC', 'ADABTC', 'TUSDBTC', 'BCHABCBTC', 'EOSBTC', 'BCDBTC']
client = Client(api_key, api_secret)

# Below function gives a list of all products on binance and also the current bid and ask price and the quantities
tickers = client.get_orderbook_tickers()

# Following gives all the order book information - all levels (100 levels on both sides)
depth = client.get_order_book(symbol='ETHBTC')

# Below gives the candle for the last  minutes - that is 
candles = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_30MINUTE)

klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

# Change the date limits
klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")
klines = client.get_historical_klines("NEOBTC", Client.KLINE_INTERVAL_1WEEK, "1 Jan, 2017")

tickers = client.get_ticker()

agg_trades = client.aggregate_trade_iter(symbol='ETHBTC', start_str='30 minutes ago UTC')

# iterate over the trade iterator
for trade in agg_trades:
    print(trade)
    # do something with the trade data

# convert the iterator to a list
# note: generators can only be iterated over once so we need to call it again
agg_trades = client.aggregate_trade_iter(symbol='ETHBTC', start_str = '30 minutes ago UTC')
agg_trade_list = list(agg_trades)

# example using last_id value
agg_trades = client.aggregate_trade_iter(symbol='ETHBTC', last_id=23380478)
agg_trade_list = list(agg_trades)
