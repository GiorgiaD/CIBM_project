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
import matplotlib
from scipy.spatial import ConvexHull
import matplotlib.path as mplPath
import pylab
import math
import matplotlib.patches as patches

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
    
def bysect_line(data, title, coeff_w_anat, target = 0, plot_y_n = False, target_yn = False): # data is the slice of 3D matrix for one scan with fs already 14-fs
    xs,ys,zs,fs,an = organize_data(data) 
    plot_hull = False
    xs,ys,zs,fs,an = data_in_hull(xs,ys,zs,fs,an,margin = 0.32,plot_hull = plot_hull)
    
    get_indexes = lambda x, x_s: [i for (y, i) in zip(x_s, range(len(x_s))) if x == y]

    # select the voxels at low (wrong to call them 'high') frequency
    idx_bordeaux = get_indexes(13,fs)
    idx_red = get_indexes(12,fs)
    
    xs_red = [xs[i] for i in idx_red]
    xs_bordeaux = [xs[i] for i in idx_bordeaux]
    xs_high = np.concatenate((xs_red,xs_bordeaux))
    
    ys_red = [ys[i] for i in idx_red]
    ys_bordeaux = [ys[i] for i in idx_bordeaux]
    ys_high = np.concatenate((ys_red,ys_bordeaux))
    
    fs_red = [fs[i] for i in idx_red]
    fs_bordeaux = [fs[i] for i in idx_bordeaux]
    fs_high = np.concatenate((fs_red,fs_bordeaux))
    
    min_xs = 300
    
    #print(len(xs_high))
    
    #print('xs_high is',len(xs_high))
    
    if len(xs_high) < min_xs:
        #print('consider orange too: xs_high = {}'.format(len(xs_high)))
        idx_orange = get_indexes(11,fs)
        xs_orange = [xs[i] for i in idx_orange]
        ys_orange = [ys[i] for i in idx_orange]
        fs_orange = [fs[i]*0.9 for i in idx_orange]
        xs_high = np.concatenate((xs_high,xs_orange))
        ys_high = np.concatenate((ys_high,ys_orange))
        fs_high = np.concatenate((fs_high,fs_orange))
        #print('xs_high after orange is',len(xs_high))
        
    if len(xs_high) < min_xs-60:
        #print('consider yellow too: xs_high = {}'.format(len(xs_high)))
        idx_orange = get_indexes(10,fs)
        xs_orange = [xs[i] for i in idx_orange]
        ys_orange = [ys[i] for i in idx_orange]
        fs_orange = [fs[i]*0.8 for i in idx_orange]
        xs_high = np.concatenate((xs_high,xs_orange))
        ys_high = np.concatenate((ys_high,ys_orange))
        fs_high = np.concatenate((fs_high,fs_orange))
        #print('xs_high after orange 2 is',len(xs_high))    
        
    
    # among the selected voxels, now keep only the ones belonging to the biggest low frequency cluster
    biggest_size = 0
    size_difference = 0
    biggest_idx = []
    
    # among the selected voxels, check the cluster which is closest to the anatomic line
    smallest_distance = 1000000
    distance_difference = 0
    distance_of_biggest = 0
    distance_idx = []   
    p1 = [0,coeff_w_anat[1]]
    p2 = [1,coeff_w_anat[0]+coeff_w_anat[1]]
    
    X = np.zeros([len(xs_high),2])
    X[:,0] = xs_high
    X[:,1] = ys_high
    
    if len(xs_high)>300:
        eps = 1.1
    elif len(xs_high)>175:
        eps = 1.4
    else:
        eps = 2.0
    
    if np.shape(X)[0]==0:
        print('WARNING : fitting cannot be performed --> data is empty')
    else:
        clustering = DBSCAN(eps=eps, min_samples=3).fit(X)
        labels = clustering.labels_ 
        #print(labels)
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        unique_labels = set(labels)
        cluster_size = 0
        for lab in unique_labels: # for each cluster
            if lab != -1:
                idx_lab = get_indexes(lab,labels)
                cluster_size = len(idx_lab)
                
                if cluster_size > biggest_size:  # update the biggest cluster when a bigger one is found
                    biggest_update = 1
                    size_difference = np.abs(biggest_size-cluster_size)
                    biggest_size = cluster_size
                    biggest_idx = idx_lab  
                else:
                    biggest_update = 0
                    
                # here compute the mean distance of points in one cluster from the line
                #dist = 0
                #for point in range(len(idx_lab)): # for each point in the cluster
                #    P = [xs_high[point], ys_high[point]]
                #    p1minusp2 = [x1 - x2 for (x1, x2) in zip(p1, p2)]
                #    p1minusP = [x1 - x2 for (x1, x2) in zip(p1, P)]
                #    dist += norm(np.cross(p1minusp2, p1minusP))/norm(p1minusp2)
                #mean_dist = dist/len(idx_lab)
                
                # compute distance from center of cluster to line
                xs_now = [xs_high[x] for x in idx_lab]
                ys_now = [ys_high[x] for x in idx_lab]
                center_cluster_x = np.mean(xs_now)
                center_cluster_y = np.mean(ys_now)
                P = [center_cluster_x,center_cluster_y]
                p2minusp1 = [x1 - x2 for (x1, x2) in zip(p2,p1)]
                p2minusP = [x1 - x2 for (x1, x2) in zip(p2, P)]
                
                mean_dist = norm(np.cross(p2minusp1,p2minusP))/norm(p2minusp1)
                
                if mean_dist < smallest_distance and cluster_size>20:  # update the biggest cluster when a bigger one is found
                    smallest_distance = mean_dist
                    distance_idx = idx_lab 
                if biggest_update == 1:
                    distance_of_biggest = mean_dist
                distance_difference = np.abs (distance_of_biggest - smallest_distance)
                  
                #print('distance of this cluster',mean_dist)
                #print('size of this cluster',cluster_size)
                #plt.figure()
                #plt.scatter(xs_now,ys_now, c = 'b', alpha = 0.3)
                #plt.plot(P[0],P[1],'ro')
                #x_fit = np.arange(np.nanmin(xs),np.nanmax(xs),0.01) 
                #y_fit_w_anat = x_fit*coeff_w_anat[0]+coeff_w_anat[1]
                #plt.plot(x_fit,y_fit_w_anat,'r',label = 'anatomic fit')
                    
        #print('difference in size of 2biggests: ', size_difference)
        #print('difference in distance of closest and biggest', distance_difference)
        #print('smallest distance', smallest_distance)
                    
        # Plot results (Black removed and is used for noise instead)
        core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
        core_samples_mask[clustering.core_sample_indices_] = True
        
        colors = [plt.cm.Spectral(each)
                  for each in np.linspace(0, 1, len(unique_labels))]
            
        #plt.figure()
        for k, col in zip(unique_labels, colors):
            if k == -1:
                # Black used for noise.
                col = [0, 0, 0, 1]
        
            class_member_mask = (labels == k)
        
            xy = X[class_member_mask & core_samples_mask]
            
            #plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),markeredgecolor='k', markersize=14)
        
            xy = X[class_member_mask & ~core_samples_mask]
            #---plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),markeredgecolor='k', markersize=6)
    
        #plt.title('Estimated number of clusters: %d' % n_clusters_)
        #plt.show()
                    
    #print('biggest size is ',biggest_size)
    
    if smallest_distance < 4.0 and distance_difference > 6:
        chosen_idx = distance_idx
        #print('Fitting on closest cluster to anatomy, size: ',len(distance_idx))
    else:
        chosen_idx = biggest_idx
     
    if biggest_size > 18:  # for big cluster you can consider only it, otherwise consider everything else too                
        w_main = [fs_high[x] for x in chosen_idx]
        xs_main = [xs_high[x] for x in chosen_idx]
        ys_main = [ys_high[x] for x in chosen_idx]
    else:
        w_main = fs_high
        xs_main = xs_high
        ys_main = ys_high
        #print(title+' all clusters considered')
    
    coeff_w = np.polyfit(xs_main,ys_main,deg = 1, w = w_main)
    
    #print(w_main)
    
    #plt.plot(xs_main,ys_main,'o')
    
    
    ## the following small commented section is the old one 
    #coeff = np.polyfit(xs_high,ys_high,1)
    xs,ys,zs,fs,an = organize_data(data) 
    x_fit = np.arange(np.nanmin(xs),np.nanmax(xs),0.01)  # use nanmin/nanmax since there is a nan value in pt[16]
    #y_fit = x_fit*coeff[0]+coeff[1]
    #uno = [1]*len(xs_red)
    #due = [2]*len(xs_bordeaux)
    #w = np.concatenate((uno,due))
    #if len(xs_red)+len(xs_bordeaux) < min_xs:
    #    w = np.concatenate((w,[0.5]*len(xs_orange)))
    #coeff_w = np.polyfit(xs_high,ys_high,deg = 1, w = w)
    y_fit_w = x_fit*coeff_w[0]+coeff_w[1]
    
    y_fit_w_anat = x_fit*coeff_w_anat[0]+coeff_w_anat[1]
    
    if plot_y_n:
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(xs,ys, c = fs, cmap = 'jet') 
        ax.scatter(xs_main,ys_main, c = 'k', alpha = 0.7)
        #plt.plot(x_fit,y_fit,'k',label = 'linear fit')
        plt.plot(x_fit,y_fit_w,'b',label = 'weighted fit on main cluster',linewidth = 5)
        plt.plot(x_fit,y_fit_w_anat,'r',label = 'anatomic fit',linewidth = 5)
        if target_yn:
            title += ' class '
            title += str(target)
        plt.title(title)
        plt.legend()
        cax, _ = matplotlib.colorbar.make_axes(ax)
        cbar = matplotlib.colorbar.ColorbarBase(cax, cmap='jet')
        cbar.ax.set_yticklabels(['high frequency', '','','','', 'low frequency'])  # vertically oriented colorbar
        plt.show()
        output_dir = "../../figures/big_dataset/bysecting/tono/"
        title = title+'_axis_tono'
        fig.savefig('{}/{}.png'.format(output_dir,title))
            
    #print(title+'biggest cluster has size {}'.format(biggest_size))
        
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
            
    cluster_number_ = [cluster_number[0]+cluster_number[1],cluster_number[2]+cluster_number[3],cluster_number[4]+cluster_number[5]]
    cluster_size_mean_ = [cluster_size_mean[0]+cluster_size_mean[1],cluster_size_mean[2]+cluster_size_mean[3],cluster_size_mean[4]+cluster_size_mean[5]]
    cluster_size_mean_ = [i/2 for i in cluster_size_mean]
    
    cluster_num_low = cluster_number[0]+cluster_number[1]
    cluster_num_med = cluster_number[2]+cluster_number[3]
    cluster_num_high = cluster_number[4]+cluster_number[5]
    cluster_size_low = cluster_size_mean[0]+cluster_size_mean[1]
    cluster_size_low = 0.5*cluster_size_low
    cluster_size_med = cluster_size_mean[2]+cluster_size_mean[3]
    cluster_size_med = 0.5*cluster_size_med
    cluster_size_high = cluster_size_mean[4]+cluster_size_mean[5]
    cluster_size_high = 0.5*cluster_size_high
                            
    
    return cluster_number, cluster_size_mean, cluster_num_low, cluster_num_med, cluster_num_high, cluster_size_low, cluster_size_med, cluster_size_high            

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
    
    # compute the distance between the two maxima
    distance_out = np.linalg.norm(a-c)
    
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
    
    return angle_out, xs_min, ys_min, xs_max_above, ys_max_above, xs_max_below, ys_max_below, distance_out




    # CLASSIFY ANATOMY AND DRAW THE ANATOMIC BYSECTING LINE

