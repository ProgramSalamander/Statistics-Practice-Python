import math
from scipy.stats import norm


class Solution:
    def solve(self):
        alpha = 0.05
        n1 = 46
        n2 = 33
        df1 = n1 - 1
        df2 = n2 - 1
        norm_standard = norm.ppf(1 - alpha / 2)
        sample1_avg = 86
        sample1_dev = 5.8
        sample2_avg = 78
        sample2_dev = 7.2
        lower = sample1_avg - sample2_avg - norm_standard*math.sqrt(sample1_dev**2/n1+sample2_dev**2/n2)
        higher = sample1_avg - sample2_avg + norm_standard*math.sqrt(sample1_dev**2/n1+sample2_dev**2/n2)
        return [lower, higher]


print(Solution().solve())
