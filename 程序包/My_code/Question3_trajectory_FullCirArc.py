import numpy as np

huchang = 5032

#返回规划好的路径
def Full_AirArc(center, point1, point2):
    # Calculate the radius
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


