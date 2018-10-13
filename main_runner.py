# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:36:12 2018

@author: Giorgia
"""

from import_function import *
import scipy.io

plt.close('all')

ctl_list_norm = ['CTL1_tono_voi_onRef_PAC_RH.txt','CTL1_tono_voi_onRef_PAC_LH.txt',
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

pt_list_norm = ['PT1_tono_voi_onRef_PAC_RH.txt','PT1_tono_voi_onRef_PAC_LH.txt',
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

ctl_list_full = ['CTL1_tono_poi_PAC_RH', 'CTL1_tono_poi_PAC_LH',
                 'CTL2_tono_poi_PAC_RH', 'CTL2_tono_poi_PAC_LH',
                 'CTL3_tono_poi_PAC_RH', 'CTL3_tono_poi_PAC_LH',
                 'CTL4_tono_poi_PAC_RH', 'CTL4_tono_poi_PAC_LH',
                 'CTL5_tono_poi_PAC_RH', 'CTL5_tono_poi_PAC_LH',
                 'CTL6_tono_poi_PAC_RH', 'CTL6_tono_poi_PAC_LH',
                 'CTL7_tono_poi_PAC_RH', 'CTL7_tono_poi_PAC_LH',
                 'CTL8_tono_poi_PAC_RH', 'CTL8_tono_poi_PAC_LH',
                 'CTL9_tono_poi_PAC_RH', 'CTL9_tono_poi_PAC_LH',
                 'CTL10_tono_poi_PAC_RH', 'CTL10_tono_poi_PAC_LH',
                 'CTL12_tono_poi_PAC_RH', 'CTL12_tono_poi_PAC_LH']

pt_list_full = ['PT1_tono_poi_PAC_RH', 'PT1_tono_poi_PAC_LH',
                'PT2_tono_poi_PAC_RH', 'PT2_tono_poi_PAC_RH',
                'PT3_tono_poi_PAC_RH', 'PT3_tono_poi_PAC_RH',
                'PT4_tono_poi_PAC_RH', 'PT4_tono_poi_PAC_LH',
                'PT5_tono_poi_PAC_RH', 'PT5_tono_poi_PAC_LH',
                'PT6_tono_poi_PAC_LH', 'PT6_tono_poi_PAC_LH',
                'PT7_tono_poi_PAC_LH', 'PT7_tono_poi_PAC_LH',
                'PT8_tono_poi_PAC_RH', 'PT8_tono_poi_PAC_LH',
                'PT9_tono_poi_PAC_RH', 'PT9_tono_poi_PAC_LH',
                'PT10_tono_poi_PAC_LH', 'PT10_tono_poi_PAC_LH',
                'PT11_tono_poi_PAC_RH', 'PT11_tono_poi_PAC_LH',
                'PT12_tono_poi_PAC_RH', 'PT12_tono_poi_PAC_LH',
                'PT13_tono_poi_PAC_RH', 'PT13_tono_poi_PAC_LH',
                'PT14_tono_poi_PAC_LH', 'PT14_tono_poi_PAC_LH',
                'PT15_tono_poi_PAC_RH', 'PT15_tono_poi_PAC_LH',
                'PT16_tono_poi_PAC_RH', 'PT16_tono_poi_PAC_LH',
                'PT17_tono_poi_PAC_RH', 'PT17_tono_poi_PAC_LH',
                'PT18_tono_poi_PAC_RH', 'PT18_tono_poi_PAC_RH',
                'PT19_tono_poi_PAC_LH', 'PT19_tono_poi_PAC_LH',
                'PT20_tono_poi_PAC_RH', 'PT20_tono_poi_PAC_LH',
                'PT21_tono_poi_PAC_RH', 'PT21_tono_poi_PAC_RH',
                'PT22_tono_poi_PAC_RH', 'PT22_tono_poi_PAC_RH',
                'PT23_tono_poi_PAC_LH', 'PT23_tono_poi_PAC_LH',
                'PT24_tono_poi_PAC_RH', 'PT24_tono_poi_PAC_RH'] # careful we're missing PT2LH,PT3LH,PT6RH,PT7RH,PT10RH,PT14RH,PT18LH,PT19RH,PT21LH,PT22LH,PT23RH,PT24LH

ctl_anat = ['CTL1_anat_poi_PAC_RH', 'CTL1_anat_poi_PAC_LH',
            'CTL2_anat_poi_PAC_RH', 'CTL2_anat_poi_PAC_LH',
            'CTL3_anat_poi_PAC_RH', 'CTL3_anat_poi_PAC_LH',
            'CTL4_anat_poi_PAC_RH', 'CTL4_anat_poi_PAC_LH',
            'CTL5_anat_poi_PAC_RH', 'CTL5_anat_poi_PAC_LH',
            'CTL6_anat_poi_PAC_RH', 'CTL6_anat_poi_PAC_LH',
            'CTL7_anat_poi_PAC_RH', 'CTL7_anat_poi_PAC_LH',
            'CTL8_anat_poi_PAC_RH', 'CTL8_anat_poi_PAC_LH',
            'CTL9_anat_poi_PAC_RH', 'CTL9_anat_poi_PAC_LH',
            'CTL10_anat_poi_PAC_RH', 'CTL10_anat_poi_PAC_LH',
            'CTL11_anat_poi_PAC_RH', 'CTL12_anat_poi_PAC_LH']

pt_anat = ['PT1_anat_poi_PAC_RH', 'PT1_anat_poi_PAC_LH',
           'PT2_anat_poi_PAC_RH', 'PT2_anat_poi_PAC_RH',
           'PT3_anat_poi_PAC_RH', 'PT3_anat_poi_PAC_LH',
           'PT4_anat_poi_PAC_RH', 'PT4_anat_poi_PAC_LH',
           'PT5_anat_poi_PAC_RH', 'PT5_anat_poi_PAC_LH',
           'PT6_anat_poi_PAC_RH', 'PT6_anat_poi_PAC_LH',
           'PT7_anat_poi_PAC_RH', 'PT7_anat_poi_PAC_LH',
           'PT8_anat_poi_PAC_RH', 'PT8_anat_poi_PAC_LH',
           'PT9_anat_poi_PAC_RH', 'PT9_anat_poi_PAC_LH',
           'PT10_anat_poi_PAC_RH', 'PT10_anat_poi_PAC_LH',
           'PT11_anat_poi_PAC_RH', 'PT11_anat_poi_PAC_LH',
           'PT12_anat_poi_PAC_RH', 'PT12_anat_poi_PAC_LH',
           'PT13_anat_poi_PAC_RH', 'PT13_anat_poi_PAC_LH',
           'PT14_anat_poi_PAC_RH', 'PT14_anat_poi_PAC_LH',
           'PT15_anat_poi_PAC_RH', 'PT15_anat_poi_PAC_LH',
           'PT16_anat_poi_PAC_RH', 'PT16_anat_poi_PAC_LH',
           'PT17_anat_poi_PAC_RH', 'PT17_anat_poi_PAC_LH',
           'PT18_anat_poi_PAC_RH', 'PT18_anat_poi_PAC_LH',
           'PT19_anat_poi_PAC_RH', 'PT19_anat_poi_PAC_LH',
           'PT20_anat_poi_PAC_RH', 'PT20_anat_poi_PAC_LH',
           'PT21_anat_poi_PAC_RH', 'PT21_anat_poi_PAC_LH',
           'PT22_anat_poi_PAC_RH', 'PT22_anat_poi_PAC_LH',
           'PT23_anat_poi_PAC_RH', 'PT23_anat_poi_PAC_LH',
           'PT24_anat_poi_PAC_RH', 'PT24_anat_poi_PAC_LH']  # careful we're missing PT2LH


ctl_name = ['Control 1 - RH','Control 1 - LH',
            'Control 2 - RH','Control 2 - LH',
            'Control 3 - RH','Control 3 - LH',
            'Control 4 - RH','Control 4 - LH',
            'Control 5 - RH','Control 5 - LH',
            'Control 6 - RH','Control 6 - LH',
            'Control 7 - RH','Control 7 - LH',
            'Control 8 - RH','Control 8 - LH',
            'Control 9 - RH','Control 9 - LH',
            'Control 10 - RH','Control 10 - LH',
            'Control 12 - RH','Control 12 - LH',
            'Control 13 - RH','Control 13 - LH']

pt_name = ['Patient 1 - RH', 'Patient 1 - LH',
           'Patient 2 - RH', 'Patient 2 - LH',
           'Patient 3 - RH', 'Patient 3 - LH',
           'Patient 4 - RH', 'Patient 4 - LH',
           'Patient 5 - RH', 'Patient 5 - LH',
           'Patient 6 - RH', 'Patient 6 - LH',
           'Patient 7 - RH', 'Patient 7 - LH',
           'Patient 8 - RH', 'Patient 8 - LH',
           'Patient 9 - RH', 'Patient 9 - LH',
           'Patient 10 - RH', 'Patient 10 - LH',
           'Patient 11 - RH', 'Patient 11 - LH',
           'Patient 12 - RH', 'Patient 12 - LH',
           'Patient 13 - RH', 'Patient 13 - LH',
           'Patient 14 - RH', 'Patient 14 - LH',
           'Patient 15 - RH', 'Patient 15 - LH',
           'Patient 16 - RH', 'Patient 16 - LH',
           'Patient 17 - RH', 'Patient 17 - LH',
           'Patient 18 - RH', 'Patient 18 - LH',
           'Patient 19 - RH', 'Patient 19 - LH',
           'Patient 20 - RH', 'Patient 20 - LH',
           'Patient 21 - RH', 'Patient 21 - LH',
           'Patient 22 - RH', 'Patient 22 - LH',
           'Patient 23 - RH', 'Patient 23 - LH',
           'Patient 24 - RH', 'Patient 24 - LH']

use_norm_data = False

if use_norm_data:  
    ctl_list = ctl_list_norm
    pt_list = pt_list_norm
else: 
    ctl_list = ctl_list_full
    pt_list = pt_list_full

# IMPORT DATA
# work with Controls
ctl_number = np.shape(ctl_list)[0]
if use_norm_data:
    ctl_3D_data = np.ones([ctl_number,4,1000])*(-2)
else:
    ctl_3D_data = np.ones([ctl_number,4,1800])*(-2)
    
for i in range(ctl_number):
    if use_norm_data:    
        mydata = import_function(ctl_list[i])
    else:
        mydata = scipy.io.loadmat(ctl_list[i])['data']
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
if use_norm_data:
    pt_3D_data = np.ones([pt_number,4,1000])*(-2)
else:
    pt_3D_data = np.ones([pt_number,4,1800])*(-2)

for i in range(pt_number):
    if use_norm_data:    
        mydata = import_function(pt_list[i])
    else:
        mydata = scipy.io.loadmat(pt_list[i])['data']
    max_len = np.shape(mydata)[0]
    # import x
    pt_3D_data[i,0,0:max_len] = mydata[:,1]
    # import y
    pt_3D_data[i,1,0:max_len] = mydata[:,2]
    # import z
    pt_3D_data[i,2,0:max_len] = mydata[:,3]
    # import f
    pt_3D_data[i,3,0:max_len] = 14-mydata[:,7]


# PLOTS
# work with Controls
how_many_plots = 'plot_until'  # choose among 'plot_all','plot_RH','plot_LH','plot_until'
plot_until = 18
if how_many_plots == 'plot_all':
    tot_plot = np.arange(np.shape(ctl_list)[0])
elif how_many_plots == 'plot_RH':
    tot_plot = np.arange(0,np.shape(ctl_list)[0],2)
elif how_many_plots == 'plot_LH':
    tot_plot = np.arange(1,np.shape(ctl_list)[0],2)
elif how_many_plots == 'plot_until':
    tot_plot = np.arange(0,plot_until)
    
threeD_plot = False
twoD_plot = False



#tot_plot = np.arange(0,8,2)
 # 3d interactive plots   
if threeD_plot:
    for i in tot_plot:
        file_name = ctl_list[i]
        file_title = ctl_name[i]
        if use_norm_data:    
            my_data = import_function(ctl_list[i])
        else:
            my_data = scipy.io.loadmat(ctl_list[i])['data']
        plot_tono_map(my_data, file_title)

# 2d subplots
if twoD_plot:
    for i in tot_plot:
        file_name = ctl_list[i]
        file_title = ctl_name[i]
        if use_norm_data:    
            my_data = import_function(ctl_list[i])
        else:
            my_data = scipy.io.loadmat(ctl_list[i])['data']
        plot_2d(my_data,file_title)
              
        
# work with Patients
how_many_plots = 'plot_all'  # choose among 'plot_all','plot_RH','plot_LH','plot_until'
plot_until = 6
if how_many_plots == 'plot_all':
    tot_plot = np.arange(np.shape(pt_list)[0])
elif how_many_plots == 'plot_RH':
    tot_plot = np.arange(int(np.shape(pt_list)[0]/2),np.shape(pt_list)[0],2)
elif how_many_plots == 'plot_LH':
    tot_plot = np.arange(1,int(np.shape(pt_list)[0]/2)+1,2)
elif how_many_plots == 'plot_until':
    tot_plot = np.arange(0,plot_until)
    
threeD_plot = False
twoD_plot = False

#tot_plot = np.arange(0,8,2)
 # 3d interactive plots   
if threeD_plot:
    for i in tot_plot:
        file_name = pt_list[i]
        file_title = pt_name[i]
        if use_norm_data:    
            my_data = import_function(pt_list[i])
        else:
            my_data = scipy.io.loadmat(pt_list[i])['data']
        plot_tono_map(my_data, file_title)

# 2d subplots
if twoD_plot:
    for i in tot_plot:
        file_name = pt_list[i]
        file_title = pt_name[i]
        if use_norm_data:    
            my_data = import_function(pt_list[i])
        else:
            my_data = scipy.io.loadmat(pt_list[i])['data']
        plot_2d(my_data,file_title)



# BYSECTING LINE - FIND AND PLOT
# Controls
fit_ctl = np.zeros([ctl_number,2])
plot_y_n = False
for i in range(ctl_number):
    fit_ctl[i,:] = bysect_line(ctl_3D_data[i,:,:], ctl_name[i], plot_y_n) # NB here fs is already 14-fs
# Patients
fit_pt = np.zeros([pt_number,2])
plot_y_n = False
for i in range(pt_number):
    fit_pt[i,:] = bysect_line(pt_3D_data[i,:,:], pt_name[i], plot_y_n)
    
# AVERAGE DISTANCE AND NUMBER OF VOXELS ABOVE AND BELOW
# Controls
mean_dist_ctl = np.zeros([ctl_number,14])
above_minus_below = np.zeros([ctl_number,14])
plot_y_n = False
# find the mean distance for each scan
for i in range(ctl_number):
    mean_dist_ctl[i,:], above_minus_below[i,:] = mean_dist_b_line(ctl_3D_data[i,:,:], ctl_name[i], fit_ctl[i,:], plot_y_n)
# find mean and std of the results of the scans
mean_of_mean_dist_ctl = np.mean(mean_dist_ctl, axis = 0)
std_of_mean_dist_ctl = np.std(mean_dist_ctl, axis = 0)
lower_bound = mean_of_mean_dist_ctl - std_of_mean_dist_ctl
upper_bound = mean_of_mean_dist_ctl + std_of_mean_dist_ctl
plot_y_n = True
if plot_y_n:
    fig,ax = plt.subplots(1)
    ax.plot(np.arange(14),mean_of_mean_dist_ctl,lw = 2, color = 'black', label = 'average distance')
    ax.fill_between(np.arange(14), lower_bound, upper_bound, facecolor = 'yellow', alpha = 0.5, label = 'std')
    ax.legend(loc = 'upper left')
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Mean distance')
    ax.set_title('CONTROLS Average distance from bysecting line vs frequency')
# find mean difference between voxels above and below line
mean_of_diff_ctl = np.mean(above_minus_below, axis = 0)
std_of_diff_ctl = np.std(above_minus_below, axis = 0)
lower_bound = mean_of_diff_ctl - std_of_diff_ctl
upper_bound = mean_of_diff_ctl + std_of_diff_ctl
plot_y_n = False
if plot_y_n:
    fig,ax = plt.subplots(1)
    ax.plot(np.arange(14),mean_of_diff_ctl,lw = 2, color = 'blue', label = 'average difference')
    ax.fill_between(np.arange(14), lower_bound, upper_bound, facecolor = 'green', alpha = 0.5, label = 'std')
    ax.legend(loc = 'upper left')
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Mean difference')
    ax.set_title('CONTROLS Average difference above-below vs frequency')

# Patients
mean_dist_pt = np.zeros([pt_number,14])
above_minus_below = np.zeros([pt_number,14])
plot_y_n = False
# find the mean distance for each scan
for i in range(pt_number):
    mean_dist_pt[i,:], above_minus_below[i,:] = mean_dist_b_line(pt_3D_data[i,:,:], pt_name[i], fit_pt[i,:], plot_y_n)
# find mean and std of the results of the scans
mean_of_mean_dist_pt = np.mean(mean_dist_pt, axis = 0)
std_of_mean_dist_pt = np.std(mean_dist_pt, axis = 0)
lower_bound = mean_of_mean_dist_pt - std_of_mean_dist_pt
upper_bound = mean_of_mean_dist_pt + std_of_mean_dist_pt
plot_y_n = False
if plot_y_n:
    fig,ax = plt.subplots(1)
    ax.plot(np.arange(14),mean_of_mean_dist_pt,lw = 2, color = 'black', label = 'average distance')
    ax.fill_between(np.arange(14), lower_bound, upper_bound, facecolor = 'yellow', alpha = 0.5, label = 'std')
    ax.legend(loc = 'upper left')
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Mean distance')
    ax.set_title('PATIENTS Average distance from bysecting line vs frequency')
# find mean difference between voxels above and below line
mean_of_diff_pt = np.mean(above_minus_below, axis = 0)
std_of_diff_pt = np.std(above_minus_below, axis = 0)
lower_bound = mean_of_diff_pt - std_of_diff_pt
upper_bound = mean_of_diff_pt + std_of_diff_pt
plot_y_n = False
if plot_y_n:
    fig,ax = plt.subplots(1)
    ax.plot(np.arange(14),mean_of_diff_pt,lw = 2, color = 'blue', label = 'average difference')
    ax.fill_between(np.arange(14), lower_bound, upper_bound, facecolor = 'green', alpha = 0.5, label = 'std')
    ax.legend(loc = 'upper left')
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Mean difference')
    ax.set_title('PATIENTS Average difference above-below vs frequency')



# DIVDE THREE RANGES OF FREQUENCIES AND COMPUTE NUMBER AND SIZE OF CLUSTERS
# Controls
plot_y_n = False
plot_hist = False
cluster_num_ctl = np.zeros([ctl_number,3])
cluster_size_ctl = np.zeros([ctl_number,3])

eps_loop = np.arange(0.5,2.5,0.5)

for eps in eps_loop:
    for i in range(ctl_number):
        cluster_num_ctl[i,:], cluster_size_ctl[i,:] = three_f_ranges(ctl_3D_data[i,:,:],ctl_name[i], fit_ctl[i,:], plot_y_n, eps = eps, min_samples = 3)
    if plot_hist:
        fig, (ax1, ax2) = plt.subplots(1, 2)
        ax1.set_title('CONTROLS Number of clusters')
        ax1.set_xlabel('Number of clusters')
        ax1.set_ylabel('Occurrency')
        ax1.hist(cluster_num_ctl[:,0], bins = 30, alpha = 0.4, label = 'Low frequency')
        ax1.hist(cluster_num_ctl[:,1], bins = 30, alpha = 0.4, label = 'Medium frequency')
        ax1.hist(cluster_num_ctl[:,2], bins = 30, alpha = 0.4, label = 'High frequency')
        ax1.legend()
        
        ax2.set_title('Size of clusters - Epsilon = {}'.format(eps))
        ax2.set_xlabel('Size of clusters')
        ax2.set_ylabel('Occurrency')
        ax2.hist(cluster_size_ctl[:,0], bins = 30, alpha = 0.4, label = 'Low frequency')
        ax2.hist(cluster_size_ctl[:,1], bins = 30, alpha = 0.4, label = 'Medium frequency')
        ax2.hist(cluster_size_ctl[:,2], bins = 30, alpha = 0.4, label = 'High frequency')
        ax2.legend()
        
    # Patients
    plot_y_n = False
    cluster_num_pt = np.zeros([pt_number,3])
    cluster_size_pt = np.zeros([pt_number,3])
    for i in range(pt_number):
        cluster_num_pt[i,:], cluster_size_pt[i,:] = three_f_ranges(pt_3D_data[i,:,:],pt_name[i], fit_pt[i,:], plot_y_n, eps = eps, min_samples = 3)
    if plot_hist:
        fig, (ax1, ax2) = plt.subplots(1, 2)
        ax1.set_title('PATIENTS Number of clusters')
        ax1.set_xlabel('Number of clusters')
        ax1.set_ylabel('Occurrency')
        ax1.hist(cluster_num_pt[:,0], bins = 30, alpha = 0.4, label = 'Low frequency')
        ax1.hist(cluster_num_pt[:,1], bins = 30, alpha = 0.4, label = 'Medium frequency')
        ax1.hist(cluster_num_pt[:,2], bins = 30, alpha = 0.4, label = 'High frequency')
        ax1.legend()
        
        ax2.set_title('Size of clusters - Epsilon = {}'.format(eps))
        ax2.set_xlabel('Size of clusters')
        ax2.set_ylabel('Occurrency')
        ax2.hist(cluster_size_pt[:,0], bins = 30, alpha = 0.4, label = 'Low frequency')
        ax2.hist(cluster_size_pt[:,1], bins = 30, alpha = 0.4, label = 'Medium frequency')
        ax2.hist(cluster_size_pt[:,2], bins = 30, alpha = 0.4, label = 'High frequency')
        ax2.legend()
        
# MATRIXING
# Work with Controls
plot_y_n = True
if use_norm_data:
    pixels = 35
else:
    pixels = 24
for i in range(ctl_number):
    ctl_mat = matrixing(ctl_3D_data[i,:,:], ctl_name[i], pixels, plot_y_n)

for i in range(pt_number):
    pt_mat = matrixing(pt_3D_data[i,:,:], pt_name[i], pixels, plot_y_n)

    




#sk learn rich regression