import numpy
from scipy.stats import chi2
from scipy.stats import chi2_contingency


class Solution():
    def solve(self):
        d = [[154, 132], [180, 126], [104, 131]]

        # chi2_contingency(d)
        # 第一个值为卡方值，第二个值为P值，第三个值为自由度，第四个为与原数据数组同维度的对应理论值

        chi2_sample = chi2_contingency(d)[0]
        df = chi2_contingency(d)[2]
        chi2_standard = chi2.ppf(0.01, df)
        if chi2_sample > chi2_standard:
            H0 = False
        else:
            H0 = True
        return [round(df, 2), round(chi2_sample, 2), H0]


print(Solution().solve())
