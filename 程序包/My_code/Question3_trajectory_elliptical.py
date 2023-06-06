import numpy as np

######################main#######################
#获取规划好的椭圆路径
def Get_elliptical():
    dis = 25*np.pi +450 #椭圆长度
    #第一条直线
    t = np.linspace(0, 25, 25)
    x1 = -250 + t * 0
    y1 = t
    a = 250
    b = 25
    t = np.linspace(0,3,528)
    x2 = a*np.cos((np.pi/3)*t)
    y2 = b*np.sin((np.pi/3)*t)+25
    # 第3条直线
    t = np.linspace(25, 0, 25)
    x3 = 250 + t * 0
    y3 = t
    ##合并三条线的数据
    data_x = [x1, x2, x3]
    data_y = [y1, y2, y3]
    data_x = np.concatenate(data_x)  ##合并三条线的x数据
    data_y = np.concatenate(data_y)  ##合并三条线的y数据
    return data_x ,data_y

