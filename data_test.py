# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 13:28:11 2020

@author: analoganddigital   ( GitHub )
"""

import os
import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

file_name = 'training_data.npy'
if os.path.isfile(file_name):
    print("file exists , loading previous data")
    training_data = list(np.load(file_name,allow_pickle=True))

''' 
w=[]
a=[]
s=[]
d=[]
v=[]
j=[]
m=[]
k=[]
n_choise=[]
'''

w=[]
j=[]
m=[]
k=[]
r=[]
n_choise=[]

df = pd.DataFrame(training_data)
print(df.head())
print(Counter(df[1].apply(str)))    

for data in training_data:                  #[img,choice]    chose=[1,0,0,0,0,0]
    img = data[0]
    choise = data[1]
    '''
    if choise[0] == 1:
        w.append([img,choise])
    elif choise[1] == 1:
        a.append([img,choise])
    elif choise[2] == 1:
        s.append([img,choise])
    elif choise[3] == 1:
        d.append([img,choise])
    elif choise[4] == 1:
        v.append([img,choise])
    elif choise[5] == 1:
        j.append([img,choise])
    elif choise[6] == 1:
        m.append([img,choise])
    elif choise[7] == 1:
        k.append([img,choise])
    elif choise == [0,0,0,0,0,0,0,0]:
        n_choise.append([img,choise])
    '''
    '''
    if choise[0] == 1:
        w.append([img,choise])
    elif choise[1] == 1:
        j.append([img,choise])
    elif choise[2] == 1:
        m.append([img,choise])
    elif choise[3] == 1:
        k.append([img,choise])
    elif choise == [0,0,0,0]:
        n_choise.append([img,choise])
    '''
    
    if choise[0] == 1:
        w.append([img,choise])
    elif choise[1] == 1:
        j.append([img,choise])
    elif choise[2] == 1:
        m.append([img,choise])
    elif choise[3] == 1:
        k.append([img,choise])
    elif choise[4] == 1:
        r.append([img,choise])
    elif choise[5] == 1:
        n_choise.append([img,choise])
    
length=len(m)
#数据量按防御次数
'''
w=w[:length]
a=a[:length]
s=s[:length]
d=d[:length]
v=v[:length]
j=j[:length]
m=m[:length]
k=k[:length]
n_choise=n_choise[:length]


final_data = w+a+s+d+v+j+m+k+n_choise
'''

w=w[:length]
j=j[:length]
m=m[:length]
k=k[:length]
r=r[:length]
n_choise=n_choise[:length]


final_data = w+j+m+k+r+n_choise
shuffle(final_data)
print(len(final_data))
np.save('training_data_2_v2_2.npy',final_data)


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

