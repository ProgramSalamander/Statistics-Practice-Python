# 假定一块蛋糕上的葡萄干粒数服从泊松分布，如果想让每块蛋糕上至少有一粒葡萄干的概率大于等于0.98，蛋糕上葡萄干的平均粒数应该是多少？

import math
from scipy.stats import poisson


class Solution():
    def solve(self):
        lamd = -math.log(1 - 0.98)
        return math.ceil(lamd)


print(Solution().solve())