def anatomy(data,title,plot_y_n_three_anat_regions,plot_y_n_anat_clusters, plot_y_n_fit_anat):   

# 1) divide three levels range: very negative, close to zero, very positive
    xs,ys,zs,fs,an = organize_data(data) 
    threshold_neg = - 0.085
    threshold_pos = 0.075
    idx_zeros = np.where(np.logical_and(an>=threshold_neg, an<=threshold_pos))
    idx_neg = np.where(an<threshold_neg)
    idx_pos = np.where(an>threshold_pos)

    xs_zeros = [xs[i] for i in idx_zeros]
    ys_zeros = [ys[i] for i in idx_zeros]
    an_zeros = [an[i] for i in idx_zeros]
    xs_pos = [xs[i] for i in idx_pos]
    ys_pos = [ys[i] for i in idx_pos]
    an_pos = [an[i] for i in idx_pos]
    xs_neg = [xs[i] for i in idx_neg]
    ys_neg = [ys[i] for i in idx_neg]
    an_neg = [an[i] for i in idx_neg]



    if plot_y_n_three_anat_regions:
        plt.figure()
        plt.plot(xs_zeros,ys_zeros,'o',color = 'gray',label = 'zeros')
        plt.plot(xs_neg,ys_neg,'o',color = 'black', label = 'concave')
        plt.plot(xs_pos,ys_pos,'o', color = 'lightgray', label = 'convex')
        plt.xlabel('x coordinate')
        plt.ylabel('y coordinate')
        #plt.legend()
        plt.title(title)
        plt.show()

    # find number of cluster and respective size
    get_indexes = lambda x, x_s: [i for (y, i) in zip(x_s, range(len(x_s))) if x == y]
    
    coord_zeros = np.zeros([len(xs_zeros[0]),2])
    coord_zeros[:,0] = xs_zeros[0]
    coord_zeros[:,1] = ys_zeros[0]
    
    coord_pos = np.zeros([len(xs_pos[0]),2])
    coord_pos[:,0] = xs_pos[0]
    coord_pos[:,1] = ys_pos[0]
    
    coord_neg = np.zeros([len(xs_neg[0]),2])
    coord_neg[:,0] = xs_neg[0]
    coord_neg[:,1] = ys_neg[0]

    coord_all = [coord_zeros, coord_pos, coord_neg]
    
    cluster_number = np.zeros(len(coord_all))
    cluster_size_mean = np.zeros(len(coord_all))
    cluster_nb_zeros = 0
    cluster_nb_zeros_big = 0
    cluster_nb_zeros_small = 0
    cluster_nb_pos = 0
    cluster_nb_pos_big = 0
    cluster_nb_pos_small = 0
    cluster_nb_neg = 0
    cluster_nb_neg_big = 0
    cluster_nb_neg_small = 0
    
    fraction_big_small = 0.09
    eps = 1.5
    
    biggest_zeros_size = 0
    biggest_pos_size = 0
    biggest_neg_size = 0
    biggest_zeros_idx = []
    biggest_pos_idx = []
    biggest_neg_idx = []
    
    anat_classify = 0
    fit_anat = [0,0]
    
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
                    #print('size of cluster level {} is {}'.format(j,len(idx_lab)))
                    #print('its ratio to total number {} is {}'.format(len(xs),len(idx_lab)/len(xs)))
                    cluster_size += len(idx_lab)
                    fraction = len(idx_lab)/len(xs)  
                    # classify the clusters according to their height and their size
                    if j == 0 and fraction >= fraction_big_small:
                        cluster_nb_zeros_big += 1
                    elif j == 0 and fraction < fraction_big_small:
                        cluster_nb_zeros_small += 1
                    elif j == 1 and fraction >= fraction_big_small:
                        cluster_nb_pos_big += 1
                    elif j == 1 and fraction < fraction_big_small:
                        cluster_nb_pos_small += 1
                    elif j == 2 and fraction >= fraction_big_small:
                        cluster_nb_neg_big += 1
                    elif j == 2 and fraction < fraction_big_small:
                        cluster_nb_neg_small += 1
                        
                    # record the biggest cluster per level
                    if j == 0 and len(idx_lab) >= biggest_zeros_size:
                        biggest_zeros_size = len(idx_lab)
                        biggest_zeros_idx = idx_lab 
                    elif j == 1 and len(idx_lab) >= biggest_pos_size:
                        biggest_pos_size = len(idx_lab)
                        biggest_pos_idx = idx_lab
                    elif j == 2 and len(idx_lab) >= biggest_neg_size:
                        biggest_neg_size = len(idx_lab)
                        biggest_neg_idx = idx_lab
                    
                    
            if n_clusters_ != 0:
                cluster_size_mean[j] = cluster_size/n_clusters_
            cluster_number[j] = n_clusters_
            # count total number of clusters per height level
            if j == 0:
                cluster_nb_zeros = n_clusters_
            elif j == 1:
                cluster_nb_pos = n_clusters_
            elif j == 2:
                cluster_nb_neg = n_clusters_
            
            # Plot results (Black removed and is used for noise instead)
            core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
            core_samples_mask[clustering.core_sample_indices_] = True
            
            colors = [plt.cm.Spectral(each)
                      for each in np.linspace(0, 1, len(unique_labels))]
                
            if plot_y_n_anat_clusters:
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
            
    #print('For control {} there are {} pos, {} neg, {} zeros'.format(i,cluster_number[0],cluster_number[1],cluster_number[2]))

    # here classify the anatomy of the scan into 1. single gyrus   2. partial duplication   3.full duplication
    # check single gyrus
    if cluster_nb_neg_big == 1 and cluster_nb_neg<=2:
        if cluster_nb_pos == 2:
            if cluster_nb_pos_big >= 1:
                if cluster_nb_zeros >= 2:
                    if cluster_nb_zeros > 2 or cluster_nb_zeros_big == 2:
                        anat_classify = 1
    # check partial duplication                    
    if anat_classify == 0:    
        if cluster_nb_zeros_big <= 2:
            if cluster_nb_pos >= 2:
                anat_classify = 2
    # check full duplication
    if anat_classify != 1:     
        if cluster_nb_pos_big >= 1:
            if cluster_nb_zeros_big >= 2 or cluster_nb_zeros >= 3:
                if cluster_nb_neg >= 2:
                    anat_classify = 3
    print('size',cluster_nb_zeros_big,cluster_nb_zeros_small,cluster_nb_pos_big,cluster_nb_pos_small,cluster_nb_neg_big,cluster_nb_neg_small)
    print('tot',cluster_nb_zeros,cluster_nb_pos,cluster_nb_neg)
    #print('classified {}'.format(ctl_anat_classify[i]))
    
    # BYSECTING LINE THROUGH ANATOMY
    # divide two cases 
    # case A) syngle gyrus --> consider only the negative values for the fit
    if anat_classify == 1:
        
        w_main_neg = [an_neg[0][x] for x in biggest_neg_idx]
        xs_main_neg = [xs_neg[0][x] for x in biggest_neg_idx]
        ys_main_neg = [ys_neg[0][x] for x in biggest_neg_idx]
        
        an_neg_rev = [-x for x in w_main_neg]
        coeff_w = np.polyfit(xs_main_neg,ys_main_neg,deg = 1, w = w_main_neg)
    
        x_fit = np.arange(np.nanmin(xs_neg[0]),np.nanmax(xs_neg[0]),0.01)  # use nanmin/nanmax since there is a nan value in pt[16]
        y_fit = x_fit*coeff_w[0]+coeff_w[1]
        
        if plot_y_n_fit_anat:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.scatter(xs,ys, c = an, cmap = 'gray')    
            plt.plot(x_fit,y_fit,'k',label = 'linear fit')
            plt.title(title)
            plt.legend()
            plt.show()
    
        fit_anat = coeff_w
    # case B) partial duplication
    if anat_classify == 2:
        
        #weights = np.concatenate((an_pos[0],an_neg[0]))
        #xs_conc = np.concatenate((xs_pos[0],xs_neg[0]))
        #ys_conc = np.concatenate((ys_pos[0],ys_neg[0]))
        
        w_main_zeros = [an_zeros[0][x] for x in biggest_zeros_idx]
        xs_main_zeros = [xs_zeros[0][x] for x in biggest_zeros_idx]
        ys_main_zeros = [ys_zeros[0][x] for x in biggest_zeros_idx]
        #coeff_w = np.polyfit(xs_conc,ys_conc,deg = 1, w = weights)
        
        #coeff_w = np.polyfit(xs_zeros[0],ys_zeros[0],deg = 1, w = an_zeros[0])
        coeff_w = np.polyfit(xs_main_zeros,ys_main_zeros,deg = 1, w = w_main_zeros)
    
        x_fit = np.arange(np.nanmin(xs_zeros[0]),np.nanmax(xs_zeros[0]),0.01)  # use nanmin/nanmax since there is a nan value in pt[16]
        y_fit = x_fit*coeff_w[0]+coeff_w[1]
        
        if plot_y_n_fit_anat:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.scatter(xs,ys, c = an, cmap = 'gray')    
            plt.plot(x_fit,y_fit,'k',label = 'linear fit')
            plt.title(title)
            plt.legend()
            plt.show()
    
        fit_anat = coeff_w
        
    # case C) full duplication
    if anat_classify == 3:    
        w_main_pos = [an_pos[0][x] for x in biggest_pos_idx]
        xs_main_pos = [xs_pos[0][x] for x in biggest_pos_idx]
        ys_main_pos = [ys_pos[0][x] for x in biggest_pos_idx]
        coeff_w = np.polyfit(xs_main_pos,ys_main_pos,deg = 1, w = w_main_pos)
    
        x_fit = np.arange(np.nanmin(xs_neg[0]),np.nanmax(xs_neg[0]),0.01)  # use nanmin/nanmax since there is a nan value in pt[16]
        y_fit = x_fit*coeff_w[0]+coeff_w[1]
        
        if plot_y_n_fit_anat:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.scatter(xs,ys, c = an, cmap = 'gray')    
            plt.plot(x_fit,y_fit,'k',label = 'linear fit')
            plt.title(title)
            plt.legend()
            plt.show()
    
        fit_anat = coeff_w
    
    return anat_classify, fit_anat

