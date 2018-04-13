import numpy as np
import matplotlib as plt

# Plot Account Bals
plt.figure(figsize=(12, 7))

for j in range(len(exchanges)):
    plt.subplot(2, 3, j + 1)
    plt.plot(acct_bals[:, j])
    plt.title(exchanges[j] + " account bal")
    plt.xlabel("Day");
    plt.ylabel("USD")

plt.subplot(2, 3, 6)
plt.plot(np.sum(acct_bals, axis=1))
plt.title("Total (sum) account bal")
plt.xlabel("Day");
plt.ylabel("USD")

plt.tight_layout()

# Plot RoR and Currency RoR
plt.figure(figsize=(14,5))
plt.plot((np.sum(acct_bals, axis=1) - acct_start*5) / acct_start*5)
plt.title("RoR")
plt.xlabel("Day"); plt.ylabel("% of Starting Capital (5K)")
plt.show()

plt.figure(figsize=(14,5))
plt.plot([x for x in range(0, df.shape[0]-window)],
         (np.mean(df.iloc[window:df.shape[0], :], axis=1) - np.mean(df.iloc[window, :])) /
         np.mean(df.iloc[window,:]))
plt.title("Mean % Price Change in Currency")
strtpr = np.round(np.mean(df.iloc[window, :]))
plt.xlabel("Day"); plt.ylabel("% of Initial Mean Price " + "(" + str(strtpr) + ")")
plt.show()


# Sharpe Ratio
tot = np.sum(acct_bals, axis=1)
ror = (tot[len(tot)-1] - acct_start*5) / acct_start*5
sharpe = ror / np.std(tot)
print("Sharpe Ratio: " + str(sharpe))