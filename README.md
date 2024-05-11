# Hash Design Rig

## Challenge
Given is a discrete frequency distribution which is known to have little over 5 bits worth of information
Extract the maximum possible information using as little physical bits as possible.

### Leaderboard

Current best method is a modified hash algo from [huyane](https://github.com/HuyaneMatsu) with entropy `3.751290 bits` and hash size of `4 bits`.

### Details

Within data.json is given a relation between observed value and frequency of the observation, the keys are the observed value and the values are frequency

Within main.py make your hashing function in-place of the function called `hash`. Implement a hashing strategy and run.

Submit your hash functions via a PR.