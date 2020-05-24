# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:29:20 2020

@author: analoganddigital   ( GitHub )
"""

import numpy as np
from grabscreen import grab_screen
import cv2
import time
import directkeys
from Alexnet import alexnet2
from getkeys import key_check
import random

WIDTH = 96
HEIGHT = 86
LR = 1e-3
EPOCHS = 20
MODEL_NAME = 'model_sekiro_1/py-sekiro-{}-{}-{}-epochs.model'.format(LR,'alexnetv2',EPOCHS)

#w j m k none

w = [1,0,0,0,0,0]
j = [0,1,0,0,0,0]
m = [0,0,1,0,0,0]
k = [0,0,0,1,0,0]
r = [0,0,0,0,1,0]
n_choise = [0,0,0,0,0,1]

model = alexnet2(WIDTH, HEIGHT, LR, output = 6)
model.load(MODEL_NAME)

window_size = (320,104,704,448)#384,224  192,112 96,86

def main():
    last_time = time.time()
    for i in list(range(5))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    while(True):
        
        if not paused:
            # 800x600 windowed mode
            screen = grab_screen(region=(window_size))
            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (WIDTH,HEIGHT))

            prediction = model.predict([screen.reshape(WIDTH,HEIGHT,1)])[0]
            print(prediction)
            
            print("np后的预测:",np.argmax(prediction))

            if np.argmax(prediction) == np.argmax(w):
                print("前")
                directkeys.go_forward()
            elif np.argmax(prediction) == np.argmax(j):
                print("攻击")
                directkeys.attack()
            elif np.argmax(prediction) == np.argmax(m):
                print("防御")
                directkeys.define()
            elif np.argmax(prediction) == np.argmax(k):
                print("跳")
                directkeys.jump()
            elif np.argmax(prediction) == np.argmax(r):
                print("识破")
                directkeys.dodge()
            elif np.argmax(prediction) == np.argmax(n_choise):
                print("不动")
            
        keys = key_check()

        # p pauses game and can get annoying.
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                '''
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                '''
                time.sleep(1)
        if 'Y' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                '''
                directkeys.ReleaseKey(J)
                directkeys.ReleaseKey(W)
                directkeys.ReleaseKey(M)
                directkeys.ReleaseKey(K)
                '''
                time.sleep(1)
                break

main()  