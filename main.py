import json
import seaborn as sns

with open("data.json", "r") as fp:
    ctr = dict(map(lambda x: (int(x[0]), x[1]), json.load(fp).items()))

sns.set_theme()
from math import exp, log, log1p, log2

import matplotlib.pyplot as plt

### Current best

def invert(n):
    out = 0
    for shift in range(3):
        out |= ((n >> shift) & 0x1) << (3 - shift)
    return out

def hash_huyane(key):
    if key != 0:
        low = key % 10
        high = key // 10
        key = (((low & 0xf) << 4) ^ (invert(high))) % 15 + 1
    return key

### Add your attempt here

def hash(key):
    if key == 0: return 0
    return (key % 7) + 1

counter_2 = {}
for key, value in ctr.items():
    key = hash(key)
    # key = hash_huyane(key)
    counter_2[key] = counter_2.get(key, 0) + value

ctr = counter_2

s = sum(ctr.values())
ent = -1 * sum((value / s) * (log2(value / s)) for value in ctr.values())
p = max(ctr).bit_length()

print("entropy:", ent)
print("validity:", s == 14167)
print("max physical bits detected:", p)

pv = (1 / (((1 << p) - (2 ** ent)) + 1)) * (1 << p) * (2 ** ent) / ((1 << (max(p, 5) - 5)) ** 2)
print("perf value:", pv)

sns.barplot(ctr)
plt.show()

# Misc

# data = np.array(list(map(tuple, ctr.items())))
# data = np.repeat(data[:,0], data[:,1])
# print(data, len(data))

# sns.displot(data, kind="ecdf")

# ret = st.fit(st.expon, data, [(0, 100)])
# print(ret)
# ret.plot()
# plt.show()