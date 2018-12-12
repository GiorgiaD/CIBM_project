# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:11:55 2018

@author: Giorgia
"""
from import_function import *
import scipy.io
import matplotlib

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

 
subj_number = 30    
for i in range(subj_number):
    title = big_dataset_names[i]+'_tono'
    data = subj_3D_data[i,:,:]
    until = list(data[3,:]).index(-2)
    xs = data[0,0:until]
    ys = data[1,0:until]
    zs = data[2,0:until]
    fs = data[3,0:until] 
    an = data[4,0:until]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xs,ys, c = fs, cmap = 'jet')    
    plt.title(title)
    plt.legend()
    cax, _ = matplotlib.colorbar.make_axes(ax)
    cbar = matplotlib.colorbar.ColorbarBase(cax, cmap='jet')
    cbar.ax.set_yticklabels(['high frequency', '','','','', 'low frequency'])  # vertically oriented colorbar
    #plt.show()
    output_dir = "../../figures/all_maps"
    fig.savefig('{}/{}.png'.format(output_dir,title))
    
    
    title = big_dataset_names[i]+'_anat'
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xs,ys, c = an, cmap = 'gray')    
    plt.title(title)
    plt.legend()
    cax, _ = matplotlib.colorbar.make_axes(ax)
    cbar = matplotlib.colorbar.ColorbarBase(cax, cmap='gray')
    cbar.ax.set_yticklabels(['< 0 convex', '','','','', '> 0 concave'])  # vertically oriented colorbar
    #plt.show()
    fig.savefig('{}/{}.png'.format(output_dir,title))
    
    
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs,ys,zs, c = fs, cmap = 'jet')
    plt.title(title)
    plt.show()
    

# BYSECTING LINE - FIND 
scan_number = subj_number
# A) Only tono
fit_tono = np.zeros([scan_number,2])
for i in range(subj_number):
    fit_tono[i,:] = bysect_line(subj_3D_data[i,:,:], big_dataset_names[i], False) # NB here fs is already 14-fs
   

# B) Only anat
anat_classify = np.zeros([scan_number,1])  # which gyrus shape does the person have?
fit_anat = np.zeros([scan_number,2])   # fit of parameters on the basis of anatomy
for i in range(30):
    #ctl_anat_classify[i], fit_ctl_anat[i,:] = anatomy(ctl_threeD_data[i,:,:],ctl_name[i],plot_y_n_three_anat_regions_ctl,plot_y_n_anat_clusters_ctl,plot_y_n_fit_anat_ctl)
    
    fit_anat[i,:] = anatomy_new(subj_3D_data[i,:,:],big_dataset_names[i], big_dataset_dupl[i], False, False, False)
    
i = 13 
perc_tono = 0.5
perc_anat = 1.-perc_tono
# Controls
fit_comb_tono_anat = perc_tono*fit_tono+perc_anat*fit_anat

cfr_bysecting_lines(subj_3D_data[i,:,:],big_dataset_names[i],fit_tono[i,:],fit_anat[i,:],fit_comb_tono_anat[i,:])


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
'''

mean_dist_subj = np.zeros([subj_number,14])
above_minus_below_subj = np.zeros([subj_number,14])
# find the mean distance for each scan
for i in range(subj_number):
    mean_dist_subj[i,:], above_minus_below_subj[i,:] = mean_dist_b_line(subj_3D_data[i,:,:], big_dataset_names[i], fit_tono[i,:], False)
    
