# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 12:22:04 2021

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
from skimage.transform import rescale, resize, downscale_local_mean
from statistics import mean, quantiles, pstdev
import matplotlib.pyplot as plt
import seaborn as sns

to_gray=True
path=os.getcwd()

actual_path= join(path,'renamed\\7pi4')
sketch_path= join(path,'sketch') 

#%%

for i in listdir(actual_path):
    #i = model_id
    actual_image=join(actual_path,i)


#%%
    # Make sketch image
    imageA= cv2.imread(actual_image)
    #actual image size is 512x512x3
    
    # #change size of actual
    # imageA=resize(imageA, (256,256))*255
    # # change type of image A to uint8
    # imageA=imageA.astype('uint8')
    
    #make gray image
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    
    inverted_gray_image = 255 - grayA
    blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21),0)
    inverted_blurred_img = 255 - blurred_img
    pencil_sketch_IMG = cv2.divide(grayA, inverted_blurred_img, scale = 256.0)
    #Show the original image
    # cv2.imshow('Original Image', imageA)
    # #Show the new image pencil sketch
    # cv2.imshow('Pencil Sketch', pencil_sketch_IMG)
    # #Display the window infinitely until any keypress
    # cv2.waitKey(0)
    filename= join(sketch_path,i)
    cv2.imwrite(filename, pencil_sketch_IMG)
    
