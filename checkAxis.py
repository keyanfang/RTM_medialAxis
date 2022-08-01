import tkinter as tk
from tkinter import filedialog
import numpy as np


import pandas as pd


def get_inlet_num():
    while True:
        num = input("enter inlet number")
        if num.isdigit():
            num = int(num)
            return num
        else:
            print("wrong input")
            continue


def get_sensor_num():
    while True:
        num = input("enter sensor number")
        if num.isdigit():
            num = int(num)
            return num
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
        return True
    else:
        print(f'sensor not on medial axis')
        return False


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
            if df.values[n, j] != df.values[0, j]:
                sensor.append(df.values[n - 1, 0])
                break
            else:
                n = n + 1

        j = j + 1
    return sensor


def get_matrix():
    inlet = get_inlet_num()
    sensor = get_sensor_num()
    time_array = []
    i = 0
    while i < inlet:
        ls = []
        time_list = read_file()
        time_array = np.append(time_array, time_list, axis=0)
        # print(time_array)
        i = i + 1
    time_array = time_array.reshape(-1, sensor)
    print(time_array)
    return time_array


def get_axis():
    matrix = get_matrix()
    inlet_sum = get_inlet_num()
    sensor_sum = get_sensor_num()
    sensor_num = 0
    axis_num = []
    while sensor_num < sensor_sum:
        inlet_num = 0
        array = []
        while inlet_num < inlet_sum:
            for i in matrix:
                array.append(i[sensor_num])
                inlet_num = inlet_num + 1
        print(array)
        if test_sensor(array):
            print(sensor_num)
            axis_num.append(sensor_num + 1)
            sensor_num = sensor_num + 1
        else:
            sensor_num = sensor_num + 1
    print(axis_num)
    return axis_num


def get_sensor_location(array):
    file_path = select_file()
    df = pd.read_csv(file_path, sep='\t', comment='#')
    data=np.array(df)
    print(data)
    for i in array:
        print(data[i-1])