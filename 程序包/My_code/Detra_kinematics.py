###########delta机械手运动学相关###############
import math
import numpy as np


R=135 #静平台外接圆
r=0  #动平台外接圆
L=380 #主动臂长度
La=980 #从动臂长度


#输入xyz坐标，输出大臂角度
def Fanjie(x,y,z):
    A1 = (x * x + y * y + z * z + L * L - La * La + (R - r) * (R - r) - 2 * x * (R - r)) / (2 * L)
    B1 = -(R - r - x)
    C1 = z
    A2 = (x * x + y * y + z * z + L * L - La * La + (R - r) * (R - r) + (x - math.sqrt(3) * y) * (R - r)) / L
    B2 = -2 * (R - r) - (x - math.sqrt(3) * y)
    C2 = 2 * z
    A3 = (x * x + y * y + z * z + L * L - La * La + (R - r) * (R - r) + (x + math.sqrt(3) * y) * (R - r)) / L
    B3 = -2 * (R - r) - (x + math.sqrt(3) * y)
    C3 = 2 * z
    K1 = A1 + B1
    U1 = 2 * C1
    V1 = A1 - B1
    K2 = A2 + B2
    U2 = 2 * C2
    V2 = A2 - B2
    K3 = A3 + B3
    U3 = 2 * C3
    V3 = A3 - B3
    theta1 = 2 * math.degrees(math.atan((-U1 - math.sqrt(U1 * U1 - 4 * K1 * V1)) / (2 * K1)))
    theta2 = 2 * math.degrees(math.atan((-U2 - math.sqrt(U2 * U2 - 4 * K2 * V2)) / (2 * K2)))
    theta3 = 2 * math.degrees(math.atan((-U3 - math.sqrt(U3 * U3 - 4 * K3 * V3)) / (2 * K3)))
    #弧度角度转化
    theta1 = theta1/180*math.pi
    theta2 = theta2 / 180 * math.pi
    theta3 = theta3 / 180 * math.pi
    return theta1,theta2,theta3

def Zhengjie(theta1, theta2, theta3):
    # theta1 =  theta1 * 180 / np.pi
    # theta2 = theta2 * 180 / np.pi
    # theta3 = theta3 * 180 / np.pi
    A1 = R + L * np.cos(theta1) - r
    B1 = 1
    C1 = L * np.sin(theta1)
    A2 = -(1 / 2) * (R + L * np.cos(theta2) - r)
    B2 = (np.sqrt(3) / 2) * (R + L * np.cos(theta2) - r)
    C2 = L * np.sin(theta2)
    A3 = -(1 / 2) * (R + L * np.cos(theta3) - r)
    B3 = -(np.sqrt(3) / 2) * (R + L * np.cos(theta3) - r)
    C3 = L * np.sin(theta3)
    D1 = (1 / 2) * (A2 * A2 - A1 * A1 + C2 * C2 - C1 * C1 + B2 * B2)
    A21 = A2 - A1
    C21 = C2 - C1
    D2 = (1 / 2) * (A3 * A3 - A1 * A1 + C3 * C3 - C1 * C1 + B3 * B3)
    A31 = A3 - A1
    C31 = C3 - C1
    E1 = (B3 * C21 - B2 * C31) / (A21 * B3 - A31 * B2)
    F1 = (B3 * D1 - B2 * D2) / (A21 * B3 - A31 * B2)
    E2 = (A31 * C21 - A21 * C31) / (A31 * B2 - A21 * B3)
    F2 = (A31 * D1 - A21 * D2) / (A31 * B2 - A21 * B3)
    a = E1 * E1 + E2 * E2 + 1
    b = 2 * E2 * F2 + 2 * C1 - 2 * E1 * (A1 - F1)
    c = (A1 - F1) * (A1 - F1) + F2 * F2 + C1 * C1 - La * La
    Z = (-b - np.sqrt(b * b - 4 * a * c)) / (2 * a)
    X = E1 * Z + F1
    Y = E2 * Z + F2
    return X, Y, Z



