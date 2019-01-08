# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:11:55 2018

@author: Giorgia
"""
from import_function import *
import scipy.io
import matplotlib
from scipy.spatial import ConvexHull
import matplotlib.path as mplPath
import pylab
import math
import matplotlib.patches as patches

plt.close('all')

big_dataset_tono = ['C1_tono_poi_STG_LH.txt','C1_tono_poi_STG_RH.txt',
                    'C2_tono_poi_STG_LH.txt','C2_tono_poi_STG_RH.txt',
                    'C3_tono_poi_STG_LH.txt','C3_tono_poi_STG_RH.txt',
                    'C4_tono_poi_STG_LH.txt','C4_tono_poi_STG_RH.txt',
                    'C5_tono_poi_STG_LH.txt','C5_tono_poi_STG_RH.txt',
                    'C6_tono_poi_STG_LH.txt','C6_tono_poi_STG_RH.txt',
                    'C7_tono_poi_STG_LH.txt','C7_tono_poi_STG_RH.txt',
                    'C8_tono_poi_STG_LH.txt','C8_tono_poi_STG_RH.txt',
                    'C9_tono_poi_STG_LH.txt','C9_tono_poi_STG_RH.txt',
                    'C10_tono_poi_STG_LH.txt','C10_tono_poi_STG_RH.txt',
                    'C11_tono_poi_STG_LH.txt','C11_tono_poi_STG_RH.txt',
                    'C12_tono_poi_STG_LH.txt','C12_tono_poi_STG_RH.txt',
                    'C13_tono_poi_STG_LH.txt','C13_tono_poi_STG_RH.txt',
                    'C14_tono_poi_STG_LH.txt','C14_tono_poi_STG_RH.txt',
                    'C15_tono_poi_STG_LH.txt',
                    'C16_tono_poi_STG_LH.txt',
                    
                    'C18_tono_poi_STG_LH.txt','C18_tono_poi_STG_RH.txt',
                    'C19_tono_poi_STG_LH.txt','C19_tono_poi_STG_RH.txt',
                    'C20_tono_poi_STG_LH.txt','C20_tono_poi_STG_RH.txt',
                    'C21_tono_poi_STG_LH.txt','C21_tono_poi_STG_RH.txt',
                    'C22_tono_poi_STG_LH.txt','C22_tono_poi_STG_RH.txt',
                    'C23_tono_poi_STG_LH.txt','C23_tono_poi_STG_RH.txt',
                    
                    'C25_tono_poi_STG_LH.txt','C25_tono_poi_STG_RH.txt',
                    'C26_tono_poi_STG_LH.txt','C26_tono_poi_STG_RH.txt',
                    'C27_tono_poi_STG_LH.txt','C27_tono_poi_STG_RH.txt',
                    'C28_tono_poi_STG_LH.txt','C28_tono_poi_STG_RH.txt',
                    'C29_tono_poi_STG_RH.txt',
                    'C30_tono_poi_STG_LH.txt',
                    'C31_tono_poi_STG_RH.txt',
                    'C32_tono_poi_STG_LH.txt','C32_tono_poi_STG_RH.txt',
                    'C33_tono_poi_STG_LH.txt','C33_tono_poi_STG_RH.txt',
                    'C34_tono_poi_STG_RH.txt',
                    'C35_tono_poi_STG_RH.txt',
                    'C36_tono_poi_STG_LH.txt',
                    
                    'C38_tono_poi_STG_RH.txt',
                    
                    'C40_tono_poi_STG_RH.txt',
                    'C41_tono_poi_STG_LH.txt','C41_tono_poi_STG_RH.txt',
                    'C42_tono_poi_STG_LH.txt','C42_tono_poi_STG_RH.txt',
                    'C43_tono_poi_STG_LH.txt','C43_tono_poi_STG_RH.txt',
                    'C44_tono_poi_STG_LH.txt','C44_tono_poi_STG_RH.txt',
                    'C45_tono_poi_STG_LH.txt','C45_tono_poi_STG_RH.txt',
                    'C46_tono_poi_STG_LH.txt','C46_tono_poi_STG_RH.txt',
                    'C47_tono_poi_STG_LH.txt','C47_tono_poi_STG_RH.txt',
                    'C48_tono_poi_STG_LH.txt','C48_tono_poi_STG_RH.txt',
                    'C49_tono_poi_STG_LH.txt','C49_tono_poi_STG_RH.txt',
                    'C50_tono_poi_STG_LH.txt','C50_tono_poi_STG_RH.txt',
                    'C51_tono_poi_STG_LH.txt','C51_tono_poi_STG_RH.txt',
                    'C52_tono_poi_STG_LH.txt','C52_tono_poi_STG_RH.txt',
                    'C53_tono_poi_STG_LH.txt','C53_tono_poi_STG_RH.txt',
                    'C54_tono_poi_STG_LH.txt','C54_tono_poi_STG_RH.txt',
                    'C55_tono_poi_STG_LH.txt','C55_tono_poi_STG_RH.txt',
                    'C56_tono_poi_STG_LH.txt','C56_tono_poi_STG_RH.txt',
                    'C57_tono_poi_STG_LH.txt','C57_tono_poi_STG_RH.txt',
                    'C58_tono_poi_STG_LH.txt','C58_tono_poi_STG_RH.txt',
                    'C59_tono_poi_STG_LH.txt','C59_tono_poi_STG_RH.txt',
                    'C60_tono_poi_STG_LH.txt','C60_tono_poi_STG_RH.txt',
                    'C61_tono_poi_STG_LH.txt','C61_tono_poi_STG_RH.txt',
                    'C62_tono_poi_STG_LH.txt','C62_tono_poi_STG_RH.txt',
                    'C63_tono_poi_STG_LH.txt','C63_tono_poi_STG_RH.txt',
                    'C64_tono_poi_STG_LH.txt','C64_tono_poi_STG_RH.txt',
                    'C65_tono_poi_STG_LH.txt','C65_tono_poi_STG_RH.txt',
                    'C66_tono_poi_STG_LH.txt','C66_tono_poi_STG_RH.txt',
                    'C67_tono_poi_STG_LH.txt',
                    'C68_tono_poi_STG_LH.txt',
                    'C69_tono_poi_STG_LH.txt',
                    'C70_tono_poi_STG_RH.txt',
                    'C71_tono_poi_STG_LH.txt','C71_tono_poi_STG_RH.txt',
                    'C72_tono_poi_STG_LH.txt',
                    'C73_tono_poi_STG_RH.txt',
                    'C74_tono_poi_STG_LH.txt','C74_tono_poi_STG_RH.txt',
                    'C75_tono_poi_STG_LH.txt','C75_tono_poi_STG_RH.txt',
                    'C76_tono_poi_STG_LH.txt','C76_tono_poi_STG_RH.txt',
                    'C77_tono_poi_STG_LH.txt','C77_tono_poi_STG_RH.txt',
                    'C78_tono_poi_STG_LH.txt','C78_tono_poi_STG_RH.txt',
                    'C79_tono_poi_STG_LH.txt','C79_tono_poi_STG_RH.txt'
                    ]
big_dataset_anat = ['C1_anat_poi_STG_LH.txt','C1_anat_poi_STG_RH.txt',
                    'C2_anat_poi_STG_LH.txt','C2_anat_poi_STG_RH.txt',
                    'C3_anat_poi_STG_LH.txt','C3_anat_poi_STG_RH.txt',
                    'C4_anat_poi_STG_LH.txt','C4_anat_poi_STG_RH.txt',
                    'C5_anat_poi_STG_LH.txt','C5_anat_poi_STG_RH.txt',
                    'C6_anat_poi_STG_LH.txt','C6_anat_poi_STG_RH.txt',
                    'C7_anat_poi_STG_LH.txt','C7_anat_poi_STG_RH.txt',
                    'C8_anat_poi_STG_LH.txt','C8_anat_poi_STG_RH.txt',
                    'C9_anat_poi_STG_LH.txt','C9_anat_poi_STG_RH.txt',
                    'C10_anat_poi_STG_LH.txt','C10_anat_poi_STG_RH.txt',
                    'C11_anat_poi_STG_LH.txt','C11_anat_poi_STG_RH.txt',
                    'C12_anat_poi_STG_LH.txt','C12_anat_poi_STG_RH.txt',
                    'C13_anat_poi_STG_LH.txt','C13_anat_poi_STG_RH.txt',
                    'C14_anat_poi_STG_LH.txt','C14_anat_poi_STG_RH.txt',
                    'C15_anat_poi_STG_LH.txt',
                    'C16_anat_poi_STG_LH.txt',
                    
                    'C18_anat_poi_STG_LH.txt','C18_anat_poi_STG_RH.txt',
                    'C19_anat_poi_STG_LH.txt','C19_anat_poi_STG_RH.txt',
                    'C20_anat_poi_STG_LH.txt','C20_anat_poi_STG_RH.txt',
                    'C21_anat_poi_STG_LH.txt','C21_anat_poi_STG_RH.txt',
                    'C22_anat_poi_STG_LH.txt','C22_anat_poi_STG_RH.txt',
                    'C23_anat_poi_STG_LH.txt','C23_anat_poi_STG_RH.txt',
                    
                    'C25_anat_poi_STG_LH.txt','C25_anat_poi_STG_RH.txt',
                    'C26_anat_poi_STG_LH.txt','C26_anat_poi_STG_RH.txt',
                    'C27_anat_poi_STG_LH.txt','C27_anat_poi_STG_RH.txt',
                    'C28_anat_poi_STG_LH.txt','C28_anat_poi_STG_RH.txt',
                    'C29_anat_poi_STG_RH.txt',
                    'C30_anat_poi_STG_LH.txt',
                    'C31_anat_poi_STG_RH.txt',
                    'C32_anat_poi_STG_LH.txt','C32_anat_poi_STG_RH.txt',
                    'C33_anat_poi_STG_LH.txt','C33_anat_poi_STG_RH.txt',
                    'C34_anat_poi_STG_RH.txt',
                    'C35_anat_poi_STG_RH.txt',
                    'C36_anat_poi_STG_LH.txt',
                    
                    'C38_anat_poi_STG_RH.txt',
                    
                    'C40_anat_poi_STG_RH.txt',
                    'C41_anat_poi_STG_LH.txt','C41_anat_poi_STG_RH.txt',
                    'C42_anat_poi_STG_LH.txt','C42_anat_poi_STG_RH.txt',
                    'C43_anat_poi_STG_LH.txt','C43_anat_poi_STG_RH.txt',
                    'C44_anat_poi_STG_LH.txt','C44_anat_poi_STG_RH.txt',
                    'C45_anat_poi_STG_LH.txt','C45_anat_poi_STG_RH.txt',
                    'C46_anat_poi_STG_LH.txt','C46_anat_poi_STG_RH.txt',
                    'C47_anat_poi_STG_LH.txt','C47_anat_poi_STG_RH.txt',
                    'C48_anat_poi_STG_LH.txt','C48_anat_poi_STG_RH.txt',
                    'C49_anat_poi_STG_LH.txt','C49_anat_poi_STG_RH.txt',
                    'C50_anat_poi_STG_LH.txt','C50_anat_poi_STG_RH.txt',
                    'C51_anat_poi_STG_LH.txt','C51_anat_poi_STG_RH.txt',
                    'C52_anat_poi_STG_LH.txt','C52_anat_poi_STG_RH.txt',
                    'C53_anat_poi_STG_LH.txt','C53_anat_poi_STG_RH.txt',
                    'C54_anat_poi_STG_LH.txt','C54_anat_poi_STG_RH.txt',
                    'C55_anat_poi_STG_LH.txt','C55_anat_poi_STG_RH.txt',
                    'C56_anat_poi_STG_LH.txt','C56_anat_poi_STG_RH.txt',
                    'C57_anat_poi_STG_LH.txt','C57_anat_poi_STG_RH.txt',
                    'C58_anat_poi_STG_LH.txt','C58_anat_poi_STG_RH.txt',
                    'C59_anat_poi_STG_LH.txt','C59_anat_poi_STG_RH.txt',
                    'C60_anat_poi_STG_LH.txt','C60_anat_poi_STG_RH.txt',
                    'C61_anat_poi_STG_LH.txt','C61_anat_poi_STG_RH.txt',
                    'C62_anat_poi_STG_LH.txt','C62_anat_poi_STG_RH.txt',
                    'C63_anat_poi_STG_LH.txt','C63_anat_poi_STG_RH.txt',
                    'C64_anat_poi_STG_LH.txt','C64_anat_poi_STG_RH.txt',
                    'C65_anat_poi_STG_LH.txt','C65_anat_poi_STG_RH.txt',
                    'C66_anat_poi_STG_LH.txt','C66_anat_poi_STG_RH.txt',
                    'C67_anat_poi_STG_LH.txt',
                    'C68_anat_poi_STG_LH.txt',
                    'C69_anat_poi_STG_LH.txt',
                    'C70_anat_poi_STG_RH.txt',
                    'C71_anat_poi_STG_LH.txt','C71_anat_poi_STG_RH.txt',
                    'C72_anat_poi_STG_LH.txt',
                    'C73_anat_poi_STG_RH.txt',
                    'C74_anat_poi_STG_LH.txt','C74_anat_poi_STG_RH.txt',
                    'C75_anat_poi_STG_LH.txt','C75_anat_poi_STG_RH.txt',
                    'C76_anat_poi_STG_LH.txt','C76_anat_poi_STG_RH.txt',
                    'C77_anat_poi_STG_LH.txt','C77_anat_poi_STG_RH.txt',
                    'C78_anat_poi_STG_LH.txt','C78_anat_poi_STG_RH.txt',
                    'C79_anat_poi_STG_LH.txt','C79_anat_poi_STG_RH.txt'
                    ]
big_dataset_names = ['Subject 1 - LH','Subject 1 - RH',
                     'Subject 2 - LH','Subject 2 - RH',
                     'Subject 3 - LH','Subject 3 - RH',
                     'Subject 4 - LH','Subject 4 - RH',
                     'Subject 5 - LH','Subject 5 - RH',
                     'Subject 6 - LH','Subject 6 - RH',
                     'Subject 7 - LH','Subject 7 - RH',
                     'Subject 8 - LH','Subject 8 - RH',
                     'Subject 9 - LH','Subject 9 - RH',
                     'Subject 10 - LH','Subject 10 - RH',
                     'Subject 11 - LH','Subject 11 - RH',
                     'Subject 12 - LH','Subject 12 - RH',
                     'Subject 13 - LH','Subject 13 - RH',
                     'Subject 14 - LH','Subject 14 - RH',
                     'Subject 15 - LH',
                     'Subject 16 - LH',
                     
                     'Subject 18 - LH','Subject 18 - RH',
                     'Subject 19 - LH','Subject 19 - RH',
                     'Subject 20 - LH','Subject 20 - RH',
                     'Subject 21 - LH','Subject 21 - RH',
                     'Subject 22 - LH','Subject 22 - RH',
                     'Subject 23 - LH','Subject 23 - RH',
                      
                     'Subject 25 - LH','Subject 25 - RH',
                     'Subject 26 - LH','Subject 26 - RH',
                     'Subject 27 - LH','Subject 27 - RH',
                     'Subject 28 - LH','Subject 28 - RH',
                     'Subject 29 - RH',
                     'Subject 30 - LH',
                     'Subject 31 - RH',
                     'Subject 32 - LH','Subject 32 - RH',
                     'Subject 33 - LH','Subject 33 - RH',
                     'Subject 34 - RH',
                     'Subject 35 - RH',
                     'Subject 36 - LH',
                     
                     'Subject 38 - RH',
                     
                     'Subject 40 - RH',
                     'Subject 41 - LH','Subject 41 - RH',
                     'Subject 42 - LH','Subject 42 - RH',
                     'Subject 43 - LH','Subject 43 - RH',
                     'Subject 44 - LH','Subject 44 - RH',
                     'Subject 45 - LH','Subject 45 - RH',
                     'Subject 46 - LH','Subject 46 - RH',
                     'Subject 47 - LH','Subject 47 - RH',
                     'Subject 48 - LH','Subject 48 - RH',
                     'Subject 49 - LH','Subject 49 - RH',
                     'Subject 50 - LH','Subject 50 - RH',
                     'Subject 51 - LH','Subject 51 - RH',
                     'Subject 52 - LH','Subject 52 - RH',
                     'Subject 53 - LH','Subject 53 - RH',
                     'Subject 54 - LH','Subject 54 - RH',
                     'Subject 55 - LH','Subject 55 - RH',
                     'Subject 56 - LH','Subject 56 - RH',
                     'Subject 57 - LH','Subject 57 - RH',
                     'Subject 58 - LH','Subject 58 - RH',
                     'Subject 59 - LH','Subject 59 - RH',
                     'Subject 60 - LH','Subject 60 - RH',
                     'Subject 61 - LH','Subject 61 - RH',
                     'Subject 62 - LH','Subject 62 - RH',
                     'Subject 63 - LH','Subject 63 - RH',
                     'Subject 64 - LH','Subject 64 - RH',
                     'Subject 65 - LH','Subject 65 - RH',
                     'Subject 66 - LH','Subject 66 - RH',
                     'Subject 67 - LH',
                     'Subject 68 - LH',
                     'Subject 69 - LH',
                     'Subject 70 - RH',
                     'Subject 71 - LH','Subject 71 - RH',
                     'Subject 72 - LH',
                     'Subject 73 - RH',
                     'Subject 74 - LH','Subject 74 - RH',
                     'Subject 75 - LH','Subject 75 - RH',
                     'Subject 76 - LH','Subject 76 - RH',
                     'Subject 77 - LH','Subject 77 - RH',
                     'Subject 78 - LH','Subject 78 - RH',
                     'Subject 79 - LH','Subject 79 - RH'
                     ]
big_dataset_dupl = ['S','CD',
                    'S','CD',
                    'CD','CD',
                    'S','CD',
                    'S','CD',
                    'S','S',
                    'CD','CD',
                    'CD','PD',
                    'S','S',
                    'S','PD',
                    'CD','PD',
                    'S','S',
                    'S','PD',
                    'CD','CD'
                    'CD',
                    'S',
                    
                    'CD','S',
                    'S','CD',
                    'CD','CD',
                    'CD','CD',
                    'CD','CD',
                    'PD','CD',
                    
                    'S','S',
                    'S','CD',
                    'PD','PD',
                    'S','PD',
                    'CD',
                    'S',
                    'CD',
                    'S','CD',
                    'CD','PD',
                    'CD',
                    'CD',
                    'PD',
                    
                    'PD',
                    
                    'S',
                    'S','CD',
                    'S','CD',
                    'S','S',
                    'S','PD',
                    'CD','CD',
                    'S','PD',
                    'S','S',
                    'S','S',
                    'CD','CD',
                    'S','PD',
                    'S','PD',
                    'PD','S',
                    'S','CD',
                    'PD','PD',
                    'CD','CD',
                    'S','PD',
                    'S','S',
                    'CD','CD',
                    'CD','CD',
                    'PD','CD',
                    'S','PD',
                    'S','S',
                    'S','S',
                    'CD','CD',
                    'S','CD',
                    'S','PD',
                    'CD',
                    'CD',
                    'CD',
                    'PD',
                    'CD',
                    'S',
                    'PD',
                    'PD','CD',
                    'S',
                    'PD',
                    'CD','PD',
                    'CD','CD',
                    'S','S',
                    'S','CD',
                    'PD','PD',
                    'PD','CD']

big_dataset_targets = [0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       1,1,
                       1,
                       1,
                       
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       
                       0,0,
                       0,0,
                       0,0,
                       1,1,
                       1,
                       1,
                       1,
                       1,1,
                       0,0,
                       1,
                       1,
                       1,
                       
                       1,
                       
                       1,
                       1,1,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       0,0,
                       1,1,
                       1,1,
                       1,
                       1,
                       1,
                       1,
                       1,1,
                       1,
                       1,
                       1,1,
                       0,0,
                       0,0,
                       0,0,
                       1,1] 
'''
subj_number = np.shape(big_dataset_tono)[0]
subj_3D_data = np.ones([subj_number,5,6000])*(-2)
max_size_tono = 0
max_size_anat = 0
for i in range(subj_number):
    mydata_tono = import_function(big_dataset_tono[i])
    max_size_tono = np.max((max_size_tono,len(mydata_tono)))
    
    max_len = len(mydata_tono)
    # import x
    subj_3D_data[i,0,0:max_len] = mydata_tono[:,1]
    # import y
    subj_3D_data[i,1,0:max_len] = mydata_tono[:,2]
    # import z
    subj_3D_data[i,2,0:max_len] = mydata_tono[:,3]
    # import f
    subj_3D_data[i,3,0:max_len] = 14-mydata_tono[:,7]

    # import anatomy
for i in range(subj_number): # 37 missing
    mydata_anat = import_function(big_dataset_anat[i])
    max_size_anat = np.max((max_size_anat,len(mydata_anat)))
    max_len = len(mydata_anat)
    
    subj_3D_data[i,4,0:max_len] = mydata_anat[:,7]
'''
for i in range(3):
    title = big_dataset_names[i]+'_tono'
    data = subj_3D_data[i,:,:]
    until = list(data[3,:]).index(-2)
    xs = data[0,0:until]
    ys = data[1,0:until]
    zs = data[2,0:until]
    fs = data[3,0:until] 
    an = data[4,0:until]
    
    #plot_hull = False
    #xs,ys,zs,fs,an = data_in_hull(xs,ys,zs,fs,an,plot_hull)
    
    
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xs,ys, c = fs, cmap = 'jet')    
    plt.title(title)
    #plt.legend()
    cax, _ = matplotlib.colorbar.make_axes(ax)
    cbar = matplotlib.colorbar.ColorbarBase(cax, cmap='jet')
    cbar.ax.set_yticklabels(['high frequency', '','','','', 'low frequency'])  # vertically oriented colorbar
    #plt.show()
    output_dir = "../../figures/all_maps"
    #fig.savefig('{}/{}.png'.format(output_dir,title))
    
    
    title = big_dataset_names[i]+'_anat'
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xs,ys, c = an, cmap = 'gray')    
    plt.title(title)
    #plt.legend()
    cax, _ = matplotlib.colorbar.make_axes(ax)
    cbar = matplotlib.colorbar.ColorbarBase(cax, cmap='gray')
    cbar.ax.set_yticklabels(['< 0 convex', '','','','', '> 0 concave'])  # vertically oriented colorbar
    #plt.show()
    #fig.savefig('{}/{}.png'.format(output_dir,title))
    '''
    
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs,ys,zs, c = fs, cmap = 'jet')
    plt.title(title)
    plt.show()
    '''


# BYSECTING LINE - FIND 
scan_number = subj_number

# B) Only anat
anat_classify = np.zeros([scan_number,1])  # which gyrus shape does the person have? not used for now
fit_anat = np.zeros([scan_number,2])   # fit of parameters on the basis of anatomy
my_range = np.arange(subj_number)
for i in my_range:
    #ctl_anat_classify[i], fit_ctl_anat[i,:] = anatomy(ctl_threeD_data[i,:,:],ctl_name[i],plot_y_n_three_anat_regions_ctl,plot_y_n_anat_clusters_ctl,plot_y_n_fit_anat_ctl)
    #print('subject ',i)
    fit_anat[i,:] = anatomy_new(subj_3D_data[i,:,:],big_dataset_names[i], big_dataset_dupl[i], False, False, False)

# A) Only tono
fit_tono = np.zeros([scan_number,2])
for i in range(subj_number):
#for i in range(24,27):
    fit_tono[i,:] = bysect_line(subj_3D_data[i,:,:], big_dataset_names[i], fit_anat[i,:], target = big_dataset_targets[i], plot_y_n = False, target_yn = True) # NB here fs is already 14-fs

    
    
'''
i = 13 
perc_tono = 0.5
perc_anat = 1.-perc_tono
# Controls
fit_comb_tono_anat = perc_tono*fit_tono+perc_anat*fit_anat

#cfr_bysecting_lines(subj_3D_data[i,:,:],big_dataset_names[i],fit_tono[i,:],fit_anat[i,:],fit_comb_tono_anat[i,:])


cluster_num_subj = np.zeros([subj_number,3])
cluster_size_subj = np.zeros([subj_number,3])
for i in range(subj_number):
        cluster_num_subj[i,:], cluster_size_subj[i,:] = three_f_ranges(subj_3D_data[i,:,:],big_dataset_names[i], fit_tono[i,:], False, eps = 1.0, min_samples = 3)
    
 
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.set_title('CONTROLS Number of clusters')
ax1.set_xlabel('Number of clusters')
ax1.set_ylabel('Occurrency')
ax1.hist(cluster_num_subj, bins = 30, alpha = 0.4, label = ['Low frequency','Medium frequency','High frequency'], density = True, stacked = True)
ax1.legend()

ax2.set_title('Size of clusters - Epsilon = {}'.format(eps))
ax2.set_xlabel('Size of clusters')
ax2.set_ylabel('Occurrency')
ax2.hist(cluster_size_subj, bins = 30, alpha = 0.4, label = ['Low frequency','Medium frequency','High frequency'],density = True, stacked = True)
ax2.legend()


mean_dist_subj = np.zeros([subj_number,14])
above_minus_below_subj = np.zeros([subj_number,14])
# find the mean distance for each scan
for i in range(subj_number):
    mean_dist_subj[i,:], above_minus_below_subj[i,:] = mean_dist_b_line(subj_3D_data[i,:,:], big_dataset_names[i], fit_tono[i,:], False)
    
get_indexes = lambda x, x_s: [i for (y, i) in zip(x_s, range(len(x_s))) if x == y]
indexes_ctl = get_indexes(0,big_dataset_targets)
indexes_pt = get_indexes(1,big_dataset_targets)
# distance
mean_dist_ctl = [mean_dist_subj[j] for j in indexes_ctl]
mean_dist_pt = [mean_dist_subj[j] for j in indexes_pt]

mean_control = np.mean(mean_dist_ctl, axis = 0)
std_control = np.std(mean_dist_ctl, axis = 0)
mean_pt = np.mean(mean_dist_pt,axis = 0)
std_pt = np.std(mean_dist_pt, axis = 0)

mean_control = np.asarray(mean_control)[::-1]
std_control = np.asarray(std_control)[::-1]
mean_pt = np.asarray(mean_pt)[::-1]
std_pt = np.asarray(std_pt)[::-1]


lower_bound_ctl = mean_control - std_control
upper_bound_ctl = mean_control + std_control
lower_bound_pt = mean_pt - std_pt
upper_bound_pt = mean_pt + std_pt


fig,ax = plt.subplots(1)
ax.plot(np.arange(14),mean_control,lw = 2, color = 'black', label = 'Controls')
ax.fill_between(np.arange(14), lower_bound_ctl, upper_bound_ctl, facecolor = 'yellow', alpha = 0.2, label = 'std control')
ax.plot(np.arange(14),mean_pt,lw = 2, color = 'red', label = 'Patients')
ax.fill_between(np.arange(14), lower_bound_pt, upper_bound_pt, facecolor = 'orange', alpha = 0.5, label = 'std patients')
ax.legend(loc = 'upper left')
ax.set_xlabel('Frequency', fontsize = 16)
ax.set_ylabel('Mean distance', fontsize = 16)
ax.set_title('Average distance from tonotopic axis vs frequency', fontsize = 16)

# voxel difference
above_minus_below_ctl = [above_minus_below_subj[j] for j in indexes_ctl]
above_minus_below_pt = [above_minus_below_subj[j] for j in indexes_pt]

mean_of_diff_ctl = np.mean(above_minus_below_ctl, axis = 0)
mean_of_diff_pt = np.mean(above_minus_below_pt, axis = 0)
std_of_diff_ctl = np.std(above_minus_below_ctl, axis = 0)
std_of_diff_pt = np.std(above_minus_below_pt, axis = 0)

mean_of_diff_ctl = np.asarray(mean_of_diff_ctl)[::-1]
mean_of_diff_pt = np.asarray(mean_of_diff_pt)[::-1]
std_of_diff_ctl = np.asarray(std_of_diff_ctl)[::-1]
std_of_diff_pt = np.asarray(std_of_diff_pt)[::-1]

lower_bound_ctl_vox = mean_of_diff_ctl - std_of_diff_ctl
upper_bound_ctl_vox = mean_of_diff_ctl + std_of_diff_ctl
lower_bound_pt_vox = mean_of_diff_pt - std_of_diff_pt
upper_bound_pt_vox = mean_of_diff_pt + std_of_diff_pt


fig,ax = plt.subplots(1)
ax.plot(np.arange(14),mean_of_diff_ctl,lw = 2, color = 'black', label = 'Controls')
ax.fill_between(np.arange(14), lower_bound_ctl_vox, upper_bound_ctl_vox, facecolor = 'yellow', alpha = 0.4, label = 'std control')
ax.plot(np.arange(14),mean_of_diff_pt,lw = 2, color = 'red', label = 'Patients')
ax.fill_between(np.arange(14), lower_bound_pt_vox, upper_bound_pt_vox, facecolor = 'orange', alpha = 0.2, label = 'std patients')
ax.legend(loc = 'upper left')
ax.set_xlabel('Frequency', fontsize = 16)
ax.set_ylabel('Mean difference', fontsize = 16)
ax.set_title('Average difference above-below vs frequency', fontsize = 16)

# percentage of voxel distribution
# Find percentage of voxels per frequency
ctl_voxel_count = np.zeros([ctl_number,14])
for i in range(ctl_number):
    data = ctl_3D_data
    until = list(data[i,3,:]).index(-2)
    fs = data[i,3,0:until]
    for j in range(14):
        ctl_voxel_count[i,j] = sum(float(num) == j for num in fs)
    ctl_voxel_count[i,:] = ctl_voxel_count[i,:]/until  # divide by total number of voxels to find percentage
    
ctl_voxel_count_mean = np.mean(ctl_voxel_count, axis = 0)
ctl_voxel_count_std = np.std(ctl_voxel_count, axis = 0)
ctl_voxel_count_mean = np.asarray(ctl_voxel_count_mean)[::-1]
ctl_voxel_count_std = np.asarray(ctl_voxel_count_std)[::-1]

lower_bound_ctl_vox = ctl_voxel_count_mean-ctl_voxel_count_std
upper_bound_ctl_vox = ctl_voxel_count_mean+ctl_voxel_count_std

pt_voxel_count = np.zeros([pt_number,14])
for i in range(pt_number):
    data = pt_3D_data
    until = list(data[i,3,:]).index(-2)
    fs = data[i,3,0:until]
    for j in range(14):
        pt_voxel_count[i,j] = sum(float(num) == j for num in fs)
    pt_voxel_count[i,:] = pt_voxel_count[i,:]/until  # divide by total number of voxels to find percentage
    
pt_voxel_count_mean = np.mean(pt_voxel_count, axis = 0)
pt_voxel_count_std = np.std(pt_voxel_count, axis = 0)
pt_voxel_count_mean = np.asarray(pt_voxel_count_mean)[::-1]
pt_voxel_count_std = np.asarray(pt_voxel_count_std)[::-1]

lower_bound_pt_vox = pt_voxel_count_mean-pt_voxel_count_std
upper_bound_pt_vox = pt_voxel_count_mean+pt_voxel_count_std

fig,ax = plt.subplots(1)
ax.plot(np.arange(14),ctl_voxel_count_mean,lw = 2, color = 'red', label = 'Controls')
ax.fill_between(np.arange(14), lower_bound_ctl_vox, upper_bound_ctl_vox, facecolor = 'red', alpha = 0.3, label = 'std control')
ax.plot(np.arange(14),pt_voxel_count_mean,lw = 2, color = 'green', label = 'Patients')
ax.fill_between(np.arange(14), lower_bound_pt_vox, upper_bound_pt_vox, facecolor = 'green', alpha = 0.2, label = 'std patients')
ax.legend()
ax.set_xlabel('Frequency', fontsize = 16)
ax.set_ylabel('% number of voxels', fontsize = 16)
ax.set_title('Voxel percentage vs frequency', fontsize = 16)



def data_in_hull(xs,ys,zs,fs,an,plot_hull):
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
        small_hull[s,0] = x_hull - 0.25*(x_hull-center_x)
        small_hull[s,1] = y_hull - 0.25*(y_hull-center_y)
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
    xs = [points_x[idx] for idx in contained_idx[0]]
    ys = [points_y[idx] for idx in contained_idx[0]]
    zs = [zs[idx] for idx in contained_idx[0]]
    fs = [fs[idx] for idx in contained_idx[0]]
    an = [an[idx] for idx in contained_idx[0]]
    contained_points = np.column_stack((xs,ys))
    
    if plot_hull:
        pylab.scatter(contained_points[:,0],contained_points[:,1],color = 'k')
    
    return xs,ys,zs,fs,an
'''
'''
cluster_num_low = np.zeros(subj_number)
cluster_size_med = np.zeros(subj_number)
cluster_num_high = np.zeros(subj_number)
cluster_size_low = np.zeros(subj_number)
cluster_num_med = np.zeros(subj_number)
cluster_size_high = np.zeros(subj_number)
eps_loop = np.arange(1.,2.5,0.5)

for eps in eps_loop:

    for i in range(subj_number):
    #for i in range(0,1):
        plot_y_n_cluster_map_ctl = False
        _,_, cluster_num_low[i], cluster_num_med[i], cluster_num_high[i], cluster_size_low[i], cluster_size_med[i], cluster_size_high[i] = three_f_ranges(subj_3D_data[i,:,:],big_dataset_names[i], fit_anat[i,:], plot_y_n_cluster_map_ctl, eps = eps, min_samples = 3)
    
    get_indexes = lambda x, x_s: [i for (y, i) in zip(x_s, range(len(x_s))) if x == y]
    idx_1 = get_indexes(1,big_dataset_targets)
    idx_0 = get_indexes(0,big_dataset_targets)
    
    cluster_num_low_ctl = [cluster_num_low[i] for i in idx_0]
    cluster_size_low_ctl = [cluster_size_low[i] for i in idx_0]
    cluster_num_med_ctl = [cluster_num_med[i] for i in idx_0]
    cluster_size_med_ctl = [cluster_size_med[i] for i in idx_0]
    cluster_num_high_ctl = [cluster_num_high[i] for i in idx_0]
    cluster_size_high_ctl = [cluster_size_high[i] for i in idx_0]
    cluster_num_low_pt = [cluster_num_low[i] for i in idx_1]
    cluster_size_low_pt = [cluster_size_low[i] for i in idx_1]
    cluster_num_med_pt = [cluster_num_med[i] for i in idx_1]
    cluster_size_med_pt = [cluster_size_med[i] for i in idx_1]
    cluster_num_high_pt = [cluster_num_high[i] for i in idx_1]
    cluster_size_high_pt = [cluster_size_high[i] for i in idx_1]
    
    plot_y_n_cluster_hist_ctl_pt = False
    plot_y_n_cluster_hist_freq = True
    
        ###################################
  
    if plot_y_n_cluster_hist_freq:
        fig, (ax1, ax2) = plt.subplots(1, 2)
        ax1.set_title('Low frequency - # clusters')
        ax1.set_xlabel('Number of clusters')
        ax1.set_ylabel('Occurrency')
        ax1.hist(cluster_num_low_ctl, bins = 30, alpha = 0.4, label = 'Controls',density = True, stacked = True)
        ax1.hist(cluster_num_low_pt, bins = 30, alpha = 0.4, label = 'Patients',density = True, stacked = True)
        ax1.legend()
        
        ax2.set_title('Size - Epsilon = {}'.format(eps))
        ax2.set_xlabel('Size of clusters')
        ax2.set_ylabel('Occurrency')
        ax2.hist(cluster_size_low_ctl, bins = 30, alpha = 0.4, label = 'Controls',density = True, stacked = True)
        ax2.hist(cluster_size_low_pt, bins = 30, alpha = 0.4, label = 'Patients',density = True, stacked = True)
        ax2.legend()
        
        fig, (ax1, ax2) = plt.subplots(1, 2)
        ax1.set_title('Medium frequency - # clusters')
        ax1.set_xlabel('Number of clusters')
        ax1.set_ylabel('Occurrency')
        ax1.hist(cluster_num_med_ctl, bins = 30, alpha = 0.4, label = 'Controls',density = True, stacked = True)
        ax1.hist(cluster_num_med_pt, bins = 30, alpha = 0.4, label = 'Patients',density = True, stacked = True)
        ax1.legend()
        
        ax2.set_title('Size - Epsilon = {}'.format(eps))
        ax2.set_xlabel('Size of clusters')
        ax2.set_ylabel('Occurrency')
        ax2.hist(cluster_size_med_ctl, bins = 30, alpha = 0.4, label = 'Controls',density = True, stacked = True)
        ax2.hist(cluster_size_med_pt, bins = 30, alpha = 0.4, label = 'Patients',density = True, stacked = True)
        ax2.legend()
        
        fig, (ax1, ax2) = plt.subplots(1, 2)
        ax1.set_title('High frequency - # clusters')
        ax1.set_xlabel('Number of clusters')
        ax1.set_ylabel('Occurrency')
        ax1.hist(cluster_num_high_ctl, bins = 30, alpha = 0.4, label = 'Controls',density = True, stacked = True)
        ax1.hist(cluster_num_high_pt, bins = 30, alpha = 0.4, label = 'Patients',density = True, stacked = True)
        ax1.legend()
        
        ax2.set_title('Size - Epsilon = {}'.format(eps))
        ax2.set_xlabel('Size of clusters')
        ax2.set_ylabel('Occurrency')
        ax2.hist(cluster_size_high_ctl, bins = 30, alpha = 0.4, label = 'Controls',density = True, stacked = True)
        ax2.hist(cluster_size_high_pt, bins = 30, alpha = 0.4, label = 'Patients',density = True, stacked = True)
        ax2.legend()
'''