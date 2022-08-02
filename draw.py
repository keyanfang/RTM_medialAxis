import matplotlib.pyplot as plt  # 导入 Matplotlib 工具包
from scipy.optimize import leastsq  # 导入 scipy 中的最小二乘法拟合工具
from scipy.stats import linregress  # 导入 scipy 中的线性回归工具

import checkAxis

test = [1, 3, 4, 5, 6]
location = checkAxis.get_sensor_location(test)


def get_attribute_x(dataframe):
    df = dataframe
    list_x = []
    for i in range(len(df)):
        # list = df.iloc[i][0].strip().split('')
        # list1.append(list)
        list_x.append(df.iloc[i][0])
    print(list_x)
    return list_x


def get_attribute_y(dataframe):
    df = dataframe
    list_y = []
    for i in range(len(df)):
        # list = df.iloc[i][0].strip().split('')
        # list1.append(list)
        list_y.append(df.iloc[i][1])
    print(list_y)
    return list_y


def get_attribute_z(dataframe):
    df = dataframe
    list_z = []
    for i in range(len(df)):
        # list = df.iloc[i][0].strip().split('')
        # list1.append(list)
        list_z.append(df.iloc[i][2])
    return list_z


