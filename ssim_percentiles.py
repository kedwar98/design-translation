# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:14:15 2021

@author: krist
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean, pstdev

ssim_percentiles=pd.read_excel('ssim_percentiles.xlsx', index_col=0)
ssim_scores=pd.read_excel('ssim_scores.xlsx', index_col=0)


perc_array=ssim_percentiles.to_numpy()
score_array=ssim_scores.to_numpy()

success_matrix=[]
for i in range(30,100):
    percentile_vals=ssim_percentiles.loc[i]
    #now you have a 6 element series 
    # of percentile scores for each orientation
    percentile_model_success=[]
    for j in range(0,252):
        model_vals=ssim_scores.loc[j]
        n=0
        for k in range(6):
            if model_vals[k]>=percentile_vals[k]:
                n+=1
        percentile_model_success.append(n)
    success_matrix.append(percentile_model_success)
success_array=np.array(success_matrix)

print('Shape of success_array is', success_array.shape)

#%% Make dataframe of success

success_df=pd.DataFrame(data=success_array, index=ssim_percentiles.index)
#%%
# success_matrix=[]
# for index in ssim_percentiles:
#     percentile_vals=row
#     #now you have a 6 element series 
#     # of percentile scores for each orientation
#     percentile_model_success=[]
#     for index in ssim_scores:
#         model_vals=row
#         n=0
#         for i in range(6):
#             if model_vals[i]>=percentile_vals[i]:
#                 n+=1
#         percentile_model_success.append(n)
#     success_matrix.append(percentile_model_success)


#%% Make histograms of success
i=30
for row in success_array:
    n, bins, patches = plt.hist(x=row, bins=7, color='#0504aa',
                            alpha=0.7, rwidth=0.85)
    avg=mean(row)
    std= pstdev(row,avg)
    
    title=('Histogram of Successes out of 6 for the {}th Percentile').format(i)
    plt.xlabel('Successes out of 6 Predicted Images')
    plt.ylabel('Number of Models')
    plt.title(title)
    # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    
    # plt.text(, 62, r'$\mu={}$'.format(round(avg, 3)))
    
    # plt.text(0., 55, r'$\sigma={}$'.format(round(std, 3)))
    plt.xlim(0,6.5)
    plt.ylim(0,252 )
    plt.grid(True)
    
    i+=1
    
    save_folder= join(join(path, 'percentile_success'),title)+'.png'
    plt.savefig(save_folder)
    
    plt.show()
    
    # print('Made plot for '+ column_names[i][8:-4] )

