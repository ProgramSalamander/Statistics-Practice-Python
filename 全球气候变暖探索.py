# -*- coding: utf-8 -*-
# 当前世界全球变暖现象严重，为了探索中国是否也存在这个现象，现调查了中国主要城市的全年气温情况，
# 包括2010年全年气温状况与2014年全年气温状况，以8月份气温为例，假设主要城市温度符合正态分布，
# 试比较是否存在温度上升现象？（需给出证明过程，仅回答YES或NO不得分）


import math
import numpy
import urllib
from scipy.stats import t


class Solution():
    def solve(self):
        n = 31
        csv_file1 = urllib.urlopen("http://py.mooctest.net:8081/dataset/temperature/temperature_2010.csv")
        csv_file2 = urllib.urlopen("http://py.mooctest.net:8081/dataset/temperature/temperature_2014.csv")
        sample1 = []
        i = 0
        for line in csv_file1:
            i = i + 1
            if i <= 6:
                continue
            if i >= 38:
                break
            sample1.append(float(line.split(',')[8]))
        print sample1
        i = 0
        sample2 = []
        for line in csv_file2:
            i = i + 1
            if i <= 5:
                continue
            if i >= 37:
                break
            sample2.append(float(line.split(',')[8]))
        print sample2
        # sample1 = [25.7, 25.6, 25.6, 22.4, 21.7, 23.3, 23, 22.2, 27.9, 27.2, 28.4, 27.5, 29.3, 29.4, 25.1, 26, 29.1,
        #            29.4, 29.9, 28.8, 28.1, 28.4, 25, 23.6, 20.6, 16.4, 24.7, 18.3, 15.4, 21.3, 22.9]
        # sample2 = [27.3, 27.7, 27.9, 23.6, 20.6, 24.3, 22.6, 22.5, 31, 30.8,
        #            31.3, 31.1, 29.6, 31.6, 28.6, 30.1, 30.6, 32, 27.5, 27.7, 27.9, 30.5, 26.5, 23.1, 19.9,
        #            15.9, 28.3, 21, 18.2, 24.4, 22.8]
        temp_data = []
        for x in range(n):
            temp_data.append(sample2[x] - sample1[x])
        data = numpy.array(temp_data)
        alpha = 0.05
        h_avg = 0
        df = n - 1
        sample_avg = data.mean()
        sample_dev = math.sqrt(data.var())
        t_standard = t.ppf(alpha, df)
        t_test = (sample_avg - h_avg) / (sample_dev / math.sqrt(n))
        if t_test >= t_standard:
            H0 = False
        else:
            H0 = True
        return H0


print(Solution().solve())
