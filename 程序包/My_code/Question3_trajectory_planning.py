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


#返回规划好的路径
def Full_AirArc(center, point1, point2):
    # Calculate the radius
    huchang = 5032
    radius = np.linalg.norm(center - point1)
    # Calculate the angle between the two points
    angle1 = np.arctan2(point1[1] - center[1], point1[0] - center[0])
    angle2 = np.arctan2(point2[1] - center[1], point2[0] - center[0])
    angle = np.abs(angle2 - angle1)
    # Create an array of angles for plotting the arc
    if angle2 <= angle1:
        angles = np.linspace(angle1, angle2, huchang)
    else:
        angles = np.linspace(angle1, angle2 + 2*np.pi, 100)

    #第一条直线
    t = np.linspace(0 , 25 , 250)
    x1 = -250 + t*0
    y1 = t
    # Calculate the x and y coordinates of the arc得到圆弧点
    x2 = center[0] + radius * np.cos(angles)
    y2 = center[1] + radius * np.sin(angles)
    #第3条直线
    t = np.linspace( 25, 0 , 250)
    x3 = 250 + t*0
    y3 = t
    data_x = [x1,x2,x3]
    data_y = [y1, y2, y3]
    data_x = np.concatenate(data_x)##合并三条线的x数据
    data_y = np.concatenate(data_y) ##合并三条线的y数据
    return data_x,data_y