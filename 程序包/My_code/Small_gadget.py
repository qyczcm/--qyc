import numpy as np


def data_easy_analysis(p1,t,input_string):
    t1_min = np.min(p1(t))
    t1_max = np.max(p1(t))
    print(input_string+"最小值")
    print(t1_min)
    print(input_string+"最大值")
    print(t1_max)
    return 0