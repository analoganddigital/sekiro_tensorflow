# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:04:12 2020

@author: analoganddigital   ( GitHub )
"""

import os
import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

file_name_1 = 'training_data_1_v2_c.npy'
if os.path.isfile(file_name_1):
    print("file exists , loading previous data")
    training_data_1 = list(np.load(file_name_1,allow_pickle=True))

file_name_2 = 'training_data_2_v2_c.npy'
if os.path.isfile(file_name_2):
    print("file exists , loading previous data")
    training_data_2 = list(np.load(file_name_2,allow_pickle=True))
    
final_data = training_data_1+training_data_2
shuffle(final_data)
print(len(final_data))
np.save('training_data_2_v2.npy',final_data)


'''
for data in training_data:
    img = data[0]
    choice = data[1]
    cv2.imshow('test',img)
    print(choice)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.waitKey()# 视频结束后，按任意键退出
cv2.destroyAllWindows()
'''

df = pd.DataFrame(final_data)
print(df.head())
print(Counter(df[1].apply(str)))