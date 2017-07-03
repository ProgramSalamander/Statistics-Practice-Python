import numpy
import math
from scipy.stats import t
from scipy.stats.mstats import ttest_1samp

class Solution():
    def solve(self):
        n = 25
        h_avg = 8
        df = n - 1
        alpha = 0.05
        sample_avg = 7.73
        sample_dev = 0.77
        t_standard = t.ppf(alpha/2, df)
        t_test = (sample_avg - h_avg)/(sample_dev / math.sqrt(n))
        # print(ttest_1samp([159,280,101,212,224,379,179,264,222,362,168,250,149,260,485,170],225))
        if abs(t_test) >= t_standard:
            H0 = False
        else:
            H0 = True
        return [df, round(t_test,2), H0]


print(Solution().solve())
