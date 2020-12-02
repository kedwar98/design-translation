#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 12:15:39 2020

@author: gauss
"""
import os 
import pathlib
import shutil
from os import listdir
from os.path import isfile, join, isdir, split

# detect the current working directory and print it
path = os.getcwd()
print ("The current working directory is %s" % path)


#define new path of the directory to be created
new_path="/home/gauss/Kristen/design_translation/airplane_images"
try:
    os.mkdir(new_path)
except OSError:
    print ("Directory %s already exists"  % new_path)
else:
    print ("Successfully created the directory %s" % new_path)

# File to read in the airplane synset ID and then all of the images for that sysnet ID
airplane_synset='02691156'
 
#file path before it gets to airplane sysnet ID
file_path= "/home/gauss/Downloads/ShapeNetCore.v2/{}/".format(airplane_synset)

#model_dirs is a list of all of the model directories
model_dirs = [join(file_path, f) for f in listdir(file_path) if isdir(join(file_path, f))]
print("Made a list of {} model directories in the form: ".format(len(model_dirs)), model_dirs[0])

#make a list of all of the paths to the screenshots
image_dirs = [join(f, "screenshots") for f in model_dirs if isdir(join(f, "screenshots"))]
print("Made a list of {} image directories in the form: ".format (len(image_dirs)), image_dirs[0])


#now to sort the images into different folders based on orientation

# see if they all have the same number of files
num_of_files= [len(listdir(f)) for f in image_dirs]

# for loop that will put each of the 14 (0-13) images in the screenshots directory into the proper directory for each item in image_dirs
for i in image_dirs:
    model=os.path.split(i)[0]
    image_num=os.path.split(model)[1]
    # model=os.path.split(image_dirs[0])[0]
    # image_num=os.path.split(model)[1]
    if image_num != '8db0b83cee14e1e5eacd58bc9fc5db51':
        for j in range(14):
            image_string=image_num+'-{}.png'.format(j)
            screenshot_path=os.path.join(i,image_string)
            #screenshot_path=os.path.join(image_dirs[0],image_string)
            if j==0:
                new_scr_path=os.path.join(new_path,'face_left')
            elif j==1:
                new_scr_path=os.path.join(new_path,'face_right')
            elif j==2:
                new_scr_path=os.path.join(new_path,'bottom')
            elif j==3:
                new_scr_path=os.path.join(new_path,'top')
            elif j==4:
                new_scr_path=os.path.join(new_path,'front')
            elif j==5:
                new_scr_path=os.path.join(new_path,'back')
            else:
                new_scr_path=os.path.join(new_path,'{}pi4'.format(j))
            
            newPath = shutil.copy(screenshot_path,new_scr_path)