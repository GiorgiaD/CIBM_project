# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:36:12 2018

@author: Giorgia
"""

from import_function import *

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

print(np.shape(ctl_list))

file_name = 'CTL1_tono_voi_onRef_PAC_RH.txt'

# work with Controls
how_many_plots = 'plot_LH'  # choose among 'plot_all','plot_RH','plot_LH','plot_until'
plot_until = 6
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
        my_data = import_function(file_name)
        plot_tono_map(my_data, file_title)

# 2d subplots
if twoD_plot:
    for i in tot_plot:
        file_name = ctl_list[i]
        file_title = ctl_name[i]
        my_data = import_function(file_name)
        plot_2d(my_data,file_title)
        
# work with Patients
how_many_plots = 'plot_LH'  # choose among 'plot_all','plot_RH','plot_LH','plot_until'
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
twoD_plot = True

#tot_plot = np.arange(0,8,2)
 # 3d interactive plots   
if threeD_plot:
    for i in tot_plot:
        file_name = pt_list[i]
        file_title = pt_name[i]
        my_data = import_function(file_name)
        plot_tono_map(my_data, file_title)

# 2d subplots
if twoD_plot:
    for i in tot_plot:
        file_name = pt_list[i]
        file_title = pt_name[i]
        my_data = import_function(file_name)
        plot_2d(my_data,file_title)



# sk learn rich regression