import json
import numpy as np
import seaborn as sns
import pandas as pd

with open("data.json", "r") as fp:
    ctr = dict(map(lambda x: (int(x[0]), x[1]), json.load(fp).items()))

# print(ctr)

sns.set_theme()
from math import exp, log, log1p, log2
# sns.displot(ctr)
# sns.barplot(x=["A", "B", "C"], y=[1, 3, 2])

import matplotlib.pyplot as plt
# plt.show()

import scipy.stats as st

counter_2 = {}

def invert(n):
    out = 0
    for shift in range(3):
        out |= ((n >> shift) & 0x1) << (3 - shift)
    return out

n = 1
for key, value in ctr.items():
    # key = int((log((key + 1) / 5))) % 4
    if key != 0:
        low = key % 10
        high = key // 10
        key = (((low & 0xf) << 4) ^ (invert(high))) % 15 + 1
    counter_2[key] = counter_2.get(key, 0) + value

ctr = counter_2

# counter_2 = {}
# for key, value in ctr.items():
#     counter_2[key] = counter_2.get(key, 0) + value

# ctr = counter_2

s = sum(ctr.values())
ent = -1 * sum((value / s) * (log2(value / s)) for value in ctr.values())
print(ent, s, ctr)

# data = pd.DataFrame(ctr, columns=["x", "y"])

sns.barplot(ctr)
plt.show()

# data = np.array(list(map(tuple, ctr.items())))
# data = np.repeat(data[:,0], data[:,1])
# print(data, len(data))

# sns.displot(data, kind="ecdf")

# ret = st.fit(st.expon, data, [(0, 100)])
# print(ret)
# ret.plot()

plt.show()