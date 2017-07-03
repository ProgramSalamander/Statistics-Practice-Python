import math
from scipy import stats
from scipy.stats import t


class Solution():
    def solve(self):
        alpha = 0.05
        n = 36
        t_val = t.ppf(1 - alpha / 2, n - 1)
        avg_interval = [18.985, 21.015]
        sample_avg = (avg_interval[0] + avg_interval[1]) / 2
        sample_dev = (avg_interval[1] - sample_avg) / t_val * math.sqrt(n)
        return [round(sample_avg, 2), round(sample_dev, 2)]


print(Solution().solve())
