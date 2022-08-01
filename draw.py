import matplotlib.pyplot as plt  # 导入 Matplotlib 工具包
from scipy.optimize import leastsq  # 导入 scipy 中的最小二乘法拟合工具
from scipy.stats import linregress  # 导入 scipy 中的线性回归工具

import checkAxis

test=[1, 3, 4, 5, 6]
checkAxis.get_sensor_location(test)