# DRAW THE ANATOMIC BYSECTING LINE ON THE BASIS OF THE DUPLICATION TYPE

def anatomy_new(data,title,dupl_type,plot_y_n_three_anat_regions,plot_y_n_anat_clusters, plot_y_n_fit_anat):   

# 1) divide three levels range: very negative, close to zero, very positive
    xs,ys,zs,fs,an = organize_data(data) 
    plot_hull = False
    xs,ys,zs,fs,an = data_in_hull(xs,ys,zs,fs,an,margin = 0.25, plot_hull = plot_hull)
    
    #print('hei hei hei')
    threshold_neg = - 0.085   # originally it was -0.085
    threshold_pos = 0.21  # originally it was 0.075 for the smaller maps
    idx_zeros = np.where(np.logical_and(an>=threshold_neg, an<=threshold_pos))
    idx_neg = np.where(an<threshold_neg)
    idx_pos = np.where(an>threshold_pos)
    
    
    '''
    print(title+'  '+dupl_type)
    print('number of white ::', np.shape(idx_pos)[1])
    print('number of black ::', np.shape(idx_neg)[1])
    '''
    
    if np.shape(idx_pos)[1]<50:
        threshold_pos = 0.17
        idx_pos = np.where(an>threshold_pos)
        print('number of white increased to ::', np.shape(idx_pos)[1])
    '''
    if np.shape(idx_neg)[1]>1100:
        threshold_neg = -0.1
        idx_neg = np.where(an<threshold_neg)
        print('number of black decreased to ::', np.shape(idx_neg)[1])
    '''
    xs_zeros = [xs[i] for i in idx_zeros]
    ys_zeros = [ys[i] for i in idx_zeros]
    an_zeros = [an[i] for i in idx_zeros]
    xs_pos = [xs[i] for i in idx_pos]
    ys_pos = [ys[i] for i in idx_pos]
    an_pos = [an[i] for i in idx_pos]
    xs_neg = [xs[i] for i in idx_neg]
    ys_neg = [ys[i] for i in idx_neg]
    an_neg = [an[i] for i in idx_neg]

    if plot_y_n_three_anat_regions:
        plt.figure()
        plt.plot(xs_zeros,ys_zeros,'o',color = 'gray',label = 'zeros')
        plt.plot(xs_neg,ys_neg,'o',color = 'black', label = 'concave')
        plt.plot(xs_pos,ys_pos,'o', color = 'lightgray', label = 'convex')
        plt.xlabel('x coordinate')
        plt.ylabel('y coordinate')
        #plt.legend()
        plt.title(title)
        plt.show()

    # find number of cluster and respective size
    get_indexes = lambda x, x_s: [i for (y, i) in zip(x_s, range(len(x_s))) if x == y]
    
    coord_zeros = np.zeros([len(xs_zeros[0]),2])
    coord_zeros[:,0] = xs_zeros[0]
    coord_zeros[:,1] = ys_zeros[0]
    
    coord_pos = np.zeros([len(xs_pos[0]),2])
    coord_pos[:,0] = xs_pos[0]
    coord_pos[:,1] = ys_pos[0]
    
    coord_neg = np.zeros([len(xs_neg[0]),2])
    coord_neg[:,0] = xs_neg[0]
    coord_neg[:,1] = ys_neg[0]

    coord_all = [coord_zeros, coord_pos, coord_neg]
    
    cluster_number = np.zeros(len(coord_all))
    cluster_size_mean = np.zeros(len(coord_all))
    cluster_nb_zeros = 0
    cluster_nb_zeros_big = 0
    cluster_nb_zeros_small = 0
    cluster_nb_pos = 0
    cluster_nb_pos_big = 0
    cluster_nb_pos_small = 0
    cluster_nb_neg = 0
    cluster_nb_neg_big = 0
    cluster_nb_neg_small = 0
    
    fraction_big_small = 0.09
    eps = 1.5
    
    biggest_zeros_size = 0
    biggest_pos_size = 0
    biggest_neg_size = 0
    biggest_zeros_idx = []
    biggest_pos_idx = []
    biggest_neg_idx = []
    
    anat_classify = 0
    fit_anat = [0,0]
    
    xs_center = (np.max(xs)+np.min(xs))*0.5
    ys_center = (np.max(ys)+np.min(ys))*0.5
    center = [xs_center,ys_center]
    min_distance = 100000
    
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
            for lab in unique_labels: # loop on the different clusters
                if lab != -1:
                    idx_lab = get_indexes(lab,labels)
                    #print('size of cluster level {} is {}'.format(j,len(idx_lab)))
                    #print('its ratio to total number {} is {}'.format(len(xs),len(idx_lab)/len(xs)))
                    cluster_size += len(idx_lab)
                    fraction = len(idx_lab)/len(xs)  
                    # classify the clusters according to their height and their size
                    if j == 0 and fraction >= fraction_big_small:
                        cluster_nb_zeros_big += 1
                    elif j == 0 and fraction < fraction_big_small:
                        cluster_nb_zeros_small += 1
                    elif j == 1 and fraction >= fraction_big_small:
                        cluster_nb_pos_big += 1
                    elif j == 1 and fraction < fraction_big_small:
                        cluster_nb_pos_small += 1
                    elif j == 2 and fraction >= fraction_big_small:
                        cluster_nb_neg_big += 1
                    elif j == 2 and fraction < fraction_big_small:
                        cluster_nb_neg_small += 1
                        
                    # record the biggest cluster per level
                    if j == 0 and len(idx_lab) >= biggest_zeros_size:
                        biggest_zeros_size = len(idx_lab)
                        biggest_zeros_idx = idx_lab 
                    elif j == 1 and len(idx_lab) >= biggest_pos_size:
                        biggest_pos_size = len(idx_lab)
                        biggest_pos_idx = idx_lab
                    elif j == 2 and len(idx_lab) >= biggest_neg_size:
                        biggest_neg_size = len(idx_lab)
                        biggest_neg_idx = idx_lab
                        
                    # white cluster closer to center
                    distance = 0
                    cnt = 0
                    if j == 1:
                        xs_white = [xs_pos[0][x] for x in idx_lab]
                        ys_white = [ys_pos[0][x] for x in idx_lab]
                        distance_in_cluster = 1000000
                        for c in range(len(idx_lab)):
                            cnt += 1
                            distance = np.sqrt((xs_white[c]-xs_center)*(xs_white[c]-xs_center)+(ys_white[c]-ys_center)*(ys_white[c]-ys_center))
                            if distance < distance_in_cluster:
                                distance_in_cluster = distance 
                        if distance_in_cluster < min_distance:
                            min_distance = distance_in_cluster
                            closest_pos_idx = idx_lab
                            
                        
                    
                    
            if n_clusters_ != 0:
                cluster_size_mean[j] = cluster_size/n_clusters_
            cluster_number[j] = n_clusters_
            # count total number of clusters per height level
            if j == 0:
                cluster_nb_zeros = n_clusters_
            elif j == 1:
                cluster_nb_pos = n_clusters_
            elif j == 2:
                cluster_nb_neg = n_clusters_
            
            # Plot results (Black removed and is used for noise instead)
            core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
            core_samples_mask[clustering.core_sample_indices_] = True
            
            colors = [plt.cm.Spectral(each)
                      for each in np.linspace(0, 1, len(unique_labels))]
                
            if plot_y_n_anat_clusters:
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
            
    #print('For control {} there are {} pos, {} neg, {} zeros'.format(i,cluster_number[0],cluster_number[1],cluster_number[2]))

    
    # BYSECTING LINE THROUGH ANATOMY
    # divide two cases 
    # case A) syngle gyrus --> consider only the negative values for the fit
    xs,ys,zs,fs,an = organize_data(data)
    if dupl_type == 'S':
        
        w_main_neg = [an_neg[0][x] for x in biggest_neg_idx]
        xs_main_neg = [xs_neg[0][x] for x in biggest_neg_idx]
        ys_main_neg = [ys_neg[0][x] for x in biggest_neg_idx]
        
        an_neg_rev = [-x for x in w_main_neg]
        coeff_w = np.polyfit(xs_main_neg,ys_main_neg,deg = 1, w = w_main_neg)
    
        x_fit = np.arange(np.nanmin(xs_neg[0]),np.nanmax(xs_neg[0]),0.01)  # use nanmin/nanmax since there is a nan value in pt[16]
        y_fit = x_fit*coeff_w[0]+coeff_w[1]
        
        if plot_y_n_fit_anat:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.scatter(xs,ys, c = an, cmap = 'gray')    
            plt.plot(x_fit,y_fit,'r',label = 'linear fit')
            cax, _ = matplotlib.colorbar.make_axes(ax)
            cbar = matplotlib.colorbar.ColorbarBase(cax, cmap='gray')
            cbar.ax.set_yticklabels(['< 0 convex', '','','','', '> 0 concave'])  # vertically oriented colorbar
            
            plt.title(title)
            plt.legend()
            #plt.show()
            output_dir = "../../figures/big_dataset/bysecting/anat/new/"
            fig.savefig('{}/{}.png'.format(output_dir,title))
    
        fit_anat = coeff_w
    # case B) partial duplication
    if dupl_type == 'PD':
        ################################################################
        weights = np.concatenate((an_pos[0],an_neg[0]))
        xs_conc = np.concatenate((xs_pos[0],xs_neg[0]))
        ys_conc = np.concatenate((ys_pos[0],ys_neg[0]))
        
        w_main_zeros = [an_zeros[0][x] for x in biggest_zeros_idx]
        xs_main_zeros = [xs_zeros[0][x] for x in biggest_zeros_idx]
        ys_main_zeros = [ys_zeros[0][x] for x in biggest_zeros_idx]
        
        #coeff_w = np.polyfit(xs_conc,ys_conc,deg = 1, w = weights)  # first way --> terrible results
        
        coeff_w_1 = np.polyfit(xs_main_zeros,ys_main_zeros,deg = 1, w = w_main_zeros)  # second way --> not good but not the worse
 
        coeff_w_2 = np.polyfit(xs_neg[0],ys_neg[0],deg = 1, w = an_neg[0])  # second way --> mmm
        
        coeff_w = 0.7*coeff_w_1+0.3*coeff_w_2
    
        x_fit = np.arange(np.nanmin(xs_zeros[0]),np.nanmax(xs_zeros[0]),0.01)  # use nanmin/nanmax since there is a nan value in pt[16]
        y_fit = x_fit*coeff_w[0]+coeff_w[1]
        y_fit_1 = x_fit*coeff_w_1[0]+coeff_w_1[1]
        y_fit_2 = x_fit*coeff_w_2[0]+coeff_w_2[1]
        ##################################################################
        
        w_main_pos = [an_pos[0][x] for x in closest_pos_idx]
        xs_main_pos = [xs_pos[0][x] for x in closest_pos_idx]
        ys_main_pos = [ys_pos[0][x] for x in closest_pos_idx]
        
        #plt.figure()
        #plt.scatter(xs_main_pos,ys_main_pos)
        
        coeff_w = np.polyfit(xs_main_pos,ys_main_pos,deg = 1, w = w_main_pos)
    
        x_fit = np.arange(np.nanmin(xs_neg[0]),np.nanmax(xs_neg[0]),0.01)  # use nanmin/nanmax since there is a nan value in pt[16]
        y_fit = x_fit*coeff_w[0]+coeff_w[1]
        
        if plot_y_n_fit_anat:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.scatter(xs,ys, c = an, cmap = 'gray')    
            plt.plot(x_fit,y_fit,'r',label = 'linear fit')
            #plt.plot(x_fit,y_fit_1,'b',label = 'fit on zeros')
            #plt.plot(x_fit,y_fit_2,'g',label = 'fit on neg')
            cax, _ = matplotlib.colorbar.make_axes(ax)
            cbar = matplotlib.colorbar.ColorbarBase(cax, cmap='gray')
            cbar.ax.set_yticklabels(['< 0 convex', '','','','', '> 0 concave'])  # vertically oriented colorbar
            
            plt.title(title)
            plt.legend()
            #plt.show()
            output_dir = "../../figures/big_dataset/bysecting/anat/new/"
            fig.savefig('{}/{}.png'.format(output_dir,title))
    
        fit_anat = coeff_w
        
    # case C) complete duplication
    if dupl_type == 'CD':    
        #w_main_pos = [an_pos[0][x] for x in biggest_pos_idx]
        #xs_main_pos = [xs_pos[0][x] for x in biggest_pos_idx]
        #ys_main_pos = [ys_pos[0][x] for x in biggest_pos_idx]
        
        w_main_pos = [an_pos[0][x] for x in closest_pos_idx]
        xs_main_pos = [xs_pos[0][x] for x in closest_pos_idx]
        ys_main_pos = [ys_pos[0][x] for x in closest_pos_idx]
        
        #plt.figure()
        #plt.scatter(xs_main_pos,ys_main_pos)
        
        coeff_w = np.polyfit(xs_main_pos,ys_main_pos,deg = 1, w = w_main_pos)
    
        x_fit = np.arange(np.nanmin(xs_neg[0]),np.nanmax(xs_neg[0]),0.01)  # use nanmin/nanmax since there is a nan value in pt[16]
        y_fit = x_fit*coeff_w[0]+coeff_w[1]
        
        if plot_y_n_fit_anat:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.scatter(xs,ys, c = an, cmap = 'gray')    
            plt.plot(x_fit,y_fit,'r',label = 'linear fit')
            #plt.scatter(xs_center,ys_center)
            cax, _ = matplotlib.colorbar.make_axes(ax)
            cbar = matplotlib.colorbar.ColorbarBase(cax, cmap='gray')
            cbar.ax.set_yticklabels(['< 0 convex', '','','','', '> 0 concave'])  # vertically oriented colorbar
            plt.title(title)
            plt.legend()
            #plt.show()
            output_dir = "../../figures/big_dataset/bysecting/anat/new/"
            fig.savefig('{}/{}.png'.format(output_dir,title))
    
        fit_anat = coeff_w
    
    return fit_anat

