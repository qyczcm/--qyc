import numpy as np
import matplotlib.pyplot as plt
import Detra_kinematics
R=135
r=40
L=180
La=500
#input:起始弧度；最终弧度；步长
theta1 = np.arange(-0.785, 1.395,0.1)  # 从-22.6到87.1，步长为5.485，生成数据
theta2 = np.arange(-0.785, 1.395,0.1)
theta3 = np.arange(-0.785, 1.395,0.1)

theta23, theta32 = np.meshgrid(theta2, theta3)  # 数据网格化
plt.rcParams['font.family'] = 'Arial'  # 设置字体为Arial
fig = plt.figure(111, figsize=(8, 7))  # 创建画布，大小为 8*7
ax = fig.add_subplot(111, projection='3d')  # 生成子图
ax.set_box_aspect([1, 1, 1])  # 设置长宽高比为1:1:1

# #XYZ工作空间
for item in theta1:
    X, Y, Z = Detra_kinematics.Zhengjie(item, theta23, theta32)  # 正解，生成X Y Z坐标
    #ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='winter')  # 绘制曲面图
    ax.scatter(X, Y, Z, s=1, c=(184/255, 14/255, 246/255), marker='o')

#XZ工作空间投影
fig = plt.figure(1, figsize=(8, 7))  # 画布大小
ax = fig.add_subplot()  # 生成子图
#
for item in theta1:
    X, Y, Z = Detra_kinematics.Zhengjie(item, theta23, theta32)
    ax.scatter( X, Z, s=1, c=(184 / 255, 14 / 255, 246 / 255), marker='o')
    ax.set_xlabel('X/mm')
    ax.set_ylabel('Z/mm')
    ax.grid(True)  # 添加网格
plt.title("Projection of workspace on X-Z plane")
plt.show()  # 显示





