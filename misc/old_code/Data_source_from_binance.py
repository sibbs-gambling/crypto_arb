# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:22:18 2019

@author: drago
"""

import numpy as np
import time
import binance.client
from binance.client import Client


# using my api key... to get a new api key go to : https://www.binance.com/en
api_key = 'dg43rhsu46Mgo8OqNEzRtEElBPMVaHUhXS43sQ3EYphHTpDZImMOhk9ic0TJcvnD'
api_secret = '8vjeqpojJOULtkqUcklmq3cbLxNeQfWz3cztd0fkRrUiEsvXi9hqypmPzHyVk5Mo'
stash = ['BNBBTC', 'XRPBTC', 'ETHBTC', 'LTCBTC', 'ADABTC', 'TUSDBTC', 'BCHABCBTC', 'EOSBTC', 'BCDBTC']
client = Client(api_key, api_secret)
depth = [[],[],[],[],[],[],[],[],[]]

btc = []
btc_price = []
btc_bid = []
btc_ask = []
order_imbalance = []
order_imbalance_ranked = []
order_imbalance_total = []

Time = 1000 # Time is gven in seconds

# the follwing code runs for the next 1000 seconds and snapshots order book for your product 
# at every 5 seconds... can change the 5 seconds to whatever delta you want as long as it is 
# greater than 0.005
# Ive modified the data to get order imbalance... you can store asks and bids to get top 10 levels of order book
# data
# 

for i in range(0,Time):
    k = 0
    time.sleep(5)
    try:
        dpt = client.get_order_book(symbol = 'ETHBTC') # change it to whatever crypto.. use right symbol.. look up at the array
        asks = (np.array(dpt['asks']).T)[1][0:10] # 10 refers to 10 levels change it to whatever levels of orderbook data you want
        asks = np.round_(asks.astype(np.float), 6)
        ask_price = float((np.array(dpt['asks']).T)[0][0]) # top of the book ask
        bids = (np.array(dpt['bids'])).T[1][0:10]
        bids = np.round_(bids.astype(np.float),6)
        bid_price = float((np.array(dpt['bids']).T)[0][0])
        midpoint = (ask_price + bid_price)/2
        btc_price.append(midpoint)
        btc.append(np.array([asks,bids]))
        btc_bid.append(round(bid_price,6))
        btc_ask.append(round(ask_price,6))
        order_imbalance.append( (bids[0]-asks[0]) / (asks[0] + bids[0]) )
        order_imbalance.append( )
        order_imbalance_total.append((sum(bids[0:3]) - sum(asks[0:3])) / (sum(bids[0:3]) + sum(asks[0:3])))
    except:
        continue


