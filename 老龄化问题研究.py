# 人口普查是一项重要的国情调查，对于国家管理、制定各项方针政策具有重要的意义，中国最早的一次人口普查在西汉汉平帝元始二年进行，
# 而自中华人民共和国建国以来分别在1953、1964、1982、1990、2000和2010年进行了共六次人口普查，
# 其中第六次人口普查分别涉及到了人口增长、家庭户人口、性别构成、年龄构成、民族构成、受教育程度、城乡人口、人口流动性等八方面。
# 现有《各地区分性别、健康状况的60岁及以上老年人口》调查数据、《各地区户数、人口数和性别比》调查数据，
# 定义老龄率=60岁及以上人口数*100/总人口数，以北京市为例，其老龄率为250084*100/1849475=13.52，
# 请编写python代码回答如下问题：
# 以各省市数据为代表，求取中国省级老龄率均值的置信区间、方差的置信区间，置信水平均为90%，假设老龄率符合正态分布

import math
import numpy
from scipy.stats import t
from scipy.stats import chi2


class Solution:
    def solve(self):
        raw_data = [[250084, 1849475],
                    [162233, 1127589],
                    [928642, 7037620],
                    [414649, 3477805],
                    [275828, 2310941],
                    [672227, 4252076],
                    [349177, 2551123],
                    [468616, 3465051],
                    [345592, 2253525],
                    [1237962, 7577122],
                    [759091, 5400348],
                    [853195, 5312628],
                    [420377, 3477491],
                    [504043, 4251692],
                    [1400109, 9272503],
                    [1196924, 9224288],
                    [779566, 5226904],
                    [939818, 6096586],
                    [957360, 9676589],
                    [616828, 4362551],
                    [93525, 826560],
                    [488115, 2609882],
                    [1412294, 8161604],
                    [446686, 3332265],
                    [514563, 4467537],
                    [20828, 265904],
                    [487378, 3614887],
                    [338325, 2623094],
                    [51945, 535412],
                    [61207, 611957],
                    [201515, 2086576]]
        temp_data = []
        for x in raw_data:
            temp_data.append(self.cal_old(x))
        print(temp_data)
        data = numpy.array(temp_data)
        alpha = 0.1
        n = 31
        df = n - 1
        sample_avg = data.mean()
        sample_dev = math.sqrt(data.var())
        sample_var = data.var()
        t_standard = t.ppf(1 - alpha / 2, df)
        avg_lower = sample_avg - (sample_dev / math.sqrt(n)) * t_standard
        avg_higher = sample_avg + (sample_dev / math.sqrt(n)) * t_standard

        chi2_lower = chi2.ppf(1 - alpha / 2, df)
        chi2_higher = chi2.ppf(alpha / 2, df)
        var_lower = (df * sample_var) / chi2_lower
        var_higher = (df * sample_var) / chi2_higher
        return [[avg_lower, avg_higher], [var_lower, var_higher]]

    def cal_old(self, data):
        return data[0] * 100 / data[1]


print(Solution().solve())
