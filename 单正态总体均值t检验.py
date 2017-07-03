import numpy
import math
from scipy.stats import t
from scipy.stats.mstats import ttest_1samp

class Solution():
    def solve(self):
        n = 20
        h_avg = 5
        df = n - 1
        alpha = 0.05
        sample_avg = 4.6
        sample_dev = 2.2
        t_standard = t.ppf(alpha, df)
        print(t_standard)
        t_test = (sample_avg - h_avg)/(sample_dev / math.sqrt(n))
        # print(ttest_1samp([159,280,101,212,224,379,179,264,222,362,168,250,149,260,485,170],225))
        if t_test > t_standard:
            H0 = False
        else:
            H0 = True
        return [df, round(t_test,2), H0]


print(Solution().solve())
