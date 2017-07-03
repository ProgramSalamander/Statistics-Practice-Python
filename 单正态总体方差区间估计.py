import numpy
from scipy.stats import chi2


class Solution:
    def solve(self):
        arr = numpy.array(
            [112.5, 108.8, 115.6, 100.0, 123.5,
             102.0, 101.6, 102.2, 116.6, 95.4,
             97.8, 108.6, 105.0, 136.8, 102.8,
             101.5, 98.4, 93.3, 101.0, 103.0,
             102.0, 100.5, 102.6, 107.5, 95.0])
        alpha = 0.05
        n = 25
        df = n - 1
        sample_var = numpy.var(arr)
        print(sample_var)
        chi2_lower = chi2.ppf(alpha / 2, df)
        chi2_higher = chi2.ppf(1 - alpha / 2, df)
        lower = (df * sample_var) / chi2_lower
        higher = (df * sample_var) / chi2_higher
        return [lower, higher]


print(Solution().solve())
