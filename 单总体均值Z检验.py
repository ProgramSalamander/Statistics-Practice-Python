import math
import scipy.stats
from scipy.stats import norm


class Solution():
    def solve(self):
        n = 51
        sample_dev = 4.9
        sample_avg = 1.1
        alpha = 0.05
        z_alpha = norm.ppf(1 - alpha)
        z = round((sample_avg - 0) / (sample_dev / math.sqrt(n)), 2)

        if z > z_alpha:
            H0 = False
        else:
            H0 = True
        return [n - 1, z, H0]


print(Solution().solve())
