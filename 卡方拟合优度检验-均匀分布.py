from scipy.stats import chisquare
import math


class Solution():
    def solve(self):
        df = 3 - 1
        alpha = 0.05
        test_val = chisquare([43, 21, 35], [33, 33, 33])[0]
        p = chisquare([43, 21, 35], [33, 33, 33])[1]
        if p < alpha:
            H0 = False
        else:
            H0 = True

        return [df, round(test_val,2), H0]

print(Solution().solve())
