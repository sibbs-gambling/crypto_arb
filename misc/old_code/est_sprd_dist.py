# Modules
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import datetime as dt
np.set_printoptions(suppress=True) # turn off sci notation

# Params
window = 30  # num days to look over for each dist realization
dir_in = "../../data/in/"

# Read Data
dat = pd.read_csv(dir_in + "cryptocompare_close.csv")

# Find Mean, SD for each Window and each Exchange Pair
# Size = (5 exchanges x 5 exchanges) x ~30 dates
df = dat.loc[:, dat.columns != 'date']  # no dates
exchanges = list(dat.columns[1:dat.shape[1]])
sprd_bin = np.zeros((len(exchanges), len(exchanges),
                     dat.shape[0]))
jexchanges = np.array(list(range(0, len(exchanges))))
for jexch in range(len(exchanges)):
    exchange = exchanges[jexch]
    diff = np.array(df.iloc[:, np.repeat(jexch, len(exchanges)-1)]) - \
           np.array(df.loc[:, df.columns != exchange])
    sprd_bin[jexch, jexchanges[jexchanges!=jexch]] = np.transpose(diff)

sprd_mean = np.zeros((len(exchanges), len(exchanges),
                      (dat.shape[0] - window)))
sprd_sd = np.zeros((len(exchanges), len(exchanges),
                      (dat.shape[0] - window)))
for jt in range(window, (dat.shape[0])):
    sub = sprd_bin[:, :, (jt-window):jt]
    sprd_mean[:, :, jt-window] = np.mean(sub, axis=2)
    sprd_sd[:, :, jt-window] = np.std(sub, axis=2)

# Plot Means and SDs over time
i = 0
while i < dat.shape[0]:
    dl = [int(x) for x in (dat.iloc[i, 0]).split('-')]
    dat.iloc[i, 0] = dt.datetime(dl[0], dl[1], dl[2])
    i += 1
x = list(dat.iloc[:, 0])
dates = x[window:len(x)]

plt.figure(figsize=(20, 10))
for x in range(1, len(exchanges)):
    for y in range(x):
        plt.plot(dates, sprd_mean[x, y, :], label=
        exchanges[x] + "-" + exchanges[y])

plt.xticks(size=16, rotation=45)
plt.legend(prop={'size': 15})
plt.title("Mean Exchange Spreads over Time, window="+str(window)+" days",
          size=20)
plt.show()

plt.figure(figsize=(20, 10))
for x in range(1, len(exchanges)):
    for y in range(x):
        plt.plot(dates, sprd_sd[x, y, :], label=
        exchanges[x] + "-" + exchanges[y])

plt.xticks(size=16, rotation=45)
plt.legend(prop={'size': 15})
plt.title("SDs of Exchange Spreads over Time, window="+str(window)+" days",
          size=20)
plt.show()

# Plot simple Time Series of each Exchange
plt.figure(figsize=(20, 10))
for x in range(0, len(exchanges)):
    plt.plot(dates, dat.iloc[window:dat.shape[0], x+1], label=
        exchanges[x])

plt.xticks(size=16, rotation=45)
plt.legend(prop={'size': 15})
plt.title("Exchange Prices over Time", size=20)
plt.show();