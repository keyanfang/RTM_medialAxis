# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes,files,tool windows,actions,and settings.
import tkinter as tk
from tkinter import filedialog
import numpy as np

import pandas as pd

time1 = [124.4288, 991.7147, 290.1113, 701.1015, 617.6743, 659.4029, 307.5349, 994.7385, 184.3257, 789.8208, 315.2538,
         151.5564, 869.6319, 990.8455, 582.0982,
         115.9137, 521.6781, 502.8839, 838.6673, 928.2018, 146.5421, 267.5610, 843.6129, 390.9406, 903.8624, 303.9839,
         282.7625, 513.8377, 492.5174, 894.8604, 303.2770, 941.4157, 857.0260, 710.5883, 429.8748, 362.1392, 651.8929,
         961.6710, 236.6557, 433.5082, 995.2139, 408.3655, 504.5016, 163.1853, 522.1873, 113.7921, 754.8174, 122.0764,
         417.3432, 849.7838, 334.0334, 184.2821, 129.6736, 118.1840, 547.2202, 581.9971, 447.3134, 164.8999, 351.7720,
         443.2302, 972.6287, 981.6495, 485.9012, 519.2591, 159.3070, 809.8064, 782.6121, 936.0158, 387.2393, 870.7505,
         576.8273, 182.6711, 941.0888, 733.5658, 229.8376, 501.6279, 643.3274, 614.9490, 281.1279, 855.2632, 945.9266,
         416.7811, 298.9986, 352.5110, 904.6651, 888.1043, 200.2542, 350.7669, 257.9843, 770.5370, 103.5365, 558.6707,
         671.9414, 124.4288, 237.7250, ]
time2 = [557.6873, 344.4303, 778.6131]
time3 = [921.2907, 624.4947, 141.3588, 131.8533, 845.0695, 640.8698, 621.2738, 377.2309, 512.8663, 264.8690, 578.9641,
         403.6210, 188.4861, 497.8439, 204.9497, 121.9882, 291.9175, 800.2429, 716.8903, 443.0219, 576.5938, 284.8589,
         355.3343, 850.1793, 108.2413, 384.3025, 970.4179, 689.5224, 950.9237, 258.4441, 137.0155, 282.2966, 653.3641,
         431.1251, 744.2115, 132.4346, 609.8717, 301.5994, 338.6395, 496.6527, 871.4349, 845.2475, 804.6169, 103.3621,
         520.3972, 344.9123, 749.5062, 658.0609, 278.1974, 421.9219, 958.6487, 857.4978, 730.3324, 289.3745, 358.6215,
         698.7018, 133.0407, 167.9505, 291.9969, 578.2982, 749.7556, 484.5668, 932.4552, 539.0141, 212.5309, 240.0869,
         730.0189, 559.5427, 738.4392, 493.6140, 183.0709, 581.1377, 336.9068, 294.3034, 586.4559, 576.2549, 429.5497,
         147.0419, 124.4738, 170.3968, 669.1086, 500.9260, 289.0942, 255.8202, 208.5120, 366.5464, 636.1553, 803.9883,
         643.6326, 777.9428, 798.9828, 367.9909, 483.0508, 798.8464, 931.4518, 541.8273, 895.8802, 875.4196, 774.2717,
         892.6114, 407.7618, 276.9209, 187.1928, 952.4478, 355.5263, 247.1016, 748.7158, 822.4678, 209.4230, 552.4930,
         677.0270, 331.8404, 603.5925, 376.3231, 921.2878, 386.9958, 325.4662, ]


def get_inlet_num():

    while True:
        num = input("enter inlet number")
        if num.isdigit():
            num = int(num)
            return num
            break
        else:
            print("wrong input")
            continue


def get_sensor_num():

    while True:
        num = input("enter sensor number")
        if num.isdigit():
            num = int(num)
            return num
            break
        else:
            print("wrong input")
            continue


def test_sensor(array):
    # search the sensor on the medial axis
    approx = []
    on_axis = False
    for item in array:
        item_approx = int(item * 10)
        approx.append(item_approx)
        if approx.count(item_approx) >= 2:
            on_axis = True
    if on_axis:
        print(f'sensor on medial axis')
    else:
        print(f'sensor not on medial axis')


def select_file():
    root = tk.Tk()
    root.withdraw()
    File = filedialog.askopenfilename()
    # print(File)
    return File


def read_file():
    file_path = select_file()
    df = pd.read_csv(file_path, sep='\t', comment='#')
    # print(df)
    data = df.values[:, 0]
    # print(data)
    length = len(df)
    len_column = len(df.columns)
    i = 0
    j = 1
    time = []
    sensor = []
    while i < length:
        time.append(df.values[i, 0])
        i = i + 1
        # print(i)
    # print(time)
    while j < len_column - 1:
        n = 0
        while n < length:
            if df.values[n, j] > 100000.0:
                sensor.append(df.values[n, 0])
                break
            else:
                n = n + 1

        j = j + 1
    return sensor


def get_array():
    inlet = get_inlet_num()
    sensor=get_sensor_num()
    time_array = []
    print(time_array)
    i=0
    while i < inlet:
        ls=[]
        time_list = read_file()
        time_array=np.append(time_array,time_list,axis=0)
        print(time_array)
        i=i+1
    time_array=time_array.reshape(-1,sensor)
    print(time_array)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # get_axis()
    get_array()