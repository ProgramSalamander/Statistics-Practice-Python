import math
from scipy.stats import t


class Solution:
    def solve(self):
        alpha = 0.05
        n = 16
        df = n - 1
        sample_avg = 503.75
        sample_dev = 6.2022
        t_standard = t.ppf(1 - alpha / 2, df)
        lower = sample_avg - (sample_dev / math.sqrt(n)) * t_standard
        higher = sample_avg + (sample_dev / math.sqrt(n)) * t_standard
        return [round(lower,1), round(higher,1)]

print(Solution().solve())