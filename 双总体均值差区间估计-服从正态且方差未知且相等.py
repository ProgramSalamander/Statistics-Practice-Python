import math
from scipy.stats import t


class Solution:
    def solve(self):
        alpha = 0.05
        n1 = 10
        n2 = 20
        df1 = n1 - 1
        df2 = n2 - 1
        t_standard = t.ppf(1 - alpha / 2, df1 + df2)
        sample1_avg = 500
        sample1_dev = 1.10
        sample2_avg = 496
        sample2_dev = 1.20
        sw = math.sqrt((df1 * (sample1_dev ** 2) + df2 * (sample2_dev ** 2)) / (df1 + df2))
        lower = sample1_avg - sample2_avg - sw * t_standard * math.sqrt(1 / n1 + 1 / n2)
        higher = sample1_avg - sample2_avg + sw * t_standard * math.sqrt(1 / n1 + 1 / n2)
        return [lower, higher]


print(Solution().solve())
