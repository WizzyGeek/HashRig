# Hash Design Rig

## Challenge
Given is discrete frequency distribution which is known to have little over 5 bits worth of information
Extract the maximum possible information using as little physical bits as possible,
mathematically maximise `entropy^2 / physical bits` where entropy is the informational entropy of the hash
over the given dataset.

### Leaderboard

Current best method is a modified hash algo from [huyane](https://github.com/HuyaneMatsu) with entropy 3.751290 and hash size of 4 bits