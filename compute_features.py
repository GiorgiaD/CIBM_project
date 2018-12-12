# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 22:36:42 2018

@author: Giorgia
"""

# this script does the preprocessing of the data: given the list of files it imports the data, 
# computes different operations such as finding the bysecting line and returns an array of features 

from import_function import *
import scipy.io
import matplotlib

# the main function
def compute_features(data_tono, data_anat, data_dupl, data_names, which_dataset, which_fit = 'comb_tono_anat'):
    
    # import data
    threeD_data = import_data_from_list(data_tono, data_anat, which_dataset) 
    
    # preprocessing
    # 1) bysecting line
    fit_tono, fit_anat, fit_comb_tono_anat, fit, theta_diff = bysecting_lines_angles_cfr(threeD_data, data_dupl, data_names, which_fit = 'comb_tono_anat')
    # 2) mean distance of frequencies from line and difference number above-below line
    mean_dist, above_minus_below = average_distance_and_voxel_number(threeD_data, data_names, fit)
    # 3) angle defined by vertices LHL and distance between the two Furthest-from-line High voxels
    angle_HLH, dist_HH = angle_HLH_and_dist(threeD_data, data_names, fit)
    
    
    # Now put the features together
    # each line gives the different features for one scan, while each column contains one feature for all the scans
    # the features are:
    # a) the difference in number of voxels above and below (14 values per scan)
    # b) the mean distance of voxels from bysecting line (14 values per scan)
    # c) the angle defined by the vertices High-Low-High (1 value per scan)
    # d) the distance between the two Furthest-from-line High voxels
    # e) the angle between the anatomic and the tonotopic bisection line (1 value per scan)
    # f) the distance between the bisecting lines (1 value per scan) --> to be done
    
    #print('above-below',above_minus_below)
    #print('mean_dist',mean_dist)
    #print('angle HLH',angle_HLH)
    #print('dist_HH',dist_HH)
    #print('theta_diff',theta_diff)
    
    features = np.concatenate((above_minus_below, mean_dist, angle_HLH, dist_HH, theta_diff), axis = 1)
    
    print('features',np.shape(features))
    
    return features

# the functions exploited in compute_features
def import_data_from_list(data_tono, data_anat, which_dataset):
    scan_number = np.shape(data_tono)[0]
    
    if which_dataset == 'normalized':
        threeD_data = np.ones([scan_number,5,1000])*(-2) # less voxels for the normalized scan
    else:
        threeD_data = np.ones([scan_number,5,6000])*(-2)  # more voxels for the original scan
    
    for i in range(scan_number):
        # tonotopy
        if which_dataset == 'normalized' or which_dataset == 'big_dataset':    
            mydata = import_function(data_tono[i])
        else:
            mydata = scipy.io.loadmat(data_tono[i])['data']
        # anatomy
        if which_dataset != 'normalized' and which_dataset != 'big_dataset':
            mydata_anat = scipy.io.loadmat(data_anat[i])['data']
        elif which_dataset == 'big_dataset':
            mydata_anat = import_function(data_anat[i])
        
        max_len = np.shape(mydata)[0]
        # import x
        threeD_data[i,0,0:max_len] = mydata[:,1]
        # import y
        threeD_data[i,1,0:max_len] = mydata[:,2]
        # import z
        threeD_data[i,2,0:max_len] = mydata[:,3]
        # import f
        threeD_data[i,3,0:max_len] = 14-mydata[:,7]
        # import anatomy
        if which_dataset != 'normalized'or which_dataset == 'big_dataset':
            threeD_data[i,4,0:max_len] = mydata_anat[:,7]
    
    return threeD_data

def bysecting_lines_angles_cfr(threeD_data, data_dupl, data_names, which_fit = 'comb_tono_anat'):
    # BYSECTING LINE - FIND 
    scan_number = np.shape(threeD_data)[0]
    # A) Only tono
    fit_tono = np.zeros([scan_number,2])
    for i in range(scan_number):
        fit_tono[i,:] = bysect_line(threeD_data[i,:,:], data_names[i], False) # NB here fs is already 14-fs
    
    # B) Only anat
    anat_classify = np.zeros([scan_number,1])  # which gyrus shape does the person have?
    fit_anat = np.zeros([scan_number,2])   # fit of parameters on the basis of anatomy
    for i in range(scan_number):
        #ctl_anat_classify[i], fit_ctl_anat[i,:] = anatomy(ctl_threeD_data[i,:,:],ctl_name[i],plot_y_n_three_anat_regions_ctl,plot_y_n_anat_clusters_ctl,plot_y_n_fit_anat_ctl)
        
        fit_anat[i,:] = anatomy_new(threeD_data[i,:,:],data_names[i], data_dupl[i], False, False, False)
              
    # C) Combined tono and anat  ---> tono weights 20%, anat weights 80%
    # which weights you want to assign to the two lines?
    perc_tono = 0.5
    perc_anat = 1.-perc_tono
    # Controls
    fit_comb_tono_anat = perc_tono*fit_tono+perc_anat*fit_anat
      
    # Find the angle between the tonotopic and the anatomic bysecting lines
    theta_diff = np.zeros([scan_number,1])
    for i in range(scan_number):
        theta_tono = np.arctan(fit_tono[i,0])
        theta_anat = np.arctan(fit_anat[i,0])
        theta_diff[i] = np.abs(theta_tono-theta_anat)
    
    # set which fit to use for the next computations
    if which_fit == 'tono_only':
        fit = fit_tono
    elif which_fit == 'anat_only':
        fit = fit_anat
    elif which_fit == 'comb_tono_anat':
        fit = fit_comb_tono_anat

    return fit_tono, fit_anat, fit_comb_tono_anat, fit, theta_diff


def average_distance_and_voxel_number(threeD_data, data_names, fit):
    # AVERAGE DISTANCE AND NUMBER OF VOXELS ABOVE AND BELOW
    scan_number = np.shape(threeD_data)[0]
    mean_dist = np.zeros([scan_number,14])
    above_minus_below = np.zeros([scan_number,14])
    # find the mean distance for each scan
    # CHANGE HERE NOT TO NEED NAME NOR PLOT_YN
    for i in range(scan_number):
        mean_dist[i,:], above_minus_below[i,:] = mean_dist_b_line(threeD_data[i,:,:], data_names[i], fit[i,:], False)
           
    return mean_dist, above_minus_below

def angle_HLH_and_dist(threeD_data, data_names, fit):
    scan_number = np.shape(threeD_data)[0]
    angle_HLH = np.zeros([scan_number,1])
    dist_HH = np.zeros([scan_number,1])
    for i in range(scan_number):
        angle_HLH[i],_,_,_,_,_,_,dist_HH[i] = find_angles(threeD_data[i,:,:],data_names[i],fit[i,:], False, False)
        
    return angle_HLH, dist_HH