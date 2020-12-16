# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 22:29:37 2020

@author: krist
"""

import os 
import pathlib
import shutil
from os import listdir
from os.path import isfile, join, isdir, split

file_path='C:\\Users\\krist\\design-translation\\airplane-images'

#orientation_dirs is a list of all of the different orientation directories
orientation_dirs = [join(file_path, f) for f in listdir(file_path) if isdir(join(file_path, f))]
print("Made a list of {} orientation directories in the form: ".format(len(orientation_dirs)), orientation_dirs[0])

#make a list of all of the paths to the individual images, these will lead to files
for f in orientation_dirs:
    image_dirs = [join(f, k) for k in listdir(f) if isfile(join(f, k))]
    #print(listdir(f)[0])
    print("Made a list of {} image directories in the form: ".format (len(image_dirs)), image_dirs[0])
    break


#need to rename the files so the last few digits "-1.png" or "-13.png" are gone such that the images have the same name
#define new path where I want the new files to go
new_path='C:\\Users\\krist\\design-translation\\renamed'
try:
    os.mkdir(new_path)
except OSError:
    print ("Directory %s already exists"  % new_path)
else:
    print ("Successfully created the directory %s" % new_path)

#make the new folders for the renamed images
for f in listdir(file_path):
    old_path=join(file_path,f)
    renamed_path=join(new_path,f)
    #os.mkdir(renamed_path)
    for n in listdir(old_path):
        old_image_dir = join(old_path,n)
        new_name=n[:-8]
        new_name=new_name + '.png'
        renamed_image_dir=join(renamed_path,new_name)
        shutil.copyfile(old_image_dir,renamed_image_dir)
    

# #rename the images and put them in the 
# for f in image_dirs:
#     new_dir=f[:-8]
#     os.shutil(f,new_dir)
    