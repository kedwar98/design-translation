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
#path = os.getcwd()
path='C:\\Users\\Gauss\\'
print ("The current working directory is %s" % path)


#define new path of the directory to be created containing the new directories for each test model_id
new_path=os.path.join( path , 'design-translation\\data\\predicted-images')

try:
    os.mkdir(new_path)
except OSError:
    print ("Directory %s already exists"  % new_path)
else:
    print ("Successfully created the directory %s" % new_path)

path_to_DATA=os.path.join(path, 'cross-domain-disen\\DATA\\')
path_to_model_id=os.path.join(path_to_DATA, 'combine_7pi4_front\\test' )

 
test_model_ids= listdir(path_to_model_id)

# %%

for f in test_model_ids:
    
    #make the new directories for each of the test cases within design-translation
    new_folder_path= os.path.join(new_path, f[:-4])
    try:
        os.mkdir(new_folder_path)
    except OSError:
        print ("Directory %s already exists"  % new_folder_path)
    else:
        print ("Successfully created the directory %s" % new_folder_path)
 
# %%
        
#fill the new directories with images from cross-domain-disen

#list of all of the 7pi4 models
combine_model=[]

for f in listdir(path_to_DATA):
    if f[:13]=='combine_7pi4_':
        combine_model.append(f)

#combine_model_dirs= [os.path.join(path_to_DATA, f) for f in combine_model]

#need to define the paths to the images -outputsX2Y, and the paths to the new locations

#%%
path_to_test= os.path.join(path, 'cross-domain-disen\\airplane_test\\')

#path to the individual combine_7pi4___ within airplane_test
combine_model_test_dirs=[join(path_to_test,f) for f in combine_model]

# for each of the model_ids (test_model_ids minus last 4 items) go through each 
# of the combine_model_test_dirs and find the file that has the same first 26 
# digits and outputsX2Y.png as the last 14 digits f[-14:], then take that file and use
# shutil.copy to copy it from its original path to its new path in design-translation

for f in test_model_ids:
    for model_dir in combine_model_test_dirs:
        model400_dir=join(model_dir, 'MODEL_400\\images')

        for a in listdir(model400_dir):
            if a[:26]==f[:26] and a[-14:]=='outputsX2Y.png':
                orig_test_path= os.path.join(model400_dir,a)
                new_test_path= os.path.join(new_path,a[:26])
                b=split(model_dir)[1]+'.png'
                new_test_path=join(new_test_path, b)
                shutil.copy(orig_test_path,new_test_path)
                
    



