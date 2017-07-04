import numpy
import math
from scipy.stats import f


class Solution():
    def solve(self):
        sample1 = numpy.array([78.1, 72.4, 76.2, 74.3, 77.4, 78.4, 76.0, 75.5, 76.7, 77.3])
        sample2 = numpy.array([79.1, 81.0, 77.3, 79.1, 80.0, 79.1, 79.1, 77.3, 80.2, 82.1])
        df1 = sample1.__len__() - 1
        df2 = sample2.__len__() - 1
        sample1_var = sample1.var()
        sample2_var = sample2.var()
        alpha = 0.05
        f_val = f.ppf(alpha, 9, 9)
        f_test = sample1_var / sample2_var
        if f_test < f_val:
            H0 = False
        else:
            H0 = True
        return [df1, df2, f_test, H0]


print(Solution().solve())
