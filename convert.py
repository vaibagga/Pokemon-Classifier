## data to h5py format

import os
import cv2
import numpy as np
import pandas as pd

DATAPATH = 'C:\\Users\\lenovo\\Desktop\\All\\Docs\\Pokemon2\\pokemon-classifier\\dataset'
CACHE = 'C:\\Users\\lenovo\\Desktop\\All\\Docs\\Pokemon2\\pokemon-classifier\\cache'
imagesCache = []
labelCache = []
SIZE = (28, 28)

def allImages(DATAPATH = DATAPATH):
	os.chdir(DATAPATH)
	for j in os.listdir():
		os.chdir(os.path.join(DATAPATH, _))
		for i in os.listdir():
			i = cv2.resize(cv2.imread(i), SIZE) 
			imagesCache.append(i)
			labelCache.append(j)

	return imagesCache, labelCache

train = pd.DataFrame()
train["X"], train["Y"] = allImages(DATAPATH)
os.chdir(CACHE)
print(train["X"][10].shape)
train.to_csv('data.csv')
