# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:12:12 2020

@author: analoganddigital   ( GitHub )
"""

import numpy as np
from Alexnet import alexnet2
from random import shuffle
import pandas as pd

# what to start at
START_NUMBER = 60

# what to end at
hm_data = 111

# use a previous model to begin?
START_FRESH = False

WIDTH = 96
HEIGHT = 86
LR = 1e-3
EPOCHS = 20
MODEL_NAME = 'model_sekiro_1/py-sekiro-{}-{}-{}-epochs.model'.format(LR,'alexnetv2',EPOCHS)
EXISTING_MODEL_NAME = 'model_sekiro_1/py-sekiro-{}-{}-{}-epochs.model'.format(LR,'alexnetv2',EPOCHS)
file_name = 'training_data_2_v2.npy'

model = alexnet2(WIDTH, HEIGHT, LR)


if not START_FRESH:
    model.load(EXISTING_MODEL_NAME)

for i in range(EPOCHS):
    '''
    data_order = [i for i in range(START_NUMBER,hm_data+1)]
    shuffle(data_order)
    for i in data_order:
        train_data = np.load(file_name,allow_pickle=True)
        
        df = pd.DataFrame(train_data)
        df = df.iloc[np.random.permutation(len(df))]
        train_data = df.values.tolist()
    '''
    train_data = np.load(file_name,allow_pickle=True)
    train = train_data[:-3000]
    test = train_data[-3000:]

    X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
    Y = [i[1] for i in train]

    test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
    test_y = [i[1] for i in test]

    model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
        snapshot_step=2500, show_metric=True, run_id=MODEL_NAME)

    model.save(MODEL_NAME)

# tensorboard --logdir=foo:C:/Users/H/Desktop/ai-gaming-phase5/log