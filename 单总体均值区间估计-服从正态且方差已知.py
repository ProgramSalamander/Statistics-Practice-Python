import math
from scipy import stats
from scipy.stats import norm


class Solution:
    def solve(self):
        alpha = 0.05
        n = 3600
        variance = 25
        z = norm.ppf(1 - alpha / 2)
        lower = 8.5 - (math.sqrt(variance) / math.sqrt(n)) * z
        higher = 8.5 + (math.sqrt(variance) / math.sqrt(n)) * z
        return [lower, higher]

print(Solution().solve())