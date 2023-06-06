import numpy as np
import Small_gadget
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# 指定中文字体文件的路径
font_path = 'C:/WINDOWS/Fonts/AdobeSongStd-Light.otf'

# 创建FontProperties对象，指定中文字体和字号
font_prop = FontProperties(fname=font_path, size=12)

# 设置中文字体为当前字体
plt.rcParams['font.family'] = font_prop.get_name()


def calAndDraw(sport_x_list,sport_y_list,sport_z_list):
    t=np.linspace(0,1,100-1)
    # 拟合曲线求解
    z1 = np.polyfit(t, sport_x_list, 8)
    p1 = np.poly1d(z1)
    print(p1)
    yval1 = p1(t)

    z2 = np.polyfit(t, sport_y_list, 8)
    p2 = np.poly1d(z2)
    print(p2)
    yval2 = p2(t)

    z3 = np.polyfit(t, sport_z_list, 8)
    p3 = np.poly1d(z3)
    print(p3)
    yval3 = p3(t)
    p1_derivative = p1.deriv()  # 一阶求导
    p2_derivative = p2.deriv()  # 一阶求导
    p3_derivative = p3.deriv()  # 一阶求导
    v1 = p1_derivative(t)
    v2 = p2_derivative(t)
    v3 = p3_derivative(t)

    fig2 = plt.figure()
    #散点变化
    # plt.plot(t,sport_x_arr , marker='.', markersize=6, c=(243 / 255, 122 / 255, 230 / 255))
    # plt.plot(t, sport_y_arr, marker='.', markersize=6, c=(138 / 255, 176 / 255, 125 / 255))
    # plt.plot(t, sport_z_arr, marker='.', markersize=6, c=(68 / 255, 70 / 255, 83 / 255))

    # 拟合角度曲线显示
    plt.xlabel('时间/s', fontproperties=font_prop)
    plt.ylabel("关节位置/rad")
    plt.plot(t, yval1, 'r', linewidth=1.5, c=(179 / 255, 184 / 255, 188 / 255))
    plt.plot(t, yval2, 'r', linewidth=1.5, c=(255 / 255, 0 / 255, 0 / 255))
    plt.plot(t, yval3, 'r', linewidth=1.5, c=(236 / 255, 185 / 255, 107 / 255))

    fig3 = plt.figure()
    # 绘制角速度曲线一阶求导
    plt.xlabel("时间/s", fontproperties=font_prop)
    plt.ylabel(r'关节加速度/($\mathrm{rad \cdot s}^{-1}$)',fontproperties=font_prop)
    # Linear  velocity / (rad * s_ - 1)
    plt.plot(t, v1, 'r', linewidth=1.5, c=(179/ 255, 184 / 255, 188 / 255))
    plt.plot(t, v2, 'r', linewidth=1.5, c=(255/ 255, 0 / 255, 0 / 255))
    plt.plot(t, v3, 'r', linewidth=1.5, c=(236 / 255, 185 / 255, 107 / 255))
    q1_derivative = p1_derivative.deriv()  # 二阶求导
    q2_derivative = p2_derivative.deriv()  # 二阶求导
    q3_derivative = p3_derivative.deriv()  # 二阶求导
    a1 = q1_derivative(t)
    a2 = q2_derivative(t)
    a3 = q3_derivative(t)
    # # 绘制角加速度曲线二阶
    fig4 = plt.figure()
    plt.xlabel("时间/s", fontproperties=font_prop)
    plt.ylabel(r'关节角加速度/($\mathrm{rad \cdot s}^{-2}$)', fontproperties=font_prop)
    plt.plot(t, a1, 'r', linewidth=1.5, c=(179 / 255, 184 / 255, 188 / 255))#灰色
    plt.plot(t, a2, 'r', linewidth=1.5, c=(255 / 255, 0 / 255, 0 / 255))#红色
    plt.plot(t, a3, 'r', linewidth=1.5, c=(236 / 255, 185 / 255, 107 / 255))#黄色

    Small_gadget.data_easy_analysis(p1 , t ,"关节1位置")
    Small_gadget.data_easy_analysis(p2, t, "关节2位置")
    Small_gadget.data_easy_analysis(p3, t, "关节3位置")
    Small_gadget.data_easy_analysis(p1_derivative , t ,"关节1速度")
    Small_gadget.data_easy_analysis(p2_derivative, t, "关节2速度")
    Small_gadget.data_easy_analysis(p3_derivative, t, "关节3速度")
    Small_gadget.data_easy_analysis(q1_derivative , t ,"关节1加速度")
    Small_gadget.data_easy_analysis(q2_derivative, t, "关节2加速度")
    Small_gadget.data_easy_analysis(q3_derivative, t, "关节3加速度")
    return 0