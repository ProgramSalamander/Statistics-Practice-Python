import numpy
import math
from scipy.stats import t


class Solution():
    def solve(self):
        sample1 = numpy.array([78.1, 72.4, 76.2, 74.3, 77.4, 78.4, 76.0, 75.5, 76.7, 77.3])
        sample2 = numpy.array([79.1, 81.0, 77.3, 79.1, 80.0, 79.1, 79.1, 77.3, 80.2, 82.1])
        temp = []
        for i in range(sample2.__len__()):
            temp.append(sample2[i] - sample1[i])
        d = numpy.array(temp)
        n = 10
        df = n - 1
        d_avg = d.mean()
        d_std = d.std()
        alpha = 0.05
        print d_avg
        print d_std
        t_val = t.isf(alpha, df)
        t_test = d_avg / (d_std / math.sqrt(n))
        print t_val
        print t_test
        if t_test > t_val:
            H0 = False
        else:
            H0 = True
        return [df, t_test, H0]


print(Solution().solve())
