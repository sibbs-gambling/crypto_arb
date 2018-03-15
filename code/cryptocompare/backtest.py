# Modules
import numpy as np

np.set_printoptions(suppress=True)  # turn off sci notation

# Parameters
# (defined above) window = 30  # num days to look over for each dist realization
dir_in = "../../data/in/"
acct_start = 1000  # dollars per exchange account
topmax = 2  # the strongest n deviations to trade
cush = 0.15  # cushion to leave in acct bals


# Function Defs
def comp_sprds(prices):
    sprd = np.zeros((len(exchanges), len(exchanges)))
    for jexch in range(len(exchanges)):
        exchange = exchanges[jexch]
        diff = np.array(prices[np.repeat(jexch, len(exchanges) - 1)]) - \
               np.array(prices[df.columns != exchange])
        sprd[jexch, jexchanges[jexchanges != jexch]] = np.transpose(diff)
    return (sprd)


# Backtest
exchanges = list(dat.columns[1:dat.shape[1]])
jexchanges = np.array(list(range(0, len(exchanges))))
acct_bals = np.zeros((df.shape[0] - window, df.shape[1]))  # dollars in exchanges (shape: time x num exchanges)
acct_bals[0, :] = acct_start
acct_poss = np.zeros((df.shape[0] - window, df.shape[1]))  # positions in each exchange (units)

for jt in range(window, dat.shape[0]):
    # Compute profit from last period.
    if jt > window:
        price_chng = df.iloc[jt, :] - df.iloc[jt - 1, :]
        acct_bals[jt - window, :] = acct_bals[jt - window - 1, :] + acct_poss[jt - window - 1, :] * price_chng

    # Find topmax number of strongest deviations
    max_idx_list = []
    max_sd_devs = []
    sprds = comp_sprds(dat.iloc[jt, 1:len(exchanges) + 1])
    trail_means = sprd_mean[:, :, jt - window]
    trail_sd = sprd_sd[:, :, jt - window]
    numSD_devs = (sprds - trail_means) / (trail_sd + np.identity(len(exchanges)))
    for jmax in range(0, topmax):  # choose highest deviations
        idx = np.where(numSD_devs == numSD_devs.max())
        max_idx_list.append(idx)
        max_sd_devs.append(numSD_devs[idx])
        numSD_devs[idx] = 0
        numSD_devs[:, idx[1]] = 0
        numSD_devs[idx[0], :] = 0

    # Compute number of dollars and position in trades
    for jmax in range(0, topmax):
        exch1 = max_idx_list[jmax][0]
        exch2 = max_idx_list[jmax][1]
        dllrs = np.min((acct_bals[jt - window, exch1], acct_bals[jt - window, exch2])) \
                * (1 - cush)  # trade with min(acct1, acct2)
        acct_poss[jt - window, exch1] = - float(df.iloc[jt, exch1] / dllrs)  # short the exchange above the mean,
        acct_poss[jt - window, exch2] = float(df.iloc[jt, exch2] / dllrs)  # long the exchange below the mean
