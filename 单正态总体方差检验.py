# -*- coding: utf-8 -*-
import numpy
from scipy.stats import chi2


class Solution():
    def solve(self):
        n = 26
        df = n - 1
        alpha = 0.02
        total_var = 5000
        sample_var = 9200
        chi2_val_higher = chi2.ppf(alpha / 2, df)
        chi2_val_lower = chi2.ppf(1 - alpha / 2, df)
        chi2_test = (n - 1) * sample_var / total_var
        if chi2_test >= chi2_val_higher or chi2_test <= chi2_val_lower:
            H0 = False
        else:
            H0 = True
        return [df, chi2_test, H0]


print(Solution().solve())
