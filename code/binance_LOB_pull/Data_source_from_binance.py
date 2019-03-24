
__author__ = "Justin Skillman, Arun Sridhar"

import numpy as np
import time
import binance.client
from binance.client import Client
import pandas as pd

# Parameters
Time = 60 * 5 # Time is gven in seconds
nLevels = 10
out_filename = '../cnn_lob/data/' + 'test_lob.csv'

# using my api key... to get a new api key go to : https://www.binance.com/en
api_key = 'dg43rhsu46Mgo8OqNEzRtEElBPMVaHUhXS43sQ3EYphHTpDZImMOhk9ic0TJcvnD'
api_secret = '8vjeqpojJOULtkqUcklmq3cbLxNeQfWz3cztd0fkRrUiEsvXi9hqypmPzHyVk5Mo'
stash = ['BNBBTC', 'XRPBTC', 'ETHBTC', 'LTCBTC', 'ADABTC', 'TUSDBTC', 'BCHABCBTC', 'EOSBTC', 'BCDBTC']
client = Client(api_key, api_secret)

ask_strs = ['ask_q_' + str(x) for x in range(nLevels)] + ['ask_p_' + str(x) for x in range(nLevels)]
bid_strs = ['bid_q_' + str(x) for x in range(nLevels)] + ['bid_p_' + str(x) for x in range(nLevels)]
other_strs = ['date', 'timestamp', 'mid_top', 'order_imbalance']
out = pd.DataFrame(columns = other_strs + ask_strs + bid_strs)  # collection bin

# the follwing code runs for the next 1000 seconds and snapshots order book for your product
# at every 5 seconds... can change the 5 seconds to whatever delta you want as long as it is
# greater than 0.005
# Ive modified the data to get order imbalance... you can store asks and bids to get top 10 levels of order book
# data
#
print('Fetching LOB data...')

for i in range(0,Time):
    k = 0
    time.sleep(1)

    dpt = client.get_order_book(symbol = 'ETHBTC') # change it to whatever crypto.. use right symbol.. look up at the array
    curr_time = pd.datetime.now()  # TODO: Fix this time, there must be a time from the API!
    ask_q = (np.array(dpt['asks']).T)[1][0:nLevels].astype(float).tolist()
    ask_p = (np.array(dpt['asks']).T)[0][0:nLevels].astype(float).tolist()
    bid_q = (np.array(dpt['bids']).T)[1][0:nLevels].astype(float).tolist()
    bid_p = (np.array(dpt['bids']).T)[0][0:nLevels].astype(float).tolist()
    order_imbalance = [(bid_q[0] - ask_q[0]) / (ask_q[0] + bid_q[0])]
    # order_imbalance_total.append((sum(bids[0:3]) - sum(asks[0:3])) / (sum(bids[0:3]) + sum(asks[0:3])))
    midpoint = [(ask_p[0] + bid_p[0]) / 2]  # only of top of book
    date = [curr_time.strftime('%Y/%m/%d')]
    timestamp = [int(curr_time.timestamp())]  # records the second un UNIX epoch timestamp

    out_l = date + timestamp + midpoint + order_imbalance + ask_q + ask_p + bid_q + bid_p
    out.loc[len(out)] = out_l

# Write Data to Disk
out.to_csv(out_filename, index=False)
