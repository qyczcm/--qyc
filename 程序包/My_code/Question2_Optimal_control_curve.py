import math
import numpy as np
import Detra_kinematics

def question_2():
    x_arr = []
    y_arr = []
    z_arr = []
    t = np.linspace(0, 6, 200)
    for i in t:
        x = 200 * np.cos((np.pi / 3) * i)
        y = 200 * np.sin((np.pi / 3) * i)
        z = -800
        theta1, theta2, theta3 = Detra_kinematics.Fanjie(x,y,z)
        x_arr.append(theta1)
        y_arr.append(theta2)
        z_arr.append(theta3)

    # 最优控制拟合曲线求解
    z1 = np.polyfit(t, x_arr, 8)
    p1 = np.poly1d(z1)
    yval1 = p1(t)

    z2 = np.polyfit(t, y_arr, 8)
    p2 = np.poly1d(z2)
    yval2 = p2(t)

    z3 = np.polyfit(t, z_arr, 8)
    p3 = np.poly1d(z3)
    yval3 = p3(t)

