# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 22:53:11 2021

@author: krist
"""

import numpy as np
import pandas as pd
# from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity
import cv2
import matplotlib.pyplot as plt
#import imutils
import os 
from os import listdir
from os.path import isfile, join, isdir, split

from center_image import new_image

original_path='FirstRoundDataset'

orientations=[join(original_path, f) for f in listdir(original_path) if isdir(join(original_path, f))]
#model_dirs = [join(file_path, f) for f in listdir(file_path) if isdir(join(file_path, f))]

for i in orientations:
    for j in listdir(i): 
        path=join(i,j)
        centered=new_image(path)
        new_path=join(join('centered',i),j)
        
        cv2.imwrite(new_path,centered)