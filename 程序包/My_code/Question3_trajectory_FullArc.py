import numpy as np
######################门字型代码/半圆弧 实现代码#########################
def FullArc():
    # 第一条直线
    t = np.linspace(-350, -500, 150)
    x1 = -1 * 141 + t * 0
    z1 = t
    # 第2条：圆弧
    t = np.linspace(3, 4.5, 78)
    x2 = 50 * np.cos((np.pi / 3) * t) - 141 + 50
    z2 = 50 * np.sin((np.pi / 3) * t) - 500
    # 第3条：直线
    t = np.linspace(-91, 91, 182)
    x3 = t
    z3 = -550 + t * 0
    # 第4条：圆弧
    t = np.linspace(4.5, 6, 78)
    x4 = 50 * np.cos((np.pi / 3) * t) + 141 - 50
    z4 = 50 * np.sin((np.pi / 3) * t) - 500
    # 第5条：直线
    t = np.linspace(-500, -350, 150)
    x5 = 141 + t * 0
    z5 = t

    # 角度变化数据处理+绘图
    data_x = [x1, x2, x3, x4, x5]
    data_y = [z1, z2, z3, z4, z5]
    data_x = np.concatenate(data_x)  ##合并五条线的x数据
    data_y = np.concatenate(data_y)  ##合并五条线的z数据
    return data_x ,data_y
#####################main############################