def cfr_bysecting_lines(data,title,fit_tono,fit_anat,fit_comb_tono_anat):
    xs,ys,zs,fs,an = organize_data(data)
    x_fit = np.arange(np.nanmin(xs),np.nanmax(xs),0.01)
    y_fit_tono = x_fit*fit_tono[0]+fit_tono[1]
    y_fit_anat = x_fit*fit_anat[0]+fit_anat[1]
    y_fit_comb = x_fit*fit_comb_tono_anat[0]+fit_comb_tono_anat[1]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xs,ys, c = fs, cmap = 'jet')    
    plt.plot(x_fit,y_fit_tono,color = 'k',linewidth = 4, label = 'tono')
    plt.plot(x_fit,y_fit_anat,color = 'g', linewidth = 4, label = 'anat')
    #plt.plot(x_fit,y_fit_comb,label = 'comb')
    plt.title(title)
    plt.legend()
    plt.show()
    
    
def data_in_hull(xs,ys,zs,fs,an,margin=0.25,plot_hull = False):
    points = np.column_stack((xs, ys))
    hull = ConvexHull(points)
    small_hull = np.zeros_like(hull.simplices)
    
    if plot_hull:
        plt.figure()
        plt.plot(points[:,0], points[:,1], 'o')
    center_x = (np.max(xs)+np.min(xs))*0.5
    center_y = (np.max(ys)+np.min(ys))*0.5
    center = np.column_stack((center_x,center_y))
    if plot_hull:
        plt.plot(center[0][0],center[0][1],'ro')
    for s,simplex in enumerate(hull.simplices):
        if plot_hull:
            plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
        
        x_hull = points[simplex, 0][0]
        y_hull = points[simplex, 1][0]  
        small_hull[s,0] = x_hull - margin*(x_hull-center_x)
        small_hull[s,1] = y_hull - margin*(y_hull-center_y)
    #convert int to list
    small_hull = list(small_hull)
    # sort by polar angle
    small_hull.sort(key=lambda p: math.atan2(p[1]-center_y,p[0]-center_x))
    # plot points
    if plot_hull:
        plt.plot([p[0] for p in small_hull],[p[1] for p in small_hull],'ro')
        pylab.figure()
        pylab.scatter([p[0] for p in points],[p[1] for p in points])
        pylab.scatter([p[0] for p in small_hull],[p[1] for p in small_hull])
    polygon = patches.Polygon(small_hull,closed=False,fill=True,color = 'g')
    path = polygon.get_path()
    
    points = list(points)
    contained = path.contains_points(points)
    contained_idx = list(np.where(contained))
    points_x = [points[p][0] for p in np.arange(len(points))]
    points_y = [points[p][1] for p in np.arange(len(points))]
    xs = np.asarray([points_x[idx] for idx in contained_idx[0]])
    ys = np.asarray([points_y[idx] for idx in contained_idx[0]])
    zs = np.asarray([zs[idx] for idx in contained_idx[0]])
    fs = np.asarray([fs[idx] for idx in contained_idx[0]])
    an = np.asarray([an[idx] for idx in contained_idx[0]])
    contained_points = np.column_stack((xs,ys))

    if plot_hull:
        pylab.scatter(contained_points[:,0],contained_points[:,1],color = 'k')
    
    return xs,ys,zs,fs,an