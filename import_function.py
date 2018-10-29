# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 13:45:09 2018

@author: Giorgia
"""
import numpy as np
from numpy.linalg import det, norm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import DBSCAN

def import_function(file_name):
    mydata = np.loadtxt(file_name,skiprows = 10) 
    return mydata

def plot_tono_map(mydata, title):
    voxel_num = np.shape(mydata)[0]  # number of voxels
    xs = mydata[:,1]
    ys = mydata[:,2]
    zs = mydata[:,3]
    fs = 14-mydata[:,7] 
 
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs,ys,zs, c = fs, cmap = 'jet')
    plt.title(title)
    plt.show()
    
def plot_2d(mydata, title):
    voxel_num = np.shape(mydata)[0]  # number of voxels
    xs = mydata[:,1]
    ys = mydata[:,2]
    fs = 14-mydata[:,7] 
  
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xs,ys, c = fs, cmap = 'jet')
    plt.title(title)
    plt.show()
    output_dir = "../figures/all_maps"
    fig.savefig('{}/{}.png'.format(output_dir,title))
    
def organize_data(data):
    until = list(data[3,:]).index(-2)
    xs = data[0,0:until]
    ys = data[1,0:until]
    zs = data[2,0:until]
    fs = data[3,0:until] 
    an = data[4,0:until]
    return xs,ys,zs,fs,an
    
def bysect_line(data, title, plot_y_n = False): # data is the slice of 3D matrix for one scan with fs already 14-fs
    xs,ys,zs,fs,an = organize_data(data) 
    
    get_indexes = lambda x, x_s: [i for (y, i) in zip(x_s, range(len(x_s))) if x == y]

    idx_bordeaux = get_indexes(13,fs)
    idx_red = get_indexes(12,fs)
    
    xs_red = [xs[i] for i in idx_red]
    xs_bordeaux = [xs[i] for i in idx_bordeaux]
    xs_high = np.concatenate((xs_red,xs_bordeaux))
    ys_red = [ys[i] for i in idx_red]
    ys_bordeaux = [ys[i] for i in idx_bordeaux]
    ys_high = np.concatenate((ys_red,ys_bordeaux))
    
    min_xs = 40
    
    if len(xs_high) < min_xs:
        #print('consider orange too')
        idx_orange = get_indexes(11,fs)
        xs_orange = [xs[i] for i in idx_orange]
        ys_orange = [ys[i] for i in idx_orange]
        xs_high = np.concatenate((xs_high,xs_orange))
        ys_high = np.concatenate((ys_high,ys_orange))
    
    
    #plt.plot(xs_high,ys_high,'o')
    coeff = np.polyfit(xs_high,ys_high,1)
    
    x_fit = np.arange(np.nanmin(xs),np.nanmax(xs),0.01)  # use nanmin/nanmax since there is a nan value in pt[16]
    y_fit = x_fit*coeff[0]+coeff[1]
    uno = [1]*len(xs_red)
    due = [2]*len(xs_bordeaux)
    
    w = np.concatenate((uno,due))
    if len(xs_red)+len(xs_bordeaux) < min_xs:
        w = np.concatenate((w,[0.5]*len(xs_orange)))
    coeff_w = np.polyfit(xs_high,ys_high,deg = 1, w = w)
    y_fit_w = x_fit*coeff_w[0]+coeff_w[1]
    
    if plot_y_n:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(xs,ys, c = fs, cmap = 'jet')    
        plt.plot(x_fit,y_fit,'k',label = 'linear fit')
        plt.plot(x_fit,y_fit_w,'b',label = 'weighted fit')
        plt.title(title)
        plt.legend()
        plt.show()
        
    return coeff_w
    
def mean_dist_b_line(data, title, coeff_w, plot_y_n = False):
    # set the data
    xs,ys,zs,fs,an = organize_data(data)
    # useful function
    get_indexes = lambda x, x_s: [i for (y, i) in zip(x_s, range(len(x_s))) if x == y]
    # two points on the line
    p1 = [0,coeff_w[1]]
    p2 = [1,coeff_w[0]+coeff_w[1]]
    mean_dist = np.zeros(14)
    above_line = np.zeros(14)
    below_line = np.zeros(14)
    above_minus_below = np.zeros(14)
    max_dist = 0
    
    for i in range(14): # loop on all the frequencies
        idx = get_indexes(i,fs)
        xs_idx = [xs[i] for i in idx]
        ys_idx = [ys[i] for i in idx]
        dist = 0
        if not idx: # case if there are no pixels associated with this particular f
            mean_dist[i] = 0
        else: # case if some voxels are associated to this f
            # find mean distance
            for j in range(len(idx)):
                P = [xs_idx[j], ys_idx[j]]
                p1minusp2 = [x1 - x2 for (x1, x2) in zip(p1, p2)]
                p1minusP = [x1 - x2 for (x1, x2) in zip(p1, P)]
                dist += norm(np.cross(p1minusp2, p1minusP))/norm(p1minusp2)
                max_dist = np.max([dist,max_dist])
                
            mean_dist[i] = dist/len(idx)
            
            # find number of points above or below the line
            for j in range(len(idx)):
                #P = [xs_idx[j], ys_idx[j]]
                #p1minusp2 = [x1 - x2 for (x1, x2) in zip(p1, p2)]
                #p1minusP = [x1 - x2 for (x1, x2) in zip(p1, P)]
                #dist += norm(np.cross(p1minusp2, p1minusP))/norm(p1minusp2)
                #if dist <=max_dist:
                if ys_idx[j] > xs_idx[j]*coeff_w[0]+coeff_w[1]:
                    above_line[i]+=1
                else:
                    below_line[i]+=1
                above_minus_below[i] = (above_line[i]-below_line[i])/(above_line[i]+below_line[i])
     
    if plot_y_n:
        plt.figure()
        plt.plot(mean_dist,'o')
        plt.xlabel('Frequency')
        plt.ylabel('Mean distance')
        plt.title('Average distance from line for all frequencies')
        
        plt.figure()
        plt.plot(above_line,'ro', label = 'voxels above line')
        plt.plot(below_line,'bo', label = 'voxels below line')
        plt.scatter(np.arange(14),[-5]*14,marker = '*',c = list((np.arange(14))), cmap = 'jet')
        plt.xlabel('Frequency')
        plt.ylabel('Number of voxels')
        plt.legend()
        plt.show()
    
    return mean_dist, above_minus_below

def three_f_ranges(data,title, coeff_w, plot_y_n = False, eps = 1.5, min_samples = 3):
    # set the data
    xs,ys,zs,fs,an = organize_data(data)
    
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
        plt.title(title)
        plt.show()
        
    # separate regions R and A1
    xs_all = [xs_flow,xs_fmedium,xs_fhigh]
    ys_all = [ys_flow,ys_fmedium,ys_fhigh]
    
    xs_flow_R = []
    xs_flow_A = []
    xs_fmedium_R = []
    xs_fmedium_A = []
    xs_fhigh_R = []
    xs_fhigh_A = []
    ys_flow_R = []
    ys_flow_A = []
    ys_fmedium_R = []
    ys_fmedium_A = []
    ys_fhigh_R = []
    ys_fhigh_A = []
    
    xs_R = [xs_flow_R, xs_fmedium_R, xs_fhigh_R]
    ys_R = [ys_flow_R, ys_fmedium_R, ys_fhigh_R]
    xs_A = [xs_flow_A, xs_fmedium_A, xs_fhigh_A]
    ys_A = [ys_flow_A, ys_fmedium_A, ys_fhigh_A]
    
    for i in range(len(xs_all)): # i stands for low, medium, high
        xs = xs_all[i]
        ys = ys_all[i]
        for j in range(len(xs)): # j stands for the index of the list of coordinate
            if ys[j] > xs[j]*coeff_w[0]+coeff_w[1]: # R region
                x_list = np.array([xs[j]])
                y_list = np.array([ys[j]])
                xs_R[i] = np.concatenate ((xs_R[i],x_list)) 
                ys_R[i] = np.concatenate ((ys_R[i],y_list)) 
            else:
                x_list = np.array([xs[j]])
                y_list = np.array([ys[j]])
                xs_A[i] = np.concatenate ((xs_A[i],x_list)) 
                ys_A[i] = np.concatenate ((ys_A[i],y_list))
        
    # find number of cluster and respective size
    coord_low_R = np.zeros([len(xs_R[0]),2])
    coord_low_A = np.zeros([len(xs_A[0]),2])
    coord_low_R[:,0] = xs_R[0]
    coord_low_R[:,1] = ys_R[0]
    coord_low_A[:,0] = xs_A[0]
    coord_low_A[:,1] = ys_A[0]
    
    coord_medium_R = np.zeros([len(xs_R[1]),2])
    coord_medium_A = np.zeros([len(xs_A[1]),2])
    coord_medium_R[:,0] = xs_R[1]
    coord_medium_R[:,1] = ys_R[1]
    coord_medium_A[:,0] = xs_A[1]
    coord_medium_A[:,1] = ys_A[1]
    
    coord_high_R = np.zeros([len(xs_R[2]),2])
    coord_high_A = np.zeros([len(xs_A[2]),2])
    coord_high_R[:,0] = xs_R[2]
    coord_high_R[:,1] = ys_R[2]
    coord_high_A[:,0] = xs_A[2]
    coord_high_A[:,1] = ys_A[2]
    
    coord_all = [coord_low_R, coord_low_A,coord_medium_R,coord_medium_A,coord_high_R,coord_high_A]
    
    cluster_number = np.zeros(len(coord_all))
    cluster_size_mean = np.zeros(len(coord_all))
    
    for j,X in enumerate(coord_all):
        if np.shape(X)[0]==0:
            cluster_size_mean[j] = 0
            cluster_number[j] = 0
        else:
            clustering = DBSCAN(eps=eps, min_samples=3).fit(X)
            labels = clustering.labels_ 
            n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
            unique_labels = set(labels)
            cluster_size = 0
            for lab in unique_labels:
                if lab != -1:
                    idx_lab = get_indexes(lab,labels)
                    cluster_size += len(idx_lab)
            if n_clusters_ != 0:
                cluster_size_mean[j] = cluster_size/n_clusters_
            cluster_number[j] = n_clusters_
            
            # Plot results (Black removed and is used for noise instead)
            core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
            core_samples_mask[clustering.core_sample_indices_] = True
            
            colors = [plt.cm.Spectral(each)
                      for each in np.linspace(0, 1, len(unique_labels))]
                
            if plot_y_n:
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
            
            #plt.title('Estimated number of clusters: %d' % n_clusters_)
            plt.show()
            
    cluster_number = [cluster_number[0]+cluster_number[1],cluster_number[2]+cluster_number[3],cluster_number[4]+cluster_number[5]]
    cluster_size_mean = [cluster_size_mean[0]+cluster_size_mean[1],cluster_size_mean[2]+cluster_size_mean[3],cluster_size_mean[4]+cluster_size_mean[5]]
    cluster_size_mean = [i/2 for i in cluster_size_mean]
            
    return cluster_number, cluster_size_mean
            

def matrixing(data, title, pixels, plot_y_n):
    xs,ys,zs,fs,an = organize_data(data) 

    min_xs = np.nanmin(xs)
    max_xs = np.nanmax(xs)
    min_ys = np.nanmin(ys)
    max_ys = np.nanmax(ys)
    
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
                table[i,j] = np.nan # set to NaN so that it's ignored (i.e. white) in the image plot
                
    if plot_y_n:
        plt.figure()
        plt.imshow(table,cmap = 'jet')
        plt.title(title)
        plt.show()

    return table        
            
            
def find_angles(data,title,coeff_w,plot_y_n,plot_points):
    xs,ys,zs,fs,an = organize_data(data) 
       
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
            
    if max_dist_below*max_dist_above == 0: # if in the considered frequency range there is no point either above or below or both the line, go to the net frequency range
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
                        
    # compute the angle between the three points                
    a = np.array([xs_max_above, ys_max_above,0.]) # zero is added for 3D coordinate
    b = np.array([xs_min, ys_min, 0.])
    c = np.array([xs_max_below, ys_max_below, 0.])
    
    ba = a - b
    bc = c - b
    
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)            
    
    angle_out = np.degrees(angle)
    
    if plot_points:            
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(xs,ys, c = fs, cmap = 'jet', alpha = 0.4)    
        plt.plot(xs_min,ys_min,'k*',markersize = 20, label = 'closest low')
        plt.plot(xs_max_above,ys_max_above,'ko',markersize = 18,label = 'highest high above')
        plt.plot(xs_max_below,ys_max_below,'ko',markersize = 18,label = 'highest high below')
        plt.title('Find angle')
        plt.legend(loc = 'upper right')
        plt.show()
    
    return angle_out, xs_min, ys_min, xs_max_above, ys_max_above, xs_max_below, ys_max_below