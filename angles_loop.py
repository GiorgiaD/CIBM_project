# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 09:24:49 2018

@author: Giorgia
"""

import numpy as np
from numpy.linalg import det, norm
import matplotlib.pyplot as plt
from import_function import *
from sklearn.cluster import DBSCAN

plt.close('all')
plot_y_n = False

ctl_list = ['CTL1_tono_voi_onRef_PAC_RH.txt','CTL1_tono_voi_onRef_PAC_LH.txt',
             'CTL2_tono_voi_onRef_PAC_RH.txt','CTL2_tono_voi_onRef_PAC_LH.txt',
             'CTL3_tono_voi_onRef_PAC_RH.txt','CTL3_tono_voi_onRef_PAC_LH.txt',
             'CTL4_tono_voi_onRef_PAC_RH.txt','CTL4_tono_voi_onRef_PAC_LH.txt',
             'CTL5_tono_voi_onRef_PAC_RH.txt','CTL5_tono_voi_onRef_PAC_LH.txt',
             'CTL6_tono_voi_onRef_PAC_RH.txt','CTL6_tono_voi_onRef_PAC_LH.txt',
             'CTL7_tono_voi_onRef_PAC_RH.txt','CTL7_tono_voi_onRef_PAC_LH.txt',
             'CTL8_tono_voi_onRef_PAC_RH.txt','CTL8_tono_voi_onRef_PAC_LH.txt',
             'CTL9_tono_voi_onRef_PAC_RH.txt','CTL9_tono_voi_onRef_PAC_LH.txt',
             'CTL10_tono_voi_onRef_PAC_RH.txt','CTL10_tono_voi_onRef_PAC_LH.txt',
             'CTL12_tono_voi_onRef_PAC_RH.txt','CTL12_tono_voi_onRef_PAC_LH.txt',
             'CTL13_tono_voi_onRef_PAC_RH.txt','CTL13_tono_voi_onRef_PAC_LH.txt']

pt_list = ['PT1_tono_voi_onRef_PAC_RH.txt','PT1_tono_voi_onRef_PAC_LH.txt',
           'PT2_tono_voi_onRef_PAC_RH.txt','PT2_tono_voi_onRef_PAC_LH.txt',
           'PT3_tono_voi_onRef_PAC_RH.txt','PT3_tono_voi_onRef_PAC_LH.txt',
           'PT4_tono_voi_onRef_PAC_RH.txt','PT4_tono_voi_onRef_PAC_LH.txt',
           'PT5_tono_voi_onRef_PAC_RH.txt','PT5_tono_voi_onRef_PAC_LH.txt',
           'PT6_tono_voi_onRef_PAC_RH.txt','PT6_tono_voi_onRef_PAC_LH.txt',
           'PT7_tono_voi_onRef_PAC_RH.txt','PT7_tono_voi_onRef_PAC_LH.txt',
           'PT8_tono_voi_onRef_PAC_RH.txt','PT8_tono_voi_onRef_PAC_LH.txt',
           'PT9_tono_voi_onRef_PAC_RH.txt','PT9_tono_voi_onRef_PAC_LH.txt',
           'PT10_tono_voi_onRef_PAC_RH.txt','PT10_tono_voi_onRef_PAC_LH.txt',
           'PT11_tono_voi_onRef_PAC_RH.txt','PT11_tono_voi_onRef_PAC_LH.txt',
           'PT12_tono_voi_onRef_PAC_RH.txt','PT12_tono_voi_onRef_PAC_LH.txt',
           'PT13_tono_voi_onRef_PAC_RH.txt','PT13_tono_voi_onRef_PAC_LH.txt',
           'PT14_tono_voi_onRef_PAC_RH.txt','PT14_tono_voi_onRef_PAC_LH.txt',
           'PT15_tono_voi_onRef_PAC_RH.txt','PT15_tono_voi_onRef_PAC_LH.txt',
           'PT16_tono_voi_onRef_PAC_RH.txt','PT16_tono_voi_onRef_PAC_LH.txt',
           'PT17_tono_voi_onRef_PAC_RH.txt','PT17_tono_voi_onRef_PAC_LH.txt',
           'PT18_tono_voi_onRef_PAC_RH.txt','PT18_tono_voi_onRef_PAC_LH.txt',
           'PT19_tono_voi_onRef_PAC_RH.txt','PT19_tono_voi_onRef_PAC_LH.txt',
           'PT20_tono_voi_onRef_PAC_RH.txt','PT20_tono_voi_onRef_PAC_LH.txt',
           'PT21_tono_voi_onRef_PAC_RH.txt','PT21_tono_voi_onRef_PAC_LH.txt',
           'PT22_tono_voi_onRef_PAC_RH.txt','PT22_tono_voi_onRef_PAC_LH.txt',
           'PT23_tono_voi_onRef_PAC_RH.txt','PT23_tono_voi_onRef_PAC_LH.txt',
           'PT24_tono_voi_onRef_PAC_RH.txt','PT24_tono_voi_onRef_PAC_LH.txt']

# IMPORT DATA
# work with Controls
ctl_number = np.shape(ctl_list)[0]
ctl_3D_data = np.ones([ctl_number,4,1000])*(-2)

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
    
# work with Patients
pt_number = np.shape(pt_list)[0]
pt_3D_data = np.ones([pt_number,4,1000])*(-2)

for i in range(pt_number):
    mydata = import_function(pt_list[i])
    max_len = np.shape(mydata)[0]
    # import x
    pt_3D_data[i,0,0:max_len] = mydata[:,1]
    # import y
    pt_3D_data[i,1,0:max_len] = mydata[:,2]
    # import z
    pt_3D_data[i,2,0:max_len] = mydata[:,3]
    # import f
    pt_3D_data[i,3,0:max_len] = 14-mydata[:,7]
    
    
# angles    
angle_ctl = np.zeros(ctl_number)
angle_pt = np.zeros(pt_number)

for i in range(ctl_number):
    data = ctl_3D_data[i,:,:]
    until = list(data[3,:]).index(-2)
    xs = data[0,0:until]
    ys = data[1,0:until]
    zs = data[2,0:until]
    fs = data[3,0:until] 
    
    # bisecting line
    coeff_w = bysect_line(data, 'Control 8', False) 
    
    # useful function
    get_indexes = lambda x, x_s: [i for (y, i) in zip(x_s, range(len(x_s))) if x == y]
    
    # find closest low
    idx_low = get_indexes(14,fs)  # look for lowest possible frequency
    if not idx_low: # if there are no voxels go to the following low freq
        idx_low = get_indexes(13,fs)
        if not idx_low:
            idx_low = get_indexes(12,fs)
            if not idx_low:
                idx_low = get_indexes(11,fs)
                if not idx_low:
                    idx_low = get_indexes(10,fs)
    xs_low = [xs[i] for i in idx_low]
    ys_low = [ys[i] for i in idx_low]
    # compute distance from line
    p1 = [0,coeff_w[1]]
    p2 = [1,coeff_w[0]+coeff_w[1]]
    min_dist = 1000
    xs_min = 0
    ys_min = 0
    
    for j in range(len(idx_low)):
        P = [xs_low[j], ys_low[j]]
        p1minusp2 = [x1 - x2 for (x1, x2) in zip(p1, p2)]
        p1minusP = [x1 - x2 for (x1, x2) in zip(p1, P)]
        dist = norm(np.cross(p1minusp2, p1minusP))/norm(p1minusp2)
        if dist < min_dist:
            xs_min = xs_low[j]
            ys_min = ys_low[j]
        elif dist == min_dist:
            xs_min = np.concatenate((xs_min,xs_low[j]))
            ys_min = np.concatenate((ys_min,ys_low[j]))
        min_dist = np.min([dist,min_dist])
        
    # find the two furthest high
    idx_high = get_indexes(1,fs)  # look for lowest possible frequency
    if not idx_high: # if there are no voxels go to the following low freq
        idx_high = get_indexes(2,fs)
        if not idx_high:
            idx_high = get_indexes(3,fs)
            if not idx_high:
                idx_high = get_indexes(4,fs)
    xs_high = [xs[i] for i in idx_high]
    ys_high = [ys[i] for i in idx_high]
    # compute distance from line
    max_dist_above = 0
    max_dist_below = 0
    xs_max_above = 0
    ys_max_above = 0
    xs_max_below = 0
    ys_max_below = 0
    
    for j in range(len(idx_high)):
        P = [xs_high[j], ys_high[j]]
        p1minusp2 = [x1 - x2 for (x1, x2) in zip(p1, p2)]
        p1minusP = [x1 - x2 for (x1, x2) in zip(p1, P)]
        dist = norm(np.cross(p1minusp2, p1minusP))/norm(p1minusp2)
        if ys_high[j] > xs_high[j]*coeff_w[0]+coeff_w[1]:  # above the line
            if dist > max_dist_above:
                xs_max_above = xs_high[j]
                ys_max_above = ys_high[j]
            elif dist == max_dist_above:
                xs_max_above = np.concatenate((xs_max_above,xs_high[j]))
                ys_max_above = np.concatenate((ys_max_above,ys_high[j]))
            max_dist_above = np.max([dist,max_dist_above])
        else:
            if dist > max_dist_below:
                xs_max_below = xs_high[j]
                ys_max_below = ys_high[j]
            elif dist == max_dist_below:
                xs_max_below = np.concatenate((xs_max_below,xs_high[j]))
                ys_max_below = np.concatenate((ys_max_below,ys_high[j]))
            max_dist_below = np.max([dist,max_dist_below])
            
    if max_dist_below*max_dist_above == 0:
        idx_high = get_indexes(5,fs) 
        if not idx_high:
            idx_high = get_indexes(6,fs)
        xs_high = [xs[i] for i in idx_high]
        ys_high = [ys[i] for i in idx_high]
        if max_dist_above == 0:
            for j in range(len(idx_high)):
                P = [xs_high[j], ys_high[j]]
                p1minusp2 = [x1 - x2 for (x1, x2) in zip(p1, p2)]
                p1minusP = [x1 - x2 for (x1, x2) in zip(p1, P)]
                dist = norm(np.cross(p1minusp2, p1minusP))/norm(p1minusp2)
                if ys_high[j] > xs_high[j]*coeff_w[0]+coeff_w[1]:  # above the line
                    if dist > max_dist_above:
                        xs_max_above = xs_high[j]
                        ys_max_above = ys_high[j]
                    elif dist == max_dist_above:
                        xs_max_above = np.concatenate((xs_max_above,xs_high[j]))
                        ys_max_above = np.concatenate((ys_max_above,ys_high[j]))
                    max_dist_above = np.max([dist,max_dist_above])
        if max_dist_below == 0:
            for j in range(len(idx_high)):
                P = [xs_high[j], ys_high[j]]
                p1minusp2 = [x1 - x2 for (x1, x2) in zip(p1, p2)]
                p1minusP = [x1 - x2 for (x1, x2) in zip(p1, P)]
                dist = norm(np.cross(p1minusp2, p1minusP))/norm(p1minusp2)
                if ys_high[j] < xs_high[j]*coeff_w[0]+coeff_w[1]:  # above the line
                    if dist > max_dist_below:
                        xs_max_below = xs_high[j]
                        ys_max_below = ys_high[j]
                    elif dist == max_dist_below:
                        xs_max_below = np.concatenate((xs_max_below,xs_high[j]))
                        ys_max_below = np.concatenate((ys_max_below,ys_high[j]))
                    max_dist_below = np.max([dist,max_dist_below])
                    
                    
    a = np.array([xs_max_above, ys_max_above,0.])
    b = np.array([xs_min, ys_min, 0.])
    c = np.array([xs_max_below, ys_max_below, 0.])
    
    ba = a - b
    bc = c - b
    
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)            
    
    angle_ctl[i] = np.degrees(angle)
    
    if plot_y_n:            
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(xs,ys, c = fs, cmap = 'jet', alpha = 0.4)    
        plt.plot(xs_min,ys_min,'k*',markersize = 20, label = 'closest low')
        plt.plot(xs_max_above,ys_max_above,'ko',markersize = 18,label = 'highest high above')
        plt.plot(xs_max_below,ys_max_below,'ko',markersize = 18,label = 'highest high below')
        plt.title('Find angle')
        plt.legend(loc = 'upper right')
        plt.show()

plt.figure()
plt.hist(angle_ctl)
plt.title('CONTROLS')
plt.xlabel('Angle')
plt.ylabel('Occurrency')

for i in range(pt_number):
    data = pt_3D_data[i,:,:]
    until = list(data[3,:]).index(-2)
    xs = data[0,0:until]
    ys = data[1,0:until]
    zs = data[2,0:until]
    fs = data[3,0:until] 
    
    # bisecting line
    coeff_w = bysect_line(data, 'Control 8', False) 
    
    # useful function
    get_indexes = lambda x, x_s: [i for (y, i) in zip(x_s, range(len(x_s))) if x == y]
    
    # find closest low
    idx_low = get_indexes(14,fs)  # look for lowest possible frequency
    if not idx_low: # if there are no voxels go to the following low freq
        idx_low = get_indexes(13,fs)
        if not idx_low:
            idx_low = get_indexes(12,fs)
            if not idx_low:
                idx_low = get_indexes(11,fs)
                if not idx_low:
                    idx_low = get_indexes(10,fs)
    xs_low = [xs[i] for i in idx_low]
    ys_low = [ys[i] for i in idx_low]
    # compute distance from line
    p1 = [0,coeff_w[1]]
    p2 = [1,coeff_w[0]+coeff_w[1]]
    min_dist = 1000
    xs_min = 0
    ys_min = 0
    
    for j in range(len(idx_low)):
        P = [xs_low[j], ys_low[j]]
        p1minusp2 = [x1 - x2 for (x1, x2) in zip(p1, p2)]
        p1minusP = [x1 - x2 for (x1, x2) in zip(p1, P)]
        dist = norm(np.cross(p1minusp2, p1minusP))/norm(p1minusp2)
        if dist < min_dist:
            xs_min = xs_low[j]
            ys_min = ys_low[j]
        elif dist == min_dist:
            xs_min = np.concatenate((xs_min,xs_low[j]))
            ys_min = np.concatenate((ys_min,ys_low[j]))
        min_dist = np.min([dist,min_dist])
        
    # find the two furthest high
    idx_high = get_indexes(1,fs)  # look for lowest possible frequency
    if not idx_high: # if there are no voxels go to the following low freq
        idx_high = get_indexes(2,fs)
        if not idx_high:
            idx_high = get_indexes(3,fs)
            if not idx_high:
                idx_high = get_indexes(4,fs)
    xs_high = [xs[i] for i in idx_high]
    ys_high = [ys[i] for i in idx_high]
    # compute distance from line
    max_dist_above = 0
    max_dist_below = 0
    xs_max_above = 0
    ys_max_above = 0
    xs_max_below = 0
    ys_max_below = 0
    
    for j in range(len(idx_high)):
        P = [xs_high[j], ys_high[j]]
        p1minusp2 = [x1 - x2 for (x1, x2) in zip(p1, p2)]
        p1minusP = [x1 - x2 for (x1, x2) in zip(p1, P)]
        dist = norm(np.cross(p1minusp2, p1minusP))/norm(p1minusp2)
        if ys_high[j] > xs_high[j]*coeff_w[0]+coeff_w[1]:  # above the line
            if dist > max_dist_above:
                xs_max_above = xs_high[j]
                ys_max_above = ys_high[j]
            elif dist == max_dist_above:
                xs_max_above = np.concatenate((xs_max_above,xs_high[j]))
                ys_max_above = np.concatenate((ys_max_above,ys_high[j]))
            max_dist_above = np.max([dist,max_dist_above])
        else:
            if dist > max_dist_below:
                xs_max_below = xs_high[j]
                ys_max_below = ys_high[j]
            elif dist == max_dist_below:
                xs_max_below = np.concatenate((xs_max_below,xs_high[j]))
                ys_max_below = np.concatenate((ys_max_below,ys_high[j]))
            max_dist_below = np.max([dist,max_dist_below])
            
    if max_dist_below*max_dist_above == 0:
        idx_high = get_indexes(5,fs) 
        if not idx_high:
            idx_high = get_indexes(6,fs)
        xs_high = [xs[i] for i in idx_high]
        ys_high = [ys[i] for i in idx_high]
        if max_dist_above == 0:
            for j in range(len(idx_high)):
                P = [xs_high[j], ys_high[j]]
                p1minusp2 = [x1 - x2 for (x1, x2) in zip(p1, p2)]
                p1minusP = [x1 - x2 for (x1, x2) in zip(p1, P)]
                dist = norm(np.cross(p1minusp2, p1minusP))/norm(p1minusp2)
                if ys_high[j] > xs_high[j]*coeff_w[0]+coeff_w[1]:  # above the line
                    if dist > max_dist_above:
                        xs_max_above = xs_high[j]
                        ys_max_above = ys_high[j]
                    elif dist == max_dist_above:
                        xs_max_above = np.concatenate((xs_max_above,xs_high[j]))
                        ys_max_above = np.concatenate((ys_max_above,ys_high[j]))
                    max_dist_above = np.max([dist,max_dist_above])
        if max_dist_below == 0:
            for j in range(len(idx_high)):
                P = [xs_high[j], ys_high[j]]
                p1minusp2 = [x1 - x2 for (x1, x2) in zip(p1, p2)]
                p1minusP = [x1 - x2 for (x1, x2) in zip(p1, P)]
                dist = norm(np.cross(p1minusp2, p1minusP))/norm(p1minusp2)
                if ys_high[j] < xs_high[j]*coeff_w[0]+coeff_w[1]:  # above the line
                    if dist > max_dist_below:
                        xs_max_below = xs_high[j]
                        ys_max_below = ys_high[j]
                    elif dist == max_dist_below:
                        xs_max_below = np.concatenate((xs_max_below,xs_high[j]))
                        ys_max_below = np.concatenate((ys_max_below,ys_high[j]))
                    max_dist_below = np.max([dist,max_dist_below])
                    
                    
    a = np.array([xs_max_above, ys_max_above,0.])
    b = np.array([xs_min, ys_min, 0.])
    c = np.array([xs_max_below, ys_max_below, 0.])
    
    ba = a - b
    bc = c - b
    
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)            
    
    angle_pt[i] = np.degrees(angle)

    if plot_y_n:            
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(xs,ys, c = fs, cmap = 'jet', alpha = 0.4)    
        plt.plot(xs_min,ys_min,'k*',markersize = 20, label = 'closest low')
        plt.plot(xs_max_above,ys_max_above,'ko',markersize = 18,label = 'highest high above')
        plt.plot(xs_max_below,ys_max_below,'ko',markersize = 18,label = 'highest high below')
        plt.title('Find angle')
        plt.legend(loc = 'upper right')
        plt.show()

plt.figure()
plt.hist(angle_pt)
plt.title('PATIENTS')
plt.xlabel('Angle')
plt.ylabel('Occurrency')