import numpy as np

#######提供z轴，顺时针和逆时针旋转45度的函数
def zheng_point(x,y,z):
    l= x * np.cos(np.pi/4) + y * np.sin(np.pi/4)
    m = x * -1 * np.sin(np.pi/4) + y * np.cos(np.pi/4)
    n = z
    return l, m, n

def fan_point(x,y,z):
    l = x * np.cos(-1*np.pi/4) + y * np.sin(-1*np.pi/4)
    m = x * -1 * np.sin(-1*np.pi/4) + y * np.cos(-1*np.pi/4)
    n = z
    return l, m, n

#输入坐标列表，返回转换后的坐标列表
def list_zheng_rotate(list_x , list_y):
    data_x_list = []
    data_y_list = []
    data_z_list = []
    for i in range(0,list_x.size):
        sport_x , sport_y , sport_z = fan_point(list_x[i],0,list_x[i])
        data_x_list.append(sport_x)
        data_y_list.append(sport_y)
        data_z_list.append(sport_z)

    return data_x_list , data_y_list , data_z_list
