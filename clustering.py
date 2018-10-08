# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 15:32:05 2018

@author: Giorgia
"""

import numpy as np
from numpy.linalg import det, norm
import matplotlib.pyplot as plt
from import_function import *
from sklearn.cluster import DBSCAN

plt.close('all')

ctl_number = 1
ctl_3D_data = np.ones([ctl_number,4,1000])*(-2)
ctl_list = ['CTL1_tono_voi_onRef_PAC_RH.txt','CTL1_tono_voi_onRef_PAC_LH.txt']

for i in range(ctl_number):
    mydata = import_function(ctl_list[i])
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
until = list(data[3,:]).index(-2)
xs = data[0,0:until]
ys = data[1,0:until]
zs = data[2,0:until]
fs = 14-data[3,0:until] 

# useful function
get_indexes = lambda x, x_s: [i for (y, i) in zip(x_s, range(len(x_s))) if x == y]
# set the ranges
f_low = [14,13,12,11,10]
f_medium = [9,8,7,6]
f_high = [5,4,3,2,1]
idx_low = []
idx_medium = []
idx_high = []
for i in f_low:
    idx_i = get_indexes(i,fs)
    idx_low = np.concatenate((idx_low,idx_i))
idx_low = [int(item) for item in idx_low]
xs_flow = [xs[i] for i in idx_low]
ys_flow = [ys[i] for i in idx_low]
for i in f_medium:
    idx_i = get_indexes(i,fs)
    idx_medium = np.concatenate((idx_medium,idx_i))
idx_medium = [int(item) for item in idx_medium]
xs_fmedium = [xs[i] for i in idx_medium]
ys_fmedium = [ys[i] for i in idx_medium]
for i in f_high:
    idx_i = get_indexes(i,fs)
    idx_high = np.concatenate((idx_high,idx_i))
idx_high = [int(item) for item in idx_high]
xs_fhigh = [xs[i] for i in idx_high]
ys_fhigh = [ys[i] for i in idx_high]

plot_y_n = False
if plot_y_n:
    plt.figure()
    plt.plot(xs_flow,ys_flow,'o',color = 'red',label = 'low frequency')
    plt.plot(xs_fmedium,ys_fmedium,'o',color = 'yellow', label = 'medium frequency')
    plt.plot(xs_fhigh,ys_fhigh,'o', color = 'blue', label = 'high frequency')
    #plt.xlabel('x coordinate')
    #plt.ylabel('y coordinate')
    plt.legend()
    plt.title('Three ranges')
    plt.show()
    
plot_separate = True
if plot_separate:
    plt.figure()
    plt.plot(xs_flow,ys_flow,'o',color = 'red',label = 'low frequency')
    plt.legend()
    plt.title('Low freq')
    plt.show()
    
    plt.figure()
    plt.plot(xs_fmedium,ys_fmedium,'o',color = 'yellow',label = 'medium frequency')
    plt.legend()
    plt.title('Medium freq')
    plt.show()
    
    plt.figure()
    plt.plot(xs_fhigh,ys_fhigh,'o',color = 'blue',label = 'high frequency')
    plt.legend()
    plt.title('High freq')
    plt.show()

coord_low = np.zeros([len(xs_flow),2])
coord_low[:,0] = xs_flow
coord_low[:,1] = ys_flow

clustering = DBSCAN(eps=1.5, min_samples=3).fit(coord_low)
labels = clustering.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)

# Plot results (Black removed and is used for noise instead)
X = coord_low
core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
core_samples_mask[clustering.core_sample_indices_] = True
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
plt.figure()
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = (labels == k)

    xy = X[class_member_mask & core_samples_mask]
    
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=14)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()