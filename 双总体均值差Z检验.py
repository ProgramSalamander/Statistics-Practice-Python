import math
import scipy.stats
from scipy.stats import norm


class Solution():
    def solve(self):
        n = 44 / 2
        sample_dev_1 = 45.1
        sample_avg_1 = 52.1
        sample_dev_2 = 26.4
        sample_avg_2 = 27.1
        alpha = 0.05
        z_alpha = norm.ppf(1 - alpha / 2)
        z = (sample_avg_1 - sample_avg_2) / math.sqrt((sample_dev_1 ** 2) / n + (sample_dev_2 ** 2) / n)

        if z > z_alpha:
            H0 = False
        else:
            H0 = True
        return [n - 1, round(z, 2), H0]


print(Solution().solve())
