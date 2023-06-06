import math

import matplotlib.pyplot as plt
import numpy as np
from IPython import embed
from numpy.polynomial import Polynomial as P
from scipy.interpolate import PPoly

##################摆线归一化运动规律的实现
def Cycloid_motion( T ,step):
    t = np.linspace(0 , T , step)
    s = t - (1/(2*np.pi)) * np.sin(2*np.pi*t)
    v = 1 - np.cos(2*np.pi*t)
    a = 2*np.pi*np.sin(2*np.pi*t)

    return s

