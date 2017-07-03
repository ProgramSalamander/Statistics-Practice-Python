import math
from scipy.stats import norm


class Solution:
    def solve(self):
        alpha = 0.05
        n = 100
        df = n - 1
        sample_avg = 0.6
        norm_val = norm.ppf(1 - alpha / 2)
        print(norm_val)
        a = (n + norm_val ** 2)
        b = -(2 * n * sample_avg + norm_val ** 2)
        c = n * (sample_avg ** 2)
        print(a)
        print(b)
        print(c)
        lower = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        higher = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return [lower, higher]


print(Solution().solve())
