# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 09:46:51 2018

@author: Giorgia
"""

import numpy as np
from numpy.linalg import det, norm
import matplotlib.pyplot as plt
from import_function import *
import scipy.io

plt.close('all')

# plot bysecting line
ctl_number = 1
ctl_3D_data = np.ones([ctl_number,4,1500])*(-2)
ctl_list = ['CTL1_tono_voi_onRef_PAC_RH.txt','CTL1_tono_voi_onRef_PAC_LH.txt']

for i in range(ctl_number):
    #mydata = import_function(ctl_list[i])
    mydata = scipy.io.loadmat('CTL1_tono_poi_PAC_LH.mat')['data']
    max_len = np.shape(mydata)[0]
    # import x
    ctl_3D_data[i,0,0:max_len] = mydata[:,1]
    # import y
    ctl_3D_data[i,1,0:max_len] = mydata[:,2]
    # import z
    ctl_3D_data[i,2,0:max_len] = mydata[:,3]
    # import f
    ctl_3D_data[i,3,0:max_len] = 14-mydata[:,7]

data = ctl_3D_data[0,:,:]

xs,ys,zs,fs = organize_data(data) 

min_xs = np.nanmin(xs)
max_xs = np.nanmax(xs)
min_ys = np.nanmin(ys)
max_ys = np.nanmax(ys)
pixels = 24

xs_array = np.linspace(min_xs,max_xs,pixels)
ys_array = np.linspace(min_ys,max_ys,pixels)

# initialize the table
table = np.zeros([pixels,pixels])
keep_trace = np.zeros_like(table)
# fill the table with the mean of the frequency at that location
for k in range(len(xs)):
    idx_x = (np.abs(xs_array-xs[k])).argmin()
    idx_y = (np.abs(ys_array-ys[k])).argmin()
    table[idx_x,idx_y] += fs[k]
    keep_trace[idx_x,idx_y] += 1
for i in range(pixels):   # divide by the number of frequencies added, or if none, substitute with -2 to indicate no pixels there
    for j in range(pixels):
        if keep_trace[i,j] != 0:
            table[i,j] = table[i,j]/keep_trace[i,j]
        else:
            table[i,j] = -2

plt.figure()
plt.imshow(table,cmap = 'jet')
