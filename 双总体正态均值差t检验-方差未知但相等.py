import numpy
import math
from scipy.stats import t
from scipy.stats.mstats import ttest_1samp


class Solution():
    def solve(self):
        sample1 = numpy.array([78.1, 72.4, 76.2, 74.3, 77.4, 78.4, 76.0, 75.5, 76.7, 77.3])
        sample2 = numpy.array([79.1, 81.0, 77.3, 79.1, 80.0, 79.1, 79.1, 77.3, 80.2, 82.1])
        n1 = 10
        n2 = 10
        df1 = n1 - 1
        df2 = n2 - 1
        sample1_avg = sample1.mean()
        sample2_avg = sample2.mean()
        sample1_var = sample1.var()
        sample2_var = sample2.var()
        h_avg = 0
        alpha = 0.05
        t_standard = t.ppf(alpha, df1 + df2)
        sw2 = (df1 * sample1_var + df2 * sample2_var) / (df1 + df2)
        t_test = (sample1_avg - sample2_avg - h_avg) / (math.sqrt(sw2) * math.sqrt(1.0 / n1 + 1.0 / n2))
        if t_test <= -t_standard:
            H0 = False
        else:
            H0 = True
        return [df1, df2, t_test, H0]


print(Solution().solve())
