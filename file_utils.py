# # -*- coding: UTF-8 -*-


# 保证脚本与Python3兼容
from __future__ import print_function
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

import tensorflow as tf
import numpy as np
import pandas as pd

def read_dir(dir='/home/work/opdir/liuguilin1/ecp/data/train/'):
    files =  os.listdir(dir)
    res = pd.DataFrame()
    for file_name in files:
        print(file_name)
        file_path = os.path.join(dir, file_name)
        print(file_path)
        df = pd.read_csv(file_path)
        res = res.append(df)
        print(file_name)
        print(res.shape)
    print(res.shape)
    x_vals = res.iloc[:,1:]
    y_vals = res.iloc[:,0]
    return (x_vals,y_vals)

read_dir()