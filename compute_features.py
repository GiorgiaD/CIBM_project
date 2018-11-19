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

def compute_features(data_tono, data_anat, data_dupl, data_names, targets, which_dataset):
    # import data
    3D_data = import_data_from_list(data_tono, data_anat, which_dataset)
    # preprocessing
    # 1) bysecting line
    fit_tono, fit_anat, fit_comb_tono_anat, fit, theta_diff = bysecting_lines_angles_cfr(3D_data, data_dupl, data_names, which_fit = 'comb_tono_anat')
    # 2) mean distance of frequencies from line and difference number above-below line
    mean_dist, above_minus_below = average_distance_and_voxel_number(3D_data, data_names, fit)
    
    
    # put the features together
    features = []
    
    return features

def import_data_from_list(data_tono, data_anat, which_dataset):
    scan_number = np.shape(data_tono)[0]
    
    if which_dataset == 'normalized':
        3D_data = np.ones([scan_number,5,1000])*(-2) # less voxels for the normalized scan
    else:
        3D_data = np.ones([scan_number,5,1800])*(-2)  # more voxels for the original scan
    
    for i in range(scan_number):
        # tonotopy
        if which_dataset == 'normalized':    
            mydata = import_function(data_tono[i])
        else:
            mydata = scipy.io.loadmat(data_tono[i])['data']
        # anatomy
        if which_dataset != 'normalized':
            mydata_anat = scipy.io.loadmat(data_anat[i])['data']
        
        max_len = np.shape(mydata)[0]
        # import x
        3D_data[i,0,0:max_len] = mydata[:,1]
        # import y
        3D_data[i,1,0:max_len] = mydata[:,2]
        # import z
        3D_data[i,2,0:max_len] = mydata[:,3]
        # import f
        3D_data[i,3,0:max_len] = 14-mydata[:,7]
        # import anatomy
        if which_dataset != 'normalized':
            3D_data[i,4,0:max_len] = mydata_anat[:,7]
    
    return 3D_data 

def bysecting_lines_angles_cfr(3D_data, data_dupl, data_names, which_fit = 'comb_tono_anat'):
    # BYSECTING LINE - FIND 
    scan_number = np.shape(3D_data)[0]
    # A) Only tono
    fit_tono = np.zeros([scan_number,2])
    for i in range(scan_number):
        # CHANGE HERE NOT TO NEED NAME NOR PLOT_YN
        fit_tono[i,:] = bysect_line(3D_data[i,:,:], data_name[i], plot_y_n_fit_ctl) # NB here fs is already 14-fs
    
    # B) Only anat
    anat_classify = np.zeros(scan_number)  # which gyrus shape does the person have?
    fit_anat = np.zeros([scan_number,2])   # fit of parameters on the basis of anatomy
    for i in range(scan_number):
        #ctl_anat_classify[i], fit_ctl_anat[i,:] = anatomy(ctl_3D_data[i,:,:],ctl_name[i],plot_y_n_three_anat_regions_ctl,plot_y_n_anat_clusters_ctl,plot_y_n_fit_anat_ctl)
        
        # CHANGE HERE NOT TO NEED NAME NOR PLOT_YN
        fit_anat[i,:] = anatomy_new(3D_data[i,:,:],data_name[i], data_dupl[i], plot_y_n_three_anat_regions_ctl,plot_y_n_anat_clusters_ctl,plot_y_n_fit_anat_ctl)
              
    # C) Combined tono and anat  ---> tono weights 20%, anat weights 80%
    # which weights you want to assign to the two lines?
    perc_tono = 0.5
    perc_anat = 1.-perc_tono
    # Controls
    fit_comb_tono_anat = perc_tono*fit_tono+perc_anat*fit_anat
      
    # Find the angle between the tonotopic and the anatomic bysecting lines
    theta_diff = np.zeros(scan_number)
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


def average_distance_and_voxel_number(3D_data, data_names, fit):
    # AVERAGE DISTANCE AND NUMBER OF VOXELS ABOVE AND BELOW
    scan_number = np.shape(3D_data)[0]
    mean_dist = np.zeros([scan_number,14])
    above_minus_below = np.zeros([scan_number,14])
    # find the mean distance for each scan
    # CHANGE HERE NOT TO NEED NAME NOR PLOT_YN
    for i in range(scan_number):
        mean_dist[i,:], above_minus_below[i,:] = mean_dist_b_line(3D_data[i,:,:], data_names[i], fit[i,:], plot_y_n_dist_each_ctl)
           
    return mean_dist, above_minus_below