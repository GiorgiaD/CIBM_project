# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 13:31:18 2018
@author: Giorgia
"""
import numpy as np
from numpy.linalg import det, norm
import matplotlib.pyplot as plt
from import_function import *

plt.close('all')

file_name = 'CTL7_tono_voi_onRef_PAC_LH.txt'
my_data = import_function(file_name)
plot_2d(my_data,file_name)

xs = my_data[:,1]
ys = my_data[:,2]
zs = my_data[:,3]
fs = 14-my_data[:,7] 

# plot bysecting line
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

get_indexes = lambda x, x_s: [i for (y, i) in zip(x_s, range(len(x_s))) if x == y]

idx_bordeaux = get_indexes(13,fs)
idx_red = get_indexes(12,fs)

xs_red = [xs[i] for i in idx_red]
xs_bordeaux = [xs[i] for i in idx_bordeaux]
xs_high = np.concatenate((xs_red,xs_bordeaux))
ys_red = [ys[i] for i in idx_red]
ys_bordeaux = [ys[i] for i in idx_bordeaux]
ys_high = np.concatenate((ys_red,ys_bordeaux))

if len(xs_high) < 140:
    print('consider orange too')
    idx_orange = get_indexes(11,fs)
    xs_orange = [xs[i] for i in idx_orange]
    ys_orange = [ys[i] for i in idx_orange]
    xs_high = np.concatenate((xs_high,xs_orange))
    ys_high = np.concatenate((ys_high,ys_orange))


#plt.plot(xs_high,ys_high,'o')
coeff = np.polyfit(xs_high,ys_high,1)

x_fit = np.arange(np.min(xs),np.max(xs),0.01)
y_fit = x_fit*coeff[0]+coeff[1]
uno = [1]*len(xs_red)
due = [2]*len(xs_bordeaux)

w = np.concatenate((uno,due))
if len(xs_red)+len(xs_bordeaux) < 140:
    w = np.concatenate((w,[0.5]*len(xs_orange)))
coeff_w = np.polyfit(xs_high,ys_high,deg = 1, w = w)
y_fit_w = x_fit*coeff_w[0]+coeff_w[1]

plt.plot(x_fit,y_fit,'k',label = 'linear fit')
plt.plot(x_fit,y_fit_w,'b',label = 'weighted fit')
plt.legend()
plt.show()

# here check for each frequency the mean distance from the line
p1_x = 0
p1_y = coeff_w[1]
p2_x = 1
p2_y = coeff_w[0]+coeff_w[1] 
p1 = [0,coeff_w[1]]
p2 = [1,coeff_w[0]+coeff_w[1]]
mean_dist = np.zeros(14)
above_line = np.zeros(14)
below_line = np.zeros(14)
max_dist = 0


for i in range(14):
    idx = get_indexes(i,fs)
    xs_idx = [xs[i] for i in idx]
    ys_idx = [ys[i] for i in idx]
    dist = 0
    if not idx:
        mean_dist[i] = 0
    else:
        for j in range(len(idx)):
            P = [xs_idx[j], ys_idx[j]]
            p1minusp2 = [x1 - x2 for (x1, x2) in zip(p1, p2)]
            p1minusP = [x1 - x2 for (x1, x2) in zip(p1, P)]
            dist += norm(np.cross(p1minusp2, p1minusP))/norm(p1minusp2)
            max_dist = np.max([dist,max_dist])
            
        mean_dist[i] = dist/len(idx)
        
        for j in range(len(idx)):
            P = [xs_idx[j], ys_idx[j]]
            p1minusp2 = [x1 - x2 for (x1, x2) in zip(p1, p2)]
            p1minusP = [x1 - x2 for (x1, x2) in zip(p1, P)]
            dist += norm(np.cross(p1minusp2, p1minusP))/norm(p1minusp2)
            if dist <=max_dist:
                if ys_idx[j] > xs_idx[j]*coeff_w[0]+coeff_w[1]:
                    above_line[i]+=1
                else:
                    below_line[i]+=1
        
plt.figure()
plt.plot(mean_dist,'o')
plt.xlabel('Frequency')
plt.ylabel('Mean distance')
plt.title('Average distance from line for all frequencies')

print(list(reversed(np.arange(14))))

plt.figure()
plt.plot(above_line,'ro', label = 'voxels above line')
plt.plot(below_line,'bo', label = 'voxels below line')
plt.scatter(np.arange(14),[-5]*14,marker = '*',c = list((np.arange(14))), cmap = 'jet')
plt.xlabel('Frequency')
plt.ylabel('Number of voxels')
plt.legend()
plt.show()

# Divide high, mean, low frequency
# set the data
data = ctl_3D_data[0,:,:]
until = list(data[3,:]).index(-2)
xs = data[0,0:until]
ys = data[1,0:until]
zs = data[2,0:until]
fs = data[3,0:until] 
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





