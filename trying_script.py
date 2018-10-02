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

file_name = 'CTL7_tono_voi_onRef_PAC_RH.txt'
my_data = import_function(file_name)
plot_2d(my_data,file_name)

xs = my_data[:,1]
ys = my_data[:,2]
zs = my_data[:,3]
fs = 14-my_data[:,7] 

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

p1minusp2 = [x1 - x2 for (x1, x2) in zip(p1, p2)]
p1minusp3 = [x1 - x2 for (x1, x2) in zip(p1, p3)]
print(p1minusp2,p1minusp3)

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

        

