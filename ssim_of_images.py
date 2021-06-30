# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:45:45 2021

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

actual_path= join(path,'renamed')
predicted_path= join(path,'predicted-images') 

#%%
#start with predicted images

ssimscores=[]
column_names=[]
row_names=[]
n=1

for i in listdir(predicted_path):
    #i = model_id
    row_names.append(i)
    row=[]
    more_pred_path=join(predicted_path,i)
    for j in listdir(more_pred_path):
        # j combine_7pi4_<***>.png
        # j orientation includes .png 
        orientation_id=j
        predicted_image=join(more_pred_path,orientation_id)
        
        more_actual_path=join(actual_path,orientation_id[13:-4])
        actual_image=join(more_actual_path,i)+'.png'

        # Find SSIM Score
        imageA= cv2.imread(actual_image)
        #actual image size is 512x512x3
        imageB=cv2.imread(predicted_image)
        #predicted image size is 256x256x3
        
        #change size of actual
        imageA=resize(imageA, (256,256))*255
        
        # change type of image A to uint8
        
        imageA=imageA.astype('uint8')
        
        #convert to gray (not always necessary)
        if to_gray:
            grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
            grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
            (score, diff) = structural_similarity(grayA, grayB, full=True, multichannel=False)
            print('Structural Similarity For Predicted vs. Actual Score for {}: '.format(i), score)   
        
        else:
            (score, diff) = structural_similarity(imageA, imageB, full=True, multichannel=True)
            print('Structural Similarity For Predicted vs. Actual Score for {}: '.format(i), score)
        row.append(score)
        if n==1:
            column_names.append(j)
            
    n=0
    ssimscores.append(row)
        
 #%% Visualizations

#They think there are 252 datasets, aka each row is a dataset

# all_sim is a flattened 1d list with 252*6=1512 elements
all_ssim= [j for sub in ssimscores for j in sub] 
n, bins, patches = plt.hist(x=all_ssim, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
avg=mean(all_ssim)
std= pstdev(all_ssim,avg)

title=('Histogram of All SSIM Scores')
plt.xlabel('SSIM Score')
plt.ylabel('Number of Models')
plt.title(title)
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')

plt.text(0.8, 176, r'$\mu={}$'.format(round(avg, 3)))

plt.text(0.8, 160, r'$\sigma={}$'.format(round(std, 3)))
plt.xlim(0.4, 1)
# plt.ylim(0, 0.03)
plt.grid(True)


save_folder= join(join(path, 'ssim_scores'),title)+'.png'
plt.savefig(save_folder)

plt.show()

#%% Visualizations for columns (orientations) and rows (models)

#turn ssimscores 2D list into numpy array
ssim_array=np.array(ssimscores)

a=['\u03C0/2','3\u03C0/4','\u03C0/4', 'Front','Left','Top']
df2=pd.DataFrame(data=ssim_array,columns=a, index=row_names)
#df2=pd.DataFrame(data=ssim_array,columns=a)

color = dict(boxes='k', whiskers='k', medians='r', caps='k')


boxplot = sns.violinplot(data= df2, palette="light:b", cut=0)

# boxplot= df2.violinplot(grid=False, rot=90, fontsize=10, color=color, showfliers=False,
#               boxprops=dict(linestyle='-', linewidth=1.5, color='#5877ff'),
#               flierprops=dict(linestyle='-', linewidth=1.5),
#               medianprops=dict(linestyle='-', linewidth=1.5, color='#5877ff'),
#               whiskerprops=dict(linestyle='-', linewidth=1.5, color='DarkBlue'),
#               capprops=dict(linestyle='-', linewidth=1.5, color='Darkblue') )

#this one works well
# boxplot= df2.boxplot(grid=False, rot=90, fontsize=10, color=color, showfliers=False,
#               boxprops=dict(linestyle='-', linewidth=1.5, color='#5877ff'),
#               flierprops=dict(linestyle='-', linewidth=1.5),
#               medianprops=dict(linestyle='-', linewidth=1.5, color='#5877ff'),
#               whiskerprops=dict(linestyle='-', linewidth=1.5, color='DarkBlue'),
#               capprops=dict(linestyle='-', linewidth=1.5, color='Darkblue') )


# boxplot = df2.plot(kind='box',
#              #color= dict(boxes='r', whiskers='DarkOrange', medians='k', caps='Gray'),
#              boxprops=dict(linestyle='-', linewidth=1.5),
#              flierprops=dict(linestyle='-', linewidth=1.5),
#              medianprops=dict(linestyle='-', linewidth=1.5),
#              whiskerprops=dict(linestyle='--', linewidth=1.5),
#              capprops=dict(linestyle='-', linewidth=1.5),
#              showfliers=False, grid=False, rot=45)
boxplot.set_ylim(bottom=0.4, top=1)
boxplot.set_xlim(left=-0.5, right=5.75)
boxplot.set_xlabel('Predicted Orientation')
boxplot.set_ylabel('SSIM Score')
boxplot.set_title('SSIM Scores per Predicted Orientation')

fs=9
plt.text(-0.25, 0.45, r'$\mu=0.854$', fontsize=fs)
plt.text(0.75, 0.45, r'$\mu=0.867$', fontsize=fs)
plt.text(1.75, 0.45, r'$\mu=0.876$', fontsize=fs)
plt.text(2.75, 0.45, r'$\mu=0.943$', fontsize=fs)
plt.text(3.75, 0.45, r'$\mu=0.910$', fontsize=fs)
plt.text(4.73, 0.45, r'$\mu=0.782$', fontsize=fs)
plt.show()
#df2.to_excel('ssim_scores.xlsx')

#%% 
i=0
for column in ssim_array.T:
    n, bins, patches = plt.hist(x=column, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
    avg=mean(column)
    std= pstdev(column,avg)
    
    title=('Histogram of {} SSIM Scores').format(column_names[i][8:-4])
    plt.xlabel('SSIM Score')
    plt.ylabel('Number of Models')
    plt.title(title)
    # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    
    plt.text(0.55, 62, r'$\mu={}$'.format(round(avg, 3)))
    
    plt.text(0.55, 55, r'$\sigma={}$'.format(round(std, 3)))
    plt.xlim(0.5, 1)
    plt.ylim(0, 75)
    plt.grid(True)
    
    
    save_folder= join(join(path, 'ssim_scores'),title)+'.png'
    plt.savefig(save_folder)
    
    plt.show()
    
    print('Made plot for '+ column_names[i][8:-4] )
    i+=1

#%% Percentiles for all data and each column (orientation)

percentile_matrix=[]
for column in ssim_array.T:
    percentile_row=[]
    for i in range(30,100,1):
        percentile_value=np.percentile(column,i)
        percentile_row.append(percentile_value)
    percentile_matrix.append(percentile_row)
    
percentile_array=np.array(percentile_matrix).T

#create dataframe of scores
a=np.arange(30,100,1)
df=pd.DataFrame(data=percentile_array,columns=column_names,index=a)

# df.to_excel('ssim_percentiles.xlsx')

#%% failure rates for models








        
